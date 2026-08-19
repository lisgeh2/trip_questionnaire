import pandas as pd
import plotly.express as px
import HandleMeta
from colors import MULTIPLE_COLORS, CORE_COLOR, BACKGROUND, FARBEN_4_ABSTUFUNGEN, FARBEN_4, BINAER_VERLAUF, BINAER_VERLAUF_OPPOSITE
import plotly.graph_objects as go
from crunch_label import give_crunch_label
from typing import Literal, Optional, Union, List
from helpers import clean_value_labels
from ValueCalcHouse import ValueCalcHouse
from config import WEIGHTING

def create_multi_stacked_barchart(
    df: pd.DataFrame,
    meta,
    cols: List[str],                       # z.B. ["GFS2_1", "GFS2_2", "GFS2_3"]
    farben_umkehren: bool = False,
    height: Optional[Union[int, float]] = None,
    crunch_label_by: Optional[int] = None,
    crunch_item_label_by: Optional[int] = None,
    group_label: Optional[str] = None,
    weighting: Optional[str] = None
):
    if weighting is None:
            weighting = WEIGHTING
    farb_verlauf = BINAER_VERLAUF_OPPOSITE if farben_umkehren else BINAER_VERLAUF

    value_labels = HandleMeta.get_value_labels(meta, cols[0]) or {}
    value_labels = clean_value_labels(value_labels)          # SPSS-Sentinels raus

    codes = list(value_labels.keys())
    labels_list = list(value_labels.values())
    labels_list = give_crunch_label(labels_list, crunch_label_by=crunch_label_by)  # LISTE rein
    n_categories = len(codes)
    # Item-Beschriftungen für die y-Achse (eine pro Frage)
    item_labels = [HandleMeta.get_column_label(meta, c) for c in cols]
    if group_label:
        item_labels = [item_label.replace(group_label, "").strip() for item_label in item_labels]
        print("is running")
        print(f"{group_label}")
    item_labels = give_crunch_label(item_labels, crunch_label_by=crunch_item_label_by) 


    # Pro Kategorie eine Zeile Anteile/Counts über alle Items berechnen
    # percent_matrix[i][j] = Anteil Kategorie i im Item j
    # Pro Item ein ValueCalcHouse -> Ergebnisse sind je Item eine Liste über Kategorien
    pct_per_item, n_per_item = [], []
    for c in cols:
        calc = ValueCalcHouse(df, c, value_labels=value_labels, weighting=weighting)
        pct_per_item.append(calc.give_percentages())   # [item][kategorie]
        n_per_item.append(calc.give_n())                # ungewichtete Fallzahl

    # Transponieren zu [kategorie][item], weil ein Trace = eine Kategorie über alle Items
    percent_matrix = [list(row) for row in zip(*pct_per_item)]
    count_matrix   = [list(row) for row in zip(*n_per_item)]

    # Stacked bar chart: ein Trace pro Antwortkategorie, x/y als Liste über die Items
    fig = go.Figure()
    for i, name in enumerate(labels_list):
        x_vals = percent_matrix[i]
        cnts = count_matrix[i]
        fig.add_trace(go.Bar(
            x=x_vals,
            y=item_labels,
            name=name,
            orientation='h',
            marker=dict(color=farb_verlauf[len(labels_list)][i]),
            text=[f"{p:.0f}%" for p in x_vals],
            textposition="inside",
            textfont=dict(color="white", size=12),
            customdata=cnts,
            hovertemplate=f"<b>{name}</b><br>%{{x:.1f}}% (%{{customdata}} Antworten)<extra></extra>",
        ))

    height = height or (60 * len(cols) + 90)                 # Höhe wächst mit Itemzahl

    fig.update_layout(
        barmode='stack',
        height=height,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="top", y=-0.15,
            xanchor="left", x=0,
        ),
        margin=dict(l=10, r=10, t=20, b=10),

        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            range=[0, 100],
            showticklabels=False,
            showgrid=False,
            zeroline=False,
        ),
        yaxis=dict(
            showticklabels=True,                             # Items müssen erkennbar sein
            showgrid=False,
            autorange="reversed",
            automargin=True,
        ),
    )
    fig.update_xaxes(fixedrange=True)   # ← neu: kein Zoom/Pan auf x
    fig.update_yaxes(fixedrange=True)   # ← neu: kein Zoom/Pan auf y

    return fig