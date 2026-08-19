# ============================================================
#  Marktforschungs-Dashboard v2 · Streamlit + Plotly
#  Enthält: Linie, Donut, Stacked Bar, Spider/Radar,
#           Heatmap, Bubble, Sankey, Balken, Zufriedenheit
#
#  Installation:  pip install streamlit plotly pandas
#  Starten:       streamlit run
# ============================================================

import config
import os
from pathlib import Path
import pyreadstat
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np
from colors import MULTIPLE_COLORS, CORE_COLOR, BACKGROUND
from global_css import GLOBAL
from header import header
import helpers as h
from KpiRenderer import KpiRenderer
import pickle
import plotly.express as px
from single_barchart import create_barchart
from stacked_barchart import create_stacked_bar
from density_chart import create_density_plot
from multi_stacked_barchart import create_multi_stacked_barchart
import HandleMeta
from HandleMeta import load_local_thing
from config import WEIGHTING
import altair as alt
from pie_chart import create_piechart
from big_number import big_number
from footer import footer
import plotly.express as px
from card_handler import CardHandler
from crunch_label import give_crunch_label
cards = CardHandler()


@st.cache_data
def load_data():
    HERE = Path(__file__).parent
    sav_path = HERE / "fertig_all_waves_UV_RANDOM.sav"
    print("Looking for:", sav_path)
    print("Exists?", sav_path.exists())
    df, meta = pyreadstat.read_sav(str(HERE / "fertig_all_waves_UV_RANDOM.sav"))
    return df, meta

df, meta = load_data()

# define weighting and your environment in the config.py file

if IN_GFS:
    os.chdir(Path(__file__).parent)


# Nur wenn man im gfs environment ist, und zugang auf den Hintergrund-Code hat, kann man den metatable laden.
# Wenn man das nicht hat, muss man eine (broken) eigenfunktion verwenden, welche die Labels über meta holt. (siehe HandleMeta)
# Dort kann man auch IN_GFS auf True oder False setzen

if IN_GFS:
    metatable = load_local_thing(path="MetaTable.pkl")
    HERE = Path(__file__).parent
    df, meta = pyreadstat.read_sav(str(HERE / "fertig_all_waves_UV_RANDOM.sav"))
else:
    df, meta = pyreadstat.read_sav("fertig_all_waves_UV_RANDOM.sav")


# ── SEITEN-KONFIGURATION ────────────────────────────────────
st.set_page_config(
    page_title="gfs-Dashboard",
    page_icon="gfs.png",
    layout="wide",
)

# ── GLOBALES CSS ─────────────────────────────────────────────
st.markdown(GLOBAL, unsafe_allow_html=True)

st.markdown(h.set_background(hex_color=BACKGROUND[1]), unsafe_allow_html=True)

