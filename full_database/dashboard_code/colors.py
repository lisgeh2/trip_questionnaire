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
    if STYLE == "leavy":
        return [
                "#38623f",  # gruen – Waldgruen (Core)
                "#8c3b2e",  # rot – Terrakotta
                "#3f5e78",  # blau – Schiefer
                "#b0862e",  # gelb – Ocker
                "#6b4a2f",  # braun – Rinde
                "#22201b",  # tinte (dunkel)
                "#8ea182",  # gruen-grau – Flechte (grau)
                "#ddd0b4",  # pergament (paper)
                ]
    if STYLE == "comic_brutalist":
        return [
                "#d8382c",  # rot – Druckfarbe Rot
                "#2b7ad4",  # blau – Druckfarbe Blau (Core)
                "#f2c400",  # gelb – Druckfarbe Gelb
                "#1f8a4d",  # gruen – Druckfarbe Gruen
                "#6b3fa0",  # violett – fuenfte Farbe fuer Kategorien
                "#14161a",  # tinte (dunkel)
                "#8b8578",  # presse-grau (grau)
                "#ded8c8",  # papier
                ]
    if STYLE == "black_white":
        return [
                "#770b0b",  # rot – Basis
                "#b04b45",  # rot – mittel
                "#d7a6a1",  # rot – hell
                "#5d0909",  # rot – dunkel (auf Schwarz noch sichtbar)
                "#942724",  # rot – dunkel-mittel
                "#f2f0ec",  # weiss (Titel)
                "#c47670",  # rot – hell-mittel
                "#e8d6d1",  # rot – sehr hell
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
    if STYLE == "leavy":
        return [
    "#38623f",    # 0% transparenz / 100% sichtbar
    "#38623fE6",  # 10% transparenz / 90% sichtbar
    "#38623fCC",  # 20% transparenz / 80% sichtbar
    "#38623fB3",  # 30% transparenz / 70% sichtbar
    "#38623f99",  # 40% transparenz / 60% sichtbar
    "#38623f80",  # 50% transparenz / 50% sichtbar
    "#38623f66",  # 60% transparenz / 40% sichtbar
    "#38623f4D",  # 70% transparenz / 30% sichtbar
    "#38623f33",  # 80% transparenz / 20% sichtbar
    "#38623f1A",  # 90% transparenz / 10% sichtbar
    "#38623f00",  # 100% transparenz / 0% sichtbar
    ]
    if STYLE == "comic_brutalist":
        return [
    "#2b7ad4",    # 0% transparenz / 100% sichtbar
    "#2b7ad4E6",  # 10% transparenz / 90% sichtbar
    "#2b7ad4CC",  # 20% transparenz / 80% sichtbar
    "#2b7ad4B3",  # 30% transparenz / 70% sichtbar
    "#2b7ad499",  # 40% transparenz / 60% sichtbar
    "#2b7ad480",  # 50% transparenz / 50% sichtbar
    "#2b7ad466",  # 60% transparenz / 40% sichtbar
    "#2b7ad44D",  # 70% transparenz / 30% sichtbar
    "#2b7ad433",  # 80% transparenz / 20% sichtbar
    "#2b7ad41A",  # 90% transparenz / 10% sichtbar
    "#2b7ad400",  # 100% transparenz / 0% sichtbar
    ]
    if STYLE == "black_white":
        return [
    "#0d0d0d",    # 0% transparenz / 100% sichtbar
    "#0d0d0dE6",  # 10% transparenz / 90% sichtbar
    "#0d0d0dCC",  # 20% transparenz / 80% sichtbar
    "#0d0d0dB3",  # 30% transparenz / 70% sichtbar
    "#0d0d0d99",  # 40% transparenz / 60% sichtbar
    "#0d0d0d80",  # 50% transparenz / 50% sichtbar
    "#0d0d0d66",  # 60% transparenz / 40% sichtbar
    "#0d0d0d4D",  # 70% transparenz / 30% sichtbar
    "#0d0d0d33",  # 80% transparenz / 20% sichtbar
    "#0d0d0d1A",  # 90% transparenz / 10% sichtbar
    "#0d0d0d00",  # 100% transparenz / 0% sichtbar
    ]
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_background():
    if STYLE == "gfs":
        return ["#f4f0e4", "#ece5d2", "#6e685b", "#14130f"]
    if STYLE == "cool_black":
        # [0] Karten-Fläche, [1] Seiten-Hintergrund, [2] Linien/Trenner, [3] Text hell
        return ["#0b0d14", "#05060a", "#171b2b", "#eaf0ff"]
    if STYLE == "leavy":
        # [0] Karte, [1] Seiten-Hintergrund, [2] Linien, [3] Tinte
        return ["#fdfaf3", "#f2ebda", "#c4cab0", "#22201b"]
    if STYLE == "comic_brutalist":
        # [0] Karte, [1] Seiten-Hintergrund, [2] Rahmen/Tinte, [3] Tinte
        return ["#f4f1e8", "#ece8dc", "#14161a", "#14161a"]
    if STYLE == "black_white":
        # Nachtmodus. [0] Flaeche, [1] Seiten-Hintergrund, [2] Linien, [3] Schrift
        return ["#111111", "#0a0a0a", "#f2f0ec", "#f2f0ec"]
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
    if STYLE == "leavy":
        return {
    2: ['#3f5e78', '#8c3b2e'],
    3: ['#3f5e78', '#e8dfc8', '#8c3b2e'],
    4: ['#3f5e78', '#b0b4ad', '#c9a895', '#8c3b2e'],
    5: ['#3f5e78', '#949ea0', '#e8dfc8', '#ba8d7b', '#8c3b2e'],
    6: ['#3f5e78', '#839298', '#c6c5b8', '#d6bea9', '#b17d6c', '#8c3b2e'],
    7: ['#3f5e78', '#778993', '#b0b4ad', '#e8dfc8', '#c9a895', '#ab7261', '#8c3b2e'],
    8: ['#3f5e78', '#6f838f', '#a0a8a6', '#d0cdbd', '#dbc8b2', '#c19986', '#a66a5a', '#8c3b2e'],
    9: ['#3f5e78', '#697e8c', '#949ea0', '#bebfb4', '#e8dfc8', '#d1b6a2', '#ba8d7b', '#a36454', '#8c3b2e'],
    }
    if STYLE == "comic_brutalist":
        return {
    2: ['#2b7ad4', '#d8382c'],
    3: ['#2b7ad4', '#ded8c8', '#d8382c'],
    4: ['#2b7ad4', '#a2b9cc', '#dca394', '#d8382c'],
    5: ['#2b7ad4', '#84a9ce', '#ded8c8', '#db887a', '#d8382c'],
    6: ['#2b7ad4', '#73a0cf', '#bac5ca', '#ddb8a9', '#da786a', '#d8382c'],
    7: ['#2b7ad4', '#6799d0', '#a2b9cc', '#ded8c8', '#dca394', '#da6d60', '#d8382c'],
    8: ['#2b7ad4', '#5e95d1', '#91b0cd', '#c4cbca', '#ddc1b2', '#db9385', '#da6659', '#d8382c'],
    9: ['#2b7ad4', '#5892d1', '#84a9ce', '#b1c0cb', '#ded8c8', '#dcb0a1', '#db887a', '#da6053', '#d8382c'],
    }
    if STYLE == "black_white":
        # Monochrom: die Opposition ist hell gegen dunkel, nicht Farbe gegen Farbe.
        return {
    2: ['#f0ebe7', '#570909'],
    3: ['#f0ebe7', '#ad453f', '#570909'],
    4: ['#f0ebe7', '#c47670', '#922522', '#570909'],
    5: ['#f0ebe7', '#cf908a', '#ad453f', '#841716', '#570909'],
    6: ['#f0ebe7', '#d6a29d', '#bb625c', '#9d302b', '#7b0f0f', '#570909'],
    7: ['#f0ebe7', '#daaea9', '#c47670', '#ad453f', '#922522', '#760b0b', '#570909'],
    8: ['#f0ebe7', '#ddb7b2', '#cb847e', '#b75a54', '#a2342f', '#8a1d1b', '#710b0b', '#570909'],
    9: ['#f0ebe7', '#e0bdb9', '#cf908a', '#be6a64', '#ad453f', '#992c27', '#841716', '#6e0a0a', '#570909'],
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
    if STYLE == "leavy":
        return {
    2: ['#8c3b2e', '#3f5e78'],
    3: ['#8c3b2e', '#e8dfc8', '#3f5e78'],
    4: ['#8c3b2e', '#c9a895', '#b0b4ad', '#3f5e78'],
    5: ['#8c3b2e', '#ba8d7b', '#e8dfc8', '#949ea0', '#3f5e78'],
    6: ['#8c3b2e', '#b17d6c', '#d6bea9', '#c6c5b8', '#839298', '#3f5e78'],
    7: ['#8c3b2e', '#ab7261', '#c9a895', '#e8dfc8', '#b0b4ad', '#778993', '#3f5e78'],
    8: ['#8c3b2e', '#a66a5a', '#c19986', '#dbc8b2', '#d0cdbd', '#a0a8a6', '#6f838f', '#3f5e78'],
    9: ['#8c3b2e', '#a36454', '#ba8d7b', '#d1b6a2', '#e8dfc8', '#bebfb4', '#949ea0', '#697e8c', '#3f5e78'],
    }
    if STYLE == "comic_brutalist":
        return {
    2: ['#d8382c', '#2b7ad4'],
    3: ['#d8382c', '#ded8c8', '#2b7ad4'],
    4: ['#d8382c', '#dca394', '#a2b9cc', '#2b7ad4'],
    5: ['#d8382c', '#db887a', '#ded8c8', '#84a9ce', '#2b7ad4'],
    6: ['#d8382c', '#da786a', '#ddb8a9', '#bac5ca', '#73a0cf', '#2b7ad4'],
    7: ['#d8382c', '#da6d60', '#dca394', '#ded8c8', '#a2b9cc', '#6799d0', '#2b7ad4'],
    8: ['#d8382c', '#da6659', '#db9385', '#ddc1b2', '#c4cbca', '#91b0cd', '#5e95d1', '#2b7ad4'],
    9: ['#d8382c', '#da6053', '#db887a', '#dcb0a1', '#ded8c8', '#b1c0cb', '#84a9ce', '#5892d1', '#2b7ad4'],
    }
    if STYLE == "black_white":
        # Eine Farbe, ueber die Helligkeit durchgezogen: von dunkelrot ueber
        # #770B0B bis fast weiss. Der dunkle Pol bleibt hell genug, um auf
        # schwarzem Grund noch sichtbar zu sein.
        return {
    2: ['#570909', '#f0ebe7'],
    3: ['#570909', '#ad453f', '#f0ebe7'],
    4: ['#570909', '#922522', '#c47670', '#f0ebe7'],
    5: ['#570909', '#841716', '#ad453f', '#cf908a', '#f0ebe7'],
    6: ['#570909', '#7b0f0f', '#9d302b', '#bb625c', '#d6a29d', '#f0ebe7'],
    7: ['#570909', '#760b0b', '#922522', '#ad453f', '#c47670', '#daaea9', '#f0ebe7'],
    8: ['#570909', '#710b0b', '#8a1d1b', '#a2342f', '#b75a54', '#cb847e', '#ddb7b2', '#f0ebe7'],
    9: ['#570909', '#6e0a0a', '#841716', '#992c27', '#ad453f', '#be6a64', '#cf908a', '#e0bdb9', '#f0ebe7'],
    }
    raise ValueError(f"Unbekannter STYLE: {STYLE!r}")

def give_farben_4():
    if STYLE == "gfs":
        return {"grün": "#4c7a3a", "rot": "#b24d24", "blau": "#3c699a", "gelb": "#c48a2a"}
    if STYLE == "cool_black":
        return {"grün": "#3dff8b", "rot": "#ff2d95", "blau": "#00d9ff", "gelb": "#ffd60a"}
    if STYLE == "leavy":
        return {"grün": "#38623f", "rot": "#8c3b2e", "blau": "#3f5e78", "gelb": "#b0862e"}
    if STYLE == "comic_brutalist":
        return {"grün": "#1f8a4d", "rot": "#d8382c", "blau": "#2b7ad4", "gelb": "#f2c400"}
    if STYLE == "black_white":
        # Die vier Namen bleiben, die Unterscheidung laeuft ueber den Tonwert
        return {"grün": "#8f8f8f", "rot": "#f2f0ec", "blau": "#c2c2c2", "gelb": "#6b6b6b"}
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
    if STYLE == "leavy":
        return {
    "grün": {
        "sehr_hell":  "#d3d8c9",
        "hell":       "#99ac96",
        "basis":      "#38623f",
        "dunkel":     "#304b32",
        "sehr_dunkel":"#293527",
    },
    "rot": {
        "sehr_hell":  "#e4d1c6",
        "hell":       "#c3988d",
        "basis":      "#8c3b2e",
        "dunkel":     "#673227",
        "sehr_dunkel":"#442921",
    },
    "blau": {
        "sehr_hell":  "#d5d8d5",
        "hell":       "#9caab2",
        "basis":      "#3f5e78",
        "dunkel":     "#354857",
        "sehr_dunkel":"#2b3439",
    },
    "gelb": {
        "sehr_hell":  "#ebe0c6",
        "hell":       "#d5be8d",
        "basis":      "#b0862e",
        "dunkel":     "#7e6227",
        "sehr_dunkel":"#4f4121",
    },
    }
    if STYLE == "comic_brutalist":
        return {
    "grün": {
        "sehr_hell":  "#c5dac6",
        "hell":       "#81b994",
        "basis":      "#1f8a4d",
        "dunkel":     "#1b653d",
        "sehr_dunkel":"#18402c",
    },
    "rot": {
        "sehr_hell":  "#eec8bf",
        "hell":       "#e58d82",
        "basis":      "#d8382c",
        "dunkel":     "#992d26",
        "sehr_dunkel":"#5b2220",
    },
    "blau": {
        "sehr_hell":  "#c8d7e4",
        "hell":       "#87b1dd",
        "basis":      "#2b7ad4",
        "dunkel":     "#245a98",
        "sehr_dunkel":"#1c3a5d",
    },
    "gelb": {
        "sehr_hell":  "#f4e7b5",
        "hell":       "#f3d96b",
        "basis":      "#f2c400",
        "dunkel":     "#ab8c08",
        "sehr_dunkel":"#645511",
    },
    }
    if STYLE == "black_white":
        return {
    "grün": {
        "sehr_hell":  "#2b2b2b",
        "hell":       "#4f4f4f",
        "basis":      "#8f8f8f",
        "dunkel":     "#bcbcbc",
        "sehr_dunkel":"#e4e2de",
    },
    "rot": {
        "sehr_hell":  "#3a3a39",
        "hell":       "#77716c",
        "basis":      "#f2f0ec",
        "dunkel":     "#f5f4f1",
        "sehr_dunkel":"#faf9f7",
    },
    "blau": {
        "sehr_hell":  "#333333",
        "hell":       "#6b6b6b",
        "basis":      "#c2c2c2",
        "dunkel":     "#d7d7d7",
        "sehr_dunkel":"#ececec",
    },
    "gelb": {
        "sehr_hell":  "#242424",
        "hell":       "#3d3d3d",
        "basis":      "#6b6b6b",
        "dunkel":     "#999999",
        "sehr_dunkel":"#c9c9c9",
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