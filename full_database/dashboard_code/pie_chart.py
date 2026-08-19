import pandas as pd
import plotly.express as px
import HandleMeta
from colors import C_LIST
from crunch_label import give_crunch_label
from typing import Literal, Optional, Union
from helpers import clean_value_labels
from ValueCalcHouse import ValueCalcHouse
from config import WEIGHTING




def create_piechart(
    df: pd.DataFrame,
    meta,
    col: str,
    hole: float = 0.4,
    height: Optional[Union[int, float]] = 200,
    crunch_label_by: Optional[int] = None,
    weighting = WEIGHTING
    ):
    
    value_labels = HandleMeta.get_value_labels(meta, col) or {}
    value_labels = clean_value_labels(value_labels)
    
    fig_calc = ValueCalcHouse(df, col, value_labels=value_labels, weighting=weighting)
    counts = fig_calc.give_counts()
    n_list = fig_calc.give_n()

    labels_list = list(value_labels.values())
    labels_list = give_crunch_label(labels_list, crunch_label_by=crunch_label_by)


    fig = px.pie(
            names=labels_list,
            values=counts,
            hole=hole,
            color_discrete_sequence=C_LIST,
        )

    fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            customdata=[[n] for n in n_list],      # eine Spalte: Fallzahl je Segment
            hovertemplate="<b>%{label}</b><br>"
                        "(%{customdata[0]} Antworten)<br>"
                        "%{percent}<extra></extra>",
        )

    fig.update_layout(
        height=height,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=5, r=20, t=0, b=0),
    )
    return fig