# ── HEADER ──────────────────────────────────────────────────
st.markdown(
    header(
        title="OMNIBUS NOVEMBER 2025",
        subtitle="Zentrale Kennzahlen, Verhaltensmuster und Trends auf einen Blick. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.",
        year=2026,
        window="Marktforschungs-Dashboard",
    ),
    unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
#  KPI-KARTEN
# ══════════════════════════════════════════════════════════
kpi = KpiRenderer(df)
kpi.render_section_title()

k1, k2, k3, k4 = st.columns(4)

# kpi.anzahl_befragte_mit_jahr(k1)

kpi.render(k1, "Stichprobengrösse", "1019", "+5 % Gegenüber dem letzten Jahr", "up")
kpi.render(k2, "Methode", "MIXED", "10% weniger CATI als letztes Jahr (50/50)", "down")
kpi.bearbeitungszeit(k3, "überdurschnittliche Zeit", "up")
kpi.render(k4, "Befragungszeitraum", "18 Tage", "von 3. - 21.  November", "down")

st.divider()
# ══════════════════
# ══════════════════════════════════════════════════════════
#  GFS1_1 · MITTELWERTE NACH JAHR
# ══════════════════════════════════════════════════════════


b1, b2 = st.columns([1.5, 2.5])

with b1:
    with st.container(key="karte2"):
        h.set_subtle_title(st, "GFS1_1", "Mittelwerte nach Break")
        st.subheader(HandleMeta.get_column_label(meta, "GFS1_1"))

        break_options = {
            "Kein Break": "tz",
            "Gemeinde": "gemeinde_gr_break",
            "Bildung": "education_break",
            "Alter": "alter_break",
            "Geschlecht": "gender_break",
            "HH-Einkommen": "einkommen_break_spez",
            "Siedlungsart": "siedlungsart_break"
        }

        selected_break_label = st.selectbox(
            "Break auswählen",
            list(break_options.keys())
        )
        current_break = break_options[selected_break_label]

        fig = create_barchart(df, meta, "GFS1_1", current_break, horizontal=False, color_gradient="categories", height=335)
        st.plotly_chart(fig, use_container_width=True)
        h.set_sample_size(st, col="GFS1_1", meta=meta, df=df)


# ── PieChart ──────────────────────────────────────────────────

b2_1, b2_2 = b2.columns([2, 1])

with b2_2:
    with st.container(key="karte5"):
        h.set_subtle_title(st, "Stichprobenzusammensetzung", "Piechart")
        # p2_1, p2_2, p2_3 = st.columns(3)
        st.text("Geschlecht")
        fig = create_piechart(df, meta, "gender_break", height=120)
        st.plotly_chart(fig, use_container_width=True)
        st.text("Bildung")
        fig = create_piechart(df, meta, "education_break", height=120)
        st.plotly_chart(fig, use_container_width=True)
        st.text("Alter")
        fig = create_piechart(df, meta, "alter_break", height=120)
        st.plotly_chart(fig, use_container_width=True)


# ── Another chart ──────────────────────────────────────────────────
b2_11, b2_22 = b2_1.columns([1, 1])


big_number(b2_11, "GFS2_2", "Kommunikation der Gemeinde", "22", "... sind nicht oder überhaupt nicht zufrieden", color="grün", add_percent=True, height=280)
big_number(b2_22, "GFS2_2", "Kommunikation der Gemeinde", "39", "... nutzen Social Media-Kanäle nicht", color="gelb", add_percent=True, height=280)

fig = create_barchart(df, meta, "GFS2_2", "tz", color="gelb", horizontal=True)

# b2_1.plotly_chart(fig, use_container_width=True)


# ── Big Number Card ──────────────────────────────────────────────────
n2_1, n2_2 = b2.columns([1, 1])


# ── Stacked Bar Chart ──────────────────────────────────────────────────


with b2_1.container(key="karte6"):
    h.set_subtle_title(st, "GFS2_1", "Stacked Barchart")
    st.subheader(HandleMeta.get_column_label(meta, "GFS2_1"))
    fig = create_stacked_bar(df, meta, "GFS2_1", height=140)
    st.plotly_chart(fig, use_container_width=True)
    h.set_sample_size(st, col="GFS2_1", meta=meta, df=df)

# ──  Bar With Slider ──────────────────────────────────────────────────


h1, h2 = st.columns([1, 1])

with h1.container(key="karte8"):
    h.set_subtle_title(st, "GFS2_3", "Stacked Barchart")
    st.subheader(HandleMeta.get_column_label(meta, "GFS2_3"))
    min_age, max_age = st.slider(
        "Gemeindegrösse wählen",
        min_value=int(df["gemeinde_gr_break"].min()),
        max_value=int(df["gemeinde_gr_break"].max()),
        value=(int(df["gemeinde_gr_break"].min()), int(df["gemeinde_gr_break"].max())),
        step=1,
        help="Nur Personen in diesee Gemeindegrösse werden angezeigt"
    )

    filtered_df = df[
        (df["gemeinde_gr_break"] >= min_age) &
        (df["gemeinde_gr_break"] <= max_age)
    ].reset_index(drop=True)

    fig = create_barchart(filtered_df, meta, "GFS2_3", current_break=None, horizontal=True, color="grün", height=220, crunch_label_by=10)
    st.plotly_chart(fig, use_container_width=True)
    fig = create_density_plot(filtered_df, meta, "GFS2_3", color="grün", height=220, smoothness=0.66)
    st.plotly_chart(fig, use_container_width=True)
    h.set_sample_size(st, col="GFS2_3", meta=meta, df=filtered_df)


# ──  Bar With Slider ──────────────────────────────────────────────────


with h2.container(key="karte10"):
    h.set_subtle_title(st, "GFS2", "Different Charts")
    st.subheader("Falls Sie die folgenden Kommunikationskanäle Ihrer Gemeinde bzw. Stadt nutzen: Wie zufrieden sind Sie damit?")
    tab1, tab2, tab3, tab4 = st.tabs(["Webseite", "Social Media-Kanäle", "Mitteilungsblatt/Gemeindeblatt", "Newsletter per E-Mail"])
    with tab1:
        st.subheader("Webseite der Gemeinde/Stadt")
        fig = create_barchart(df, meta, "GFS2_1", color_gradient="categories", height=453, crunch_label_by=10)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Social Media-Kanäle der Gemeinde/Stadt")
        fig = create_barchart(df, meta, "GFS2_2", color_gradient="categories", height=453, crunch_label_by=11)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Mitteilungsblatt/Gemeindeblatt")
        fig = create_barchart(df, meta, "GFS2_3", color_gradient="categories", height=453, crunch_label_by=12)
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.subheader("Newsletter per E-Mail")
        fig = create_barchart(df, meta, "GFS2_4", color_gradient="categories", height=453, crunch_label_by=13)
        st.plotly_chart(fig, use_container_width=True)

    h.set_sample_size(st, col="GFS2_4", meta=meta, df=df)
    


# ── New Multis ──────────────────────────────────────────────────

x1, x2, = st.columns([2, 1])
with x1:
    with st.container(key="karte16"):
        h.set_subtle_title(st, "GFS2", "Different Charts")
        group_label = h.extract_group_label(df, meta, ["GFS2_1", "GFS2_2", "GFS2_3", "GFS2_4"])
        st.subheader(group_label)
        fig = create_multi_stacked_barchart(
            df, meta,
            ["GFS2_1", "GFS2_2", "GFS2_3", "GFS2_4"],
            height=300,
            crunch_label_by=13,
            crunch_item_label_by = 12,
            group_label=group_label,
            farben_umkehren=False
        )
        st.plotly_chart(fig, use_container_width=True)


# ── FOOTER ──────────────────────────────────────────────────

st.divider()

st.html(footer(
    logos=["gfs.png", "uni.png", "kmu.png"]
))
st.caption("gfs-Demo-Dashboard · Daten nicht akkurat · Erstellt von Lisa Gehrig · 22.04.2026")
