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
    if STYLE == "cool_black":
        return [
                "#ff2d95",  # rot – hot neon pink (Core)
                "#00d9ff",  # blau – electric cyan
                "#3dff8b",  # gruen – acid mint
                "#ffd60a",  # gelb – voltage
                "#b14bff",  # purple – ultraviolet
                "#eaf0ff",  # ice (statt dunkel: auf Schwarz ist Hell der Kontrast)
                "#7c88a8",  # grau – cool grey
                "#ff6b1a",  # orange (statt paper)
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
    if STYLE == "cool_black":
        return [
    "#ff2d95",    # 0% transparenz / 100% sichtbar
    "#ff2d95E6",  # 10% transparenz / 90% sichtbar
    "#ff2d95CC",  # 20% transparenz / 80% sichtbar
    "#ff2d95B3",  # 30% transparenz / 70% sichtbar
    "#ff2d9599",  # 40% transparenz / 60% sichtbar
    "#ff2d9580",  # 50% transparenz / 50% sichtbar
    "#ff2d9566",  # 60% transparenz / 40% sichtbar
    "#ff2d954D",  # 70% transparenz / 30% sichtbar
    "#ff2d9533",  # 80% transparenz / 20% sichtbar
    "#ff2d951A",  # 90% transparenz / 10% sichtbar
    "#ff2d9500",  # 100% transparenz / 0% sichtbar
    ]
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_background():
    if STYLE == "gfs":
        return ["#f4f0e4", "#ece5d2", "#6e685b", "#14130f"]
    if STYLE == "cool_black":
        # [0] Karten-Fläche, [1] Seiten-Hintergrund, [2] Linien/Trenner, [3] Text hell
        return ["#0b0d14", "#141725", "#171b2b", "#eaf0ff"]
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
    if STYLE == "cool_black":
        # Divergierend durch die Dunkelheit statt durch Weiss
        return {
    2: ['#00d9ff', '#ff2d95'],
    3: ['#00d9ff', '#2a2f45', '#ff2d95'],
    4: ['#00d9ff', '#1c6883', '#712e60', '#ff2d95'],
    5: ['#00d9ff', '#1584a2', '#2a2f45', '#942e6d', '#ff2d95'],
    6: ['#00d9ff', '#1195b5', '#22516a', '#552f55', '#aa2e75', '#ff2d95'],
    7: ['#00d9ff', '#0ea0c1', '#1c6883', '#2a2f45', '#712e60', '#b82e7a', '#ff2d95'],
    8: ['#00d9ff', '#0ca8ca', '#187895', '#244760', '#482f50', '#852e67', '#c22e7e', '#ff2d95'],
    9: ['#00d9ff', '#0aaed0', '#1584a2', '#205a74', '#2a2f45', '#5f2e59', '#942e6d', '#ca2e81', '#ff2d95'],
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
    if STYLE == "cool_black":
        # Divergierend durch die Dunkelheit statt durch Weiss
        return {
    2: ['#ff2d95', '#00d9ff'],
    3: ['#ff2d95', '#2a2f45', '#00d9ff'],
    4: ['#ff2d95', '#712e60', '#1c6883', '#00d9ff'],
    5: ['#ff2d95', '#942e6d', '#2a2f45', '#1584a2', '#00d9ff'],
    6: ['#ff2d95', '#aa2e75', '#552f55', '#22516a', '#1195b5', '#00d9ff'],
    7: ['#ff2d95', '#b82e7a', '#712e60', '#2a2f45', '#1c6883', '#0ea0c1', '#00d9ff'],
    8: ['#ff2d95', '#c22e7e', '#852e67', '#482f50', '#244760', '#187895', '#0ca8ca', '#00d9ff'],
    9: ['#ff2d95', '#ca2e81', '#942e6d', '#5f2e59', '#2a2f45', '#205a74', '#1584a2', '#0aaed0', '#00d9ff'],
    }
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_farben_4():
    if STYLE == "gfs":
        return {"grün": "#4c7a3a", "rot": "#b24d24", "blau": "#3c699a", "gelb": "#c48a2a"}
    if STYLE == "cool_black":
        return {"grün": "#3dff8b", "rot": "#ff2d95", "blau": "#00d9ff", "gelb": "#ffd60a"}
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
    if STYLE == "cool_black":
        # Achtung: auf schwarzem Grund laeuft die Skala andersrum.
        # Die Stufen behalten ihre ROLLE (sehr_hell = wenig Kontrast / Flaeche,
        # sehr_dunkel = viel Kontrast / Linie & Text), nur wird "dunkel" hier
        # heller statt dunkler - sonst verschwindet alles im Hintergrund.
        return {
    "grün": {
        "sehr_hell":  "#103824",
        "hell":       "#1e7644",
        "basis":      "#3dff8b",
        "dunkel":     "#7bffb0",
        "sehr_dunkel":"#bdffd8",
    },
    "rot": {
        "sehr_hell":  "#370e26",
        "hell":       "#761849",
        "basis":      "#ff2d95",
        "dunkel":     "#ff70b7",
        "sehr_dunkel":"#ffb8db",
    },
    "blau": {
        "sehr_hell":  "#04303b",
        "hell":       "#036578",
        "basis":      "#00d9ff",
        "dunkel":     "#52e5ff",
        "sehr_dunkel":"#a8f2ff",
    },
    "gelb": {
        "sehr_hell":  "#37300a",
        "hell":       "#76640a",
        "basis":      "#ffd60a",
        "dunkel":     "#ffe358",
        "sehr_dunkel":"#fff1ac",
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