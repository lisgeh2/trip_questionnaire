import pandas as pd
import plotly.express as px
import HandleMeta
from colors import MULTIPLE_COLORS, C, BINAER_VERLAUF, BINAER_VERLAUF_OPPOSITE
from crunch_label import give_crunch_label
from typing import Literal, Optional, Union
from helpers import clean_plot_array, clean_value_labels
from ValueCalcHouse import ValueCalcHouse
from config import WEIGHTING

def create_barchart(
    df: pd.DataFrame,
    meta,
    col: str,
    current_break: Optional[str] = None,
    color: str = "blau",
    color_gradient: Optional[Literal["categories", "continuous"]] = None,
    horizontal: bool = False,
    farben_umkehren: bool = False,
    height: Optional[Union[int, float]] = 450,
    crunch_label_by: Optional[int] = None,
    weighting: Optional[str] = None,          # neu
    ):
    if weighting is None:                     # neu
        weighting = WEIGHTING
    _validate_inputs(df, col, current_break, color)


    global FARB_VERLAUF
    if farben_umkehren == True:
        FARB_VERLAUF = BINAER_VERLAUF_OPPOSITE
    else:
        FARB_VERLAUF = BINAER_VERLAUF

    value_labels = HandleMeta.get_value_labels(meta, col) or {}
    value_labels = clean_value_labels(value_labels)
    
    question = HandleMeta.get_column_label(meta, col)
    
    break_labels = HandleMeta.get_value_labels(meta, current_break) or {}
    break_labels = clean_value_labels(break_labels)
    break_labels = give_crunch_label(break_labels, crunch_label_by=crunch_label_by)
    

    if crunch_label_by:
        value_labels = give_crunch_label(value_labels, crunch_label_by=crunch_label_by)

    if current_break == "tz" or current_break is None:
        fig = return_aggregate_percent_fig(df, col, value_labels, color_gradient, horizontal, color, weighting=weighting)
    else:
        fig = return_break_values_fig(df, col, current_break, value_labels, break_labels, question, color, color_gradient, horizontal)

    fig.update_layout(
        height=height,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=20, b=20),
    )
    fig.update_xaxes(fixedrange=True)   # ← neu: kein Zoom/Pan auf x
    fig.update_yaxes(fixedrange=True)   # ← neu: kein Zoom/Pan auf y

    return fig


def return_aggregate_percent_fig(df, col, value_labels, color_gradient, horizontal, color,
                                 weighting=WEIGHTING):
    calc = ValueCalcHouse(df, col, value_labels=value_labels, weighting=weighting)

    codes  = calc.give_codes()               # Reihenfolge wie value_labels
    counts = calc.give_counts()              # gewichtet (bei tz = Fallzahl)
    values = calc.give_percentages()         # Prozente, schon gerundet -> Python-Liste
    n_list = calc.give_n()                   # ungewichtete Fallzahl je Kategorie

    labels = [str(value_labels[k]) for k in codes]
    texts  = [f"{p:.1f}%" for p in values]

    aggregated = True
    fig = give_bar_fig(
        color, color_gradient, horizontal, aggregated,
        labels=labels, values=values, texts=texts, col=col, value_labels=value_labels,
    )

    customdata = [[lab, cnt, pct] for lab, cnt, pct in zip(labels, n_list, values)]
    fig.update_traces(
        customdata=customdata,
        hovertemplate="<b>%{customdata[0]}</b><br>"
                      "(%{customdata[1]} Antworten)<br>"
                      "%{customdata[2]:.1f}%<extra></extra>",
    )

    fig.update_layout(coloraxis_showscale=False)

    if horizontal:
        fig.update_yaxes(type="category", categoryorder="array", categoryarray=labels)
        fig.update_xaxes(title="Anteil", ticksuffix=" %")
    else:
        fig.update_xaxes(type="category", categoryorder="array", categoryarray=labels)
        fig.update_yaxes(title="Anteil", ticksuffix=" %")
    return fig


def return_break_values_fig(df, col, current_break, value_labels, break_labels,
                            question, color, color_gradient, horizontal, weighting=None):
    if weighting is None:
        weighting = WEIGHTING

    # Gewichteter Mittelwert je Break-Kategorie via ValueCalcHouse
    rows = []
    for break_code, break_label in break_labels.items():
        sub_df = df[df[current_break] == break_code]
        calc = ValueCalcHouse(sub_df, col, value_labels=value_labels, weighting=weighting)
        mittelwert = calc.give_mean()
        if mittelwert is not None:
            rows.append({current_break: break_label, col: round(mittelwert, 2)})

    mean_df = pd.DataFrame(rows).sort_values(by=col, ascending=False)

    aggregated = False
    fig = give_bar_fig(
        color, color_gradient, horizontal, aggregated,
        mean_df=mean_df, current_break=current_break, col=col, question=question, value_labels=value_labels,
    )
    return fig


def handle_horizontal(x, y, horizontal):
    if not horizontal:
        orientation = "v"
        return x, y, orientation
    else:
        temp = x
        x = y
        y = temp
        orientation = "h"
        return x, y, orientation


def handle_color(color, color_gradient, values, num_categories):
    # Default Fallback
    color_continuous_scale = None
    color_discrete_sequence = [MULTIPLE_COLORS[color]]
    color_arg = None
    marker = None
    showlegend = False

    if color_gradient == "continuous":
        color_continuous_scale = "Blues"
        color_discrete_sequence = None
        color_arg = values
        marker = None
        showlegend = False
    elif color_gradient == "categories":
        color_continuous_scale = None
        color_discrete_sequence = None
        color_arg = None
        showlegend = True  # ✅ KEIN KOMMA
        marker = dict(color=FARB_VERLAUF[num_categories])

    return color_discrete_sequence, color_continuous_scale, color_arg, marker, showlegend  # ✅ Kein Komma nach showlegend


def give_bar_fig(color, color_gradient, horizontal, aggregated,
                 mean_df=None, labels=None, values=None, texts=None,
                 current_break=None, col=None, question=None, value_labels=None,):

    if aggregated:
        data = None
        x = labels
        y = values
        text = texts
        px_labels = None
        color_values = values
        num_categories = len(labels)
    else:
        data = mean_df
        x = current_break
        y = col
        text = mean_df[col].round(2)
        px_labels = {col: "Werte", current_break: ""}
        color_values = mean_df[col].values
        num_categories = len(mean_df)

    color_discrete_sequence, color_continuous_scale, color_arg, marker, showlegend = handle_color(color, color_gradient, color_values, num_categories)
    x, y, orientation = handle_horizontal(x, y, horizontal)

    fig = px.bar(
        data,
        x=x,
        y=y,
        text=text,
        labels=px_labels,
        color_discrete_sequence=color_discrete_sequence,
        color=color_arg,
        color_continuous_scale=color_continuous_scale,
        orientation=orientation,
    )
    if marker is not None:
        fig.update_traces(marker=marker)
    fig.update_layout(showlegend=showlegend)

    return fig



def _validate_inputs(df, col, current_break, color):
    if col != "tz":
        assert col in df.columns, f"col '{col}' is not a column in df"
    if current_break != "tz":
        assert current_break is None or current_break in df.columns, \
            f"current_break '{current_break}' is not a column in df"
    assert color in C, f"color must be one of {C}"