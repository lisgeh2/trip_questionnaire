"""
Smoke tests for streamlit_app.py.

The bar these set: the whole script executes top to bottom on the .sav path
without raising. Streamlit swallows exceptions into at.exception rather than
letting them propagate, so a plain "it imported fine" check would pass on a
broken app - every test here inspects at.exception explicitly.
"""

import pytest
from streamlit.testing.v1 import AppTest

# The app builds ~15 plotly figures over a full dataframe; the 3s default is tight.
TIMEOUT = 90


def _fmt(exceptions) -> str:
    """Readable failure message out of Streamlit's exception elements."""
    lines = []
    for e in exceptions:
        value = getattr(e, "value", e)
        etype = getattr(e, "type", type(value).__name__)
        lines.append(f"{etype}: {value}")
        tb = getattr(e, "stack_trace", None)
        if tb:
            lines.append("".join(tb) if isinstance(tb, list) else str(tb))
    return "\n".join(lines)


@pytest.fixture
def app(app_file, in_app_dir) -> AppTest:
    at = AppTest.from_file(str(app_file), default_timeout=TIMEOUT)
    at.run()
    return at


# ---------------------------------------------------------------------------
# The core assertion
# ---------------------------------------------------------------------------


def test_app_runs_without_exception(app):
    """The whole script executes cleanly. This is the one that matters."""
    assert not app.exception, "streamlit_app.py raised:\n" + _fmt(app.exception)


def test_app_reports_no_error_elements(app):
    """st.error()/st.exception() output means the app degraded even if it ran."""
    assert not app.error, "App rendered error elements:\n" + _fmt(app.error)


# ---------------------------------------------------------------------------
# Did it actually render, or did it just not crash?
# ---------------------------------------------------------------------------


def test_app_renders_expected_charts(app):
    """
    Guards against the silent-failure mode: no exception, but charts missing
    because a helper returned None instead of a figure.
    """
    assert len(app.get("plotly_chart")) >= 8, (
        f"expected the dashboard's plotly charts, got {len(app.get('plotly_chart'))}"
    )


def test_app_renders_kpi_and_header(app):
    """Header, KPI cards and footer all produce markdown/html."""
    assert len(app.markdown) >= 4, "header/KPI markdown missing"
    body = " ".join(m.value for m in app.markdown if isinstance(m.value, str))
    assert "sample-size" in body or "section-title" in body, (
        "expected the dashboard's CSS-classed markdown blocks"
    )


def test_app_has_no_none_labels(app):
    """
    Regression guard for the DATA_TYPE bug: when DATA_TYPE was 'jsonl',
    HandleMeta returned None for every label and 'None' leaked into the UI.
    """
    rendered = " ".join(
        str(el.value) for el in list(app.markdown) + list(app.subheader) if el.value is not None
    )
    assert "None" not in rendered, "a label rendered as 'None' - check config.DATA_TYPE"


# ---------------------------------------------------------------------------
# Interactive paths - these only execute on user input, so a plain run misses them
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "break_label",
    [
        "Kein Break",
        "Gemeinde",
        "Bildung",
        "Alter",
        "Geschlecht",
        "HH-Einkommen",
        "Siedlungsart",
    ],
)
def test_every_break_option_runs(app, break_label):
    """
    The break selectbox swaps create_barchart between its aggregate and
    grouped code paths. A first run only ever exercises the default option.
    """
    if not app.selectbox:
        pytest.skip("no selectbox in app")
    app.selectbox[0].set_value(break_label).run()
    assert not app.exception, f"break '{break_label}' raised:\n" + _fmt(app.exception)


def test_slider_filtering_runs(app):
    """
    The Gemeindegrösse slider narrows the dataframe before charting. A narrow
    window can empty out categories, which is exactly where division-by-zero
    and empty-label bugs surface.
    """
    if not app.slider:
        pytest.skip("no slider in app")
    slider = app.slider[0]
    low, high = slider.value
    if low == high:
        pytest.skip("slider range is degenerate")
    slider.set_value((low, low)).run()  # narrowest possible selection
    assert not app.exception, "narrow slider selection raised:\n" + _fmt(app.exception)


def test_tabs_all_render(app):
    """All four channel tabs build their own barchart."""
    assert len(app.tabs) >= 4, f"expected 4 channel tabs, got {len(app.tabs)}"
    assert not app.exception, _fmt(app.exception)
