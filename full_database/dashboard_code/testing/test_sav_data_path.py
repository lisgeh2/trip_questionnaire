"""
Targeted regression tests for the .sav data path.

The app-level smoke test proves the script runs. These prove it runs *correctly*
on the sav path - covering the two failure modes that don't raise on their own:

  * DATA_TYPE pointing anywhere but "sav", which makes every HandleMeta lookup
    return None and only blows up later, deep inside a chart helper.
  * Codes present in the data that have no matching value label, which is the
    KeyError: np.float64(1.0) family.
"""

import pandas as pd
import pytest

import config
import HandleMeta
import helpers as h
from conftest import BREAK_COLUMNS, QUESTION_COLUMNS
from density_chart import create_density_plot
from multi_stacked_barchart import create_multi_stacked_barchart
from pie_chart import create_piechart
from single_barchart import create_barchart
from stacked_barchart import create_stacked_bar
from ValueCalcHouse import ValueCalcHouse


# ---------------------------------------------------------------------------
# Config contract
# ---------------------------------------------------------------------------


def test_data_type_is_sav():
    """
    HandleMeta binds DATA_TYPE at import time (from config import DATA_TYPE),
    so this value is fixed the moment the process starts. Anything but "sav"
    silently returns None from every label lookup.
    """
    assert config.DATA_TYPE == "sav", (
        f"config.DATA_TYPE is {config.DATA_TYPE!r}; the sav path needs 'sav'"
    )


def test_handlemeta_agrees_with_config():
    """HandleMeta's import-time copy must not have drifted from config."""
    assert HandleMeta.DATA_TYPE == config.DATA_TYPE


def test_weighting_column_exists(loaded_sav):
    """give_counts() indexes df[WEIGHTING] with no guard - missing column = KeyError."""
    df, _ = loaded_sav
    assert config.WEIGHTING in df.columns, (
        f"WEIGHTING={config.WEIGHTING!r} is not a column in the .sav"
    )


# ---------------------------------------------------------------------------
# Metadata lookups return real values, not None
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("col", QUESTION_COLUMNS + BREAK_COLUMNS)
def test_column_label_is_a_string(loaded_sav, col):
    _, meta = loaded_sav
    label = HandleMeta.get_column_label(meta, col)
    assert isinstance(label, str) and label, f"{col}: expected a label, got {label!r}"


@pytest.mark.parametrize("col", QUESTION_COLUMNS + BREAK_COLUMNS)
def test_value_labels_are_a_dict(loaded_sav, col):
    _, meta = loaded_sav
    labels = HandleMeta.get_value_labels(meta, col)
    assert isinstance(labels, dict), f"{col}: expected a dict, got {type(labels).__name__}"


@pytest.mark.parametrize("col", QUESTION_COLUMNS + BREAK_COLUMNS)
def test_every_code_in_data_has_a_label(loaded_sav, col):
    """
    The exact bug behind KeyError: np.float64(1.0).

    ValueCalcHouse.give_codes() falls back to reading distinct values off the
    dataframe whenever value_labels is empty, and the chart helpers then index
    value_labels with those codes. Any code without a label is a crash.
    """
    df, meta = loaded_sav
    labels = h.clean_value_labels(HandleMeta.get_value_labels(meta, col) or {})
    codes = ValueCalcHouse(df, col, meta=meta).give_codes()
    missing = [c for c in codes if c not in labels]
    assert not missing, f"{col}: codes without a value label -> {missing}"


def test_sentinels_are_stripped(loaded_sav):
    """clean_value_labels must drop the 99999xxx missing-data codes."""
    _, meta = loaded_sav
    labels = HandleMeta.get_value_labels(meta, "GFS1_1")
    assert all(k < 99999990 for k in h.clean_value_labels(labels))


def test_group_label_extraction(loaded_sav):
    """extract_group_label feeds the multi-stacked chart's title."""
    df, meta = loaded_sav
    group_label = h.extract_group_label(df, meta, QUESTION_COLUMNS[1:])
    assert isinstance(group_label, str) and group_label.strip()


