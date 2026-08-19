from config import STYLE

def give_multiple_colors():
    if STYLE == "gfs":
        return [
                "#b24d24",  # rot
                "#3c699a",  # blau
                "#4c7a3a",  # gruen
                "#c48a2a",  # gelb
                "#7c5cbf",  # purple
                "#1a1a2e",  # dunkel
                "#7a7269",  # grau
                "#f5f0e8",  # paper
                ]
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_core_color():
    if STYLE == "gfs":
        return [
    "#3c699a",    # 0% transparenz / 100% sichtbar
    "#3c699aE6",  # 10% transparenz / 90% sichtbar
    "#3c699aCC",  # 20% transparenz / 80% sichtbar
    "#3c699aB3",  # 30% transparenz / 70% sichtbar
    "#3c699a99",  # 40% transparenz / 60% sichtbar
    "#3c699a80",  # 50% transparenz / 50% sichtbar
    "#3c699a66",  # 60% transparenz / 40% sichtbar
    "#3c699a4D",  # 70% transparenz / 30% sichtbar
    "#3c699a33",  # 80% transparenz / 20% sichtbar
    "#3c699a1A",  # 90% transparenz / 10% sichtbar
    "#3c699a00",  # 100% transparenz / 0% sichtbar
    ]
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_background():
    if STYLE == "gfs":
        return ["#f4f0e4", "#ece5d2", "#6e685b", "#14130f"]
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")



def give_binaer_verlauf_opposite():
    if STYLE == "gfs":
        return {
    2: ['#1b3f68', '#b24d24'],
    3: ['#1b3f68', '#cfddec', '#b24d24'],
    4: ['#1b3f68', '#6289b2', '#e5dad3', '#b24d24'],
    5: ['#1b3f68', '#2d5f96', '#cfddec', '#f1d9c7', '#b24d24'],
    6: ['#1b3f68', '#29588c', '#8eaac9', '#dcdbdd', '#e4bca6', '#b24d24'],
    7: ['#1b3f68', '#275486', '#6289b2', '#cfddec', '#e5dad3', '#dcaa90', '#b24d24'],
    8: ['#1b3f68', '#255182', '#4471a2', '#a0b9d3', '#d8dbe1', '#ecd9cc', '#d69d81', '#b24d24'],
    9: ['#1b3f68', '#1b3f68', '#255182', '#4471a2', '#a0b9d3', '#d8dbe1', '#ecd9cc', '#d69d81', '#b24d24'],
    }
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_binaer_verlauf():
    if STYLE == "gfs":
        return {
    2: ['#b24d24', '#1b3f68'],
    3: ['#b24d24', '#cfddec', '#1b3f68'],
    4: ['#b24d24', '#e5dad3', '#6289b2', '#1b3f68'],
    5: ['#b24d24', '#f1d9c7', '#cfddec', '#2d5f96', '#1b3f68'],
    6: ['#b24d24', '#e4bca6', '#dcdbdd', '#8eaac9', '#29588c', '#1b3f68'],
    7: ['#b24d24', '#dcaa90', '#e5dad3', '#cfddec', '#6289b2', '#275486', '#1b3f68'],
    8: ['#b24d24', '#d69d81', '#ecd9cc', '#d8dbe1', '#a0b9d3', '#4471a2', '#255182', '#1b3f68'],
    9: ['#b24d24', '#d69d81', '#ecd9cc', '#d8dbe1', '#a0b9d3', '#4471a2', '#255182', '#1b3f68', '#1b3f68'],
    }
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_farben_4():
    if STYLE == "gfs":
        return {"grün": "#4c7a3a", "rot": "#b24d24", "blau": "#3c699a", "gelb": "#c48a2a"}
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_farben_4_abstufungen():
    if STYLE == "gfs":
        return {
    "grün": {
        "sehr_hell":  "#c9d7c4",
        "hell":       "#93af89",
        "basis":      "#4c7a3a",
        "dunkel":     "#355529",
        "sehr_dunkel":"#263d1d",
    },
    "rot": {
        "sehr_hell":  "#e8cabd",
        "hell":       "#d1947c",
        "basis":      "#b24d24",
        "dunkel":     "#7d3619",
        "sehr_dunkel":"#592712",
    },
    "blau": {
        "sehr_hell":  "#c5d2e1",
        "hell":       "#8aa5c2",
        "basis":      "#3c699a",
        "dunkel":     "#2a4a6c",
        "sehr_dunkel":"#1e354d",
    },
    "gelb": {
        "sehr_hell":  "#eddcbf",
        "hell":       "#dcb97f",
        "basis":      "#c48a2a",
        "dunkel":     "#89611d",
        "sehr_dunkel":"#624515",
    },
    }
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

MULTIPLE_COLORS = give_multiple_colors()
CORE_COLOR = give_core_color()
BACKGROUND = give_background()
BINAER_VERLAUF_OPPOSITE = give_binaer_verlauf_opposite()
BINAER_VERLAUF = give_binaer_verlauf()
FARBEN_4 = give_farben_4()
FARBEN_4_ABSTUFUNGEN = give_farben_4_abstufungen()