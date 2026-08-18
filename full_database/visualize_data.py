from process_df import build_df
from process_meta import transform_to_meta, DONT_KNOW

import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Responses", layout="wide")
st.title("Questionnaire responses")

df = build_df()
meta = transform_to_meta()

st.caption(f"{len(df)} submissions")


def counts_frame(key, entry):
    values = pd.to_numeric(df[key], errors="coerce")
    values = values[values != DONT_KNOW].dropna()

    labels = {c: l for c, l in entry["item_labels"].items() if c != DONT_KNOW}
    if not labels:                       # body_weight etc. — no fixed scale
        if values.empty:
            return None
        labels = {c: str(c) for c in sorted(values.unique())}

    codes = sorted(labels)
    counts = values.value_counts().reindex(codes, fill_value=0)

    return pd.DataFrame({
        "code": codes,
        "n": [int(counts[c]) for c in codes],
        "answer": [labels[c] for c in codes],
    })


for key, entry in meta.items():
    if entry["type"] not in ("slider", "radio"):
        continue

    counts = counts_frame(key, entry)
    if counts is None:
        continue

    st.subheader(entry["label"])

    chart = (
        alt.Chart(counts)
        .mark_bar(cornerRadius=3)
        .encode(
            x=alt.X("answer:N", sort=list(counts["answer"]), title=None,
                    axis=alt.Axis(labelAngle=-40, labelLimit=200)),
            y=alt.Y("n:Q", title="responses", axis=alt.Axis(tickMinStep=1)),
            color=alt.Color("code:Q", legend=None, scale=alt.Scale(scheme="viridis")),
            tooltip=["answer", "n"],
        )
        .properties(height=260)
    )
    st.altair_chart(chart, use_container_width=True)

st.divider()
st.subheader("Raw data")
st.dataframe(df)