# ---------------------------------------------------------------------------
# Chart helpers build a figure for every column the app uses
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("col", QUESTION_COLUMNS)
@pytest.mark.parametrize("break_col", BREAK_COLUMNS)
def test_barchart_every_column_and_break(loaded_sav, col, break_col):
    """Both create_barchart code paths (aggregate and grouped) over every combo."""
    df, meta = loaded_sav
    fig = create_barchart(df, meta, col, break_col, height=300)
    assert fig is not None and len(fig.data) > 0, f"{col}/{break_col} produced an empty figure"


@pytest.mark.parametrize("horizontal", [True, False])
@pytest.mark.parametrize("gradient", [None, "categories", "continuous"])
def test_barchart_render_options(loaded_sav, horizontal, gradient):
    """Orientation and colour-gradient branches of handle_color."""
    df, meta = loaded_sav
    fig = create_barchart(
        df, meta, "GFS1_1", "tz", horizontal=horizontal, color_gradient=gradient, height=300
    )
    assert fig is not None and len(fig.data) > 0


@pytest.mark.parametrize("color", ["grün", "rot", "blau", "gelb"])
def test_barchart_named_colors(loaded_sav, color):
    """FARBEN_4 keys - regression guard for the C/MULTIPLE_COLORS rename."""
    df, meta = loaded_sav
    assert create_barchart(df, meta, "GFS1_1", "tz", color=color, height=300) is not None


@pytest.mark.parametrize("col", QUESTION_COLUMNS)
def test_stacked_bar(loaded_sav, col):
    df, meta = loaded_sav
    assert create_stacked_bar(df, meta, col, height=140) is not None


@pytest.mark.parametrize("col", BREAK_COLUMNS[1:])
def test_piechart(loaded_sav, col):
    df, meta = loaded_sav
    assert create_piechart(df, meta, col, height=120) is not None


def test_density_plot(loaded_sav):
    df, meta = loaded_sav
    assert create_density_plot(df, meta, "GFS2_3", color="grün", height=220, smoothness=0.66) is not None


def test_multi_stacked_barchart(loaded_sav):
    df, meta = loaded_sav
    cols = QUESTION_COLUMNS[1:]
    group_label = h.extract_group_label(df, meta, cols)
    fig = create_multi_stacked_barchart(
        df, meta, cols, height=300, crunch_label_by=13,
        crunch_item_label_by=12, group_label=group_label, farben_umkehren=False,
    )
    assert fig is not None and len(fig.data) > 0


# ---------------------------------------------------------------------------
# Edge cases that show up once real users start filtering
# ---------------------------------------------------------------------------


def test_barchart_on_filtered_subset(loaded_sav):
    """The Gemeindegrösse slider charts a filtered frame, not the full one."""
    df, meta = loaded_sav
    smallest = df["gemeinde_gr_break"].min()
    subset = df[df["gemeinde_gr_break"] == smallest].reset_index(drop=True)
    assert not subset.empty
    assert create_barchart(subset, meta, "GFS2_3", None, horizontal=True, height=220) is not None


def test_percentages_sum_to_100(loaded_sav):
    """Weighted percentages should total ~100 - catches weighting mistakes."""
    df, meta = loaded_sav
    pct = ValueCalcHouse(df, "GFS1_1", meta=meta).give_percentages()
    assert pct, "no percentages returned"
    assert abs(sum(pct) - 100.0) < 1.0, f"percentages sum to {sum(pct)}"


def test_total_n_is_positive(loaded_sav):
    df, meta = loaded_sav
    assert ValueCalcHouse(df, "GFS1_1", meta=meta).give_total_n() > 0


def test_empty_frame_does_not_hang(loaded_sav):
    """
    A slider range matching nobody yields an empty frame. Raising here is
    acceptable and informative; returning a broken figure silently is not.
    """
    df, meta = loaded_sav
    empty = df.iloc[0:0].copy()
    try:
        fig = create_barchart(empty, meta, "GFS1_1", "tz", height=200)
    except (ZeroDivisionError, ValueError, KeyError, IndexError):
        pytest.skip("empty frame raises - acceptable, but worth guarding in the app")
    assert fig is not None
