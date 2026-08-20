from colors import FARBEN_4_ABSTUFUNGEN
from config import STYLE

def give_global_css():
    if STYLE == "gfs":
        return """
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,900&family=DM+Sans:wght@400;500;600&display=swap');
  html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    header[data-testid="stHeader"] {
        display: none;
    }
  .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
  h3 { font-size: 1rem !important; font-weight: 600 !important; }
  .kpi-box {
    background: white; border: 1px solid #e2ddd4;
    padding: 18px 20px; border-radius: 2px; margin-bottom: 4px;
  }
  .kpi-label { font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: #7a7269; margin-bottom: 6px; }
  .kpi-value { font-size: 2rem; font-weight: 700; color: #1a1a2e; line-height: 1; margin-bottom: 5px; }
  .kpi-up   { color: #4c7a3a; font-size: 0.76rem; font-weight: 500; }
  .kpi-neutral   { color: #7a7269; font-size: 0.76rem; font-weight: 500; }
  .kpi-down { color: #b24d24; font-size: 0.76rem; font-weight: 500; }
  .section-title {
    font-size: 0.68rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; color: #7a7269;
    border-bottom: 1px solid #e2ddd4; padding-bottom: 6px; margin: 8px 0 4px;
  }
  .sample-size {
      font-size: 0.68rem;
      font-weight: 600;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #7a7269;
      margin-top: 12px;
      display: flex;
      justify-content: flex-end;
  }

:root {
    --bg: #f5ebe0;
    --card: #ffffff;
    --border: #e8dfd2;
    --text: #1a1d24;
    --muted: #6b7280;
    --accent-red: #b24d24;
    --accent-yellow: #c48a2a;
    --accent-blue: "#3c699a";
    --accent-green: #4c7a3a;
}

[class*="st-key-karte"] {
    background-color: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

/* Footer */
footer{padding:40px 0;border-top:1px solid rgba(148,163,184,.12);color:var(--muted)}

.footer-logos {
display: flex;
justify-content: center;
align-items: center;
gap: 2.5rem;
flex-wrap: wrap;
margin-bottom: 0.5rem;
}

.footer-logos img {
height: 70px;
max-width: 140px;
object-fit: contain;
opacity: 0.9;
filter: grayscale(40%);
transition: filter 0.3s ease, transform 0.3s ease, opacity 0.3s ease;
}

.footer-logos img:hover {
opacity: 1;
filter: grayscale(0%);
transform: scale(1.05);
}

.footer-bottom {
display: flex;
justify-content: space-between;
gap: 1rem;
flex-wrap: wrap;
width: 100%;
}




.stat-label {
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--muted);
    margin: 0 0 0.9rem 0;
}

.stat-number {
    font-family: "Fraunces", serif;
    font-variation-settings: "opsz" 144;
    font-weight: 700;
    font-size: 5.5rem;
    line-height: 0.9;
    letter-spacing: -0.02em;
    margin: 0;
    color: var(--text);
}

.stat-number .percent {
    font-size: 3rem;
    font-weight: 600;
    color: var(--accent-yellow);
    vertical-align: top;
    margin-left: 0.1em;
}

.stat-description {
    margin: 0.4rem 0 0 0;
    font-size: 0.92rem;
    line-height: 1.4;
    opacity: 0.85;
}
</style>
"""
    if STYLE == "cool_black":
        return """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100,400;100,500;100,600;112,700;112,800&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg: #05060a;
    --surface: rgba(234, 240, 255, 0.035);
    --border: rgba(234, 240, 255, 0.10);
    --text: #eaf0ff;
    --muted: rgba(234, 240, 255, 0.45);
    --accent-red: #ff2d95;
    --accent-yellow: #ffd60a;
    --accent-blue: #00d9ff;
    --accent-green: #3dff8b;
}

  html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
  header[data-testid="stHeader"] { display: none; }

  .stApp { background-color: var(--bg); color: var(--text); }
  .stApp, .stApp p, .stApp li, .stApp label,
  [data-testid="stMarkdownContainer"] { color: var(--text); }

  .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

  h1, h2, h3, h4 {
    font-family: 'Archivo', sans-serif !important;
    color: var(--text) !important;
    letter-spacing: -0.02em;
  }
  h3 { font-size: 1rem !important; font-weight: 600 !important; }

  /* Keine weissen Karten mehr - Glas statt Papier */
  .kpi-box {
    background: var(--surface);
    border: 1px solid var(--border);
    backdrop-filter: blur(14px);
    padding: 18px 20px; border-radius: 2px; margin-bottom: 4px;
  }
  .kpi-label {
    font-size: 0.64rem; letter-spacing: 0.22em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 8px; font-weight: 600;
  }
  .kpi-value {
    font-family: 'Archivo', sans-serif;
    font-size: 2.2rem; font-weight: 800; color: var(--text);
    line-height: 1; margin-bottom: 5px; letter-spacing: -0.03em;
  }
  .kpi-up      { color: var(--accent-green); font-size: 0.76rem; font-weight: 600; }
  .kpi-neutral { color: var(--muted);        font-size: 0.76rem; font-weight: 600; }
  .kpi-down    { color: var(--accent-red);   font-size: 0.76rem; font-weight: 600; }

  .section-title {
    font-size: 0.64rem; font-weight: 700; letter-spacing: 0.24em;
    text-transform: uppercase; color: var(--muted);
    border-bottom: 1px solid var(--border); padding-bottom: 8px; margin: 8px 0 4px;
  }
  .sample-size {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.62rem;
      font-weight: 400;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 12px;
      display: flex;
      justify-content: flex-end;
  }

[class*="st-key-karte"] {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 2px;
    padding: 1.5rem;
    backdrop-filter: blur(14px);
    box-shadow: none;
    transition: border-color 0.25s ease;
}
[class*="st-key-karte"]:hover {
    border-color: rgba(255, 45, 149, 0.40);
}

/* Streamlit-Widgets ins Dunkle ziehen */
[data-baseweb="select"] > div, .stTextInput input, .stNumberInput input {
    background: var(--surface) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
}
[data-testid="stMetricValue"] { color: var(--text); }
hr, [data-testid="stDivider"] { border-color: var(--border); }

/* Footer */
footer{padding:40px 0;border-top:1px solid var(--border);color:var(--muted)}

.footer-logos {
display: flex;
justify-content: center;
align-items: center;
gap: 2.5rem;
flex-wrap: wrap;
margin-bottom: 0.5rem;
}

.footer-logos img {
height: 70px;
max-width: 140px;
object-fit: contain;
opacity: 0.4;
filter: brightness(0) invert(1);
transition: filter 0.3s ease, transform 0.3s ease, opacity 0.3s ease;
}

.footer-logos img:hover {
opacity: 0.95;
transform: scale(1.05);
}

.footer-bottom {
display: flex;
justify-content: space-between;
gap: 1rem;
flex-wrap: wrap;
width: 100%;
}

.stat-label {
    font-size: 0.64rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.22em;
    color: var(--muted);
    margin: 0 0 0.9rem 0;
}

.stat-number {
    font-family: 'Archivo', sans-serif;
    font-variation-settings: "wdth" 112;
    font-weight: 800;
    font-size: 6rem;
    line-height: 0.85;
    letter-spacing: -0.045em;
    margin: 0;
    color: var(--text);
}

.stat-number .percent {
    font-size: 2.6rem;
    font-weight: 500;
    color: var(--accent-red);
    vertical-align: top;
    margin-left: 0.08em;
    letter-spacing: 0;
}

.stat-description {
    margin: 0.7rem 0 0 0;
    font-size: 0.92rem;
    line-height: 1.45;
    opacity: 0.85;
}
</style>
"""
    if STYLE == "leavy":
        return """
<style>
  @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Playfair+Display:ital,wght@0,600;0,700;0,900;1,600&display=swap');

:root {
    --bg: #f2ebda;
    --card: #fdfaf3;
    --border: #d8cdb4;
    --rule: #38623f;
    --text: #22201b;
    --muted: #6f6552;
    --accent-red: #8c3b2e;
    --accent-yellow: #b0862e;
    --accent-blue: #3f5e78;
    --accent-green: #38623f;
}

  html, body, [class*="css"] { font-family: 'EB Garamond', Georgia, serif; }
  header[data-testid="stHeader"] { display: none; }

  .stApp { background-color: var(--bg); color: var(--text); }
  .stApp, .stApp p, .stApp li, .stApp label,
  [data-testid="stMarkdownContainer"] { color: var(--text); }

  .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }

  h1, h2, h3, h4 {
    font-family: 'Playfair Display', Georgia, serif !important;
    color: var(--text) !important;
    letter-spacing: -0.01em;
    font-weight: 600 !important;
  }
  h3 { font-size: 1.06rem !important; }

  /* KpiRenderer setzt inline border-top:3px solid {akzent}.
     Darum hier NUR eine Haarlinie und kein Doppelrahmen - sonst
     kollidieren die beiden Rahmen wie zwei uebereinandergelegte Passepartouts. */
  .kpi-box {
    background: var(--card);
    border: 1px solid var(--border);
    box-shadow: none;
    padding: 22px 24px 20px 24px;
    border-radius: 0; margin-bottom: 4px;
  }
  /* Die Akzentfarbe kommt inline aus dem KpiRenderer (border-top:3px).
     Nur die Breite wird hier ueberschrieben - die Farbe bleibt inline.
     !important ist noetig, weil Inline-Styles sonst gewinnen. */
  .kpi-box[style*="border-top"] {
    border-top-width: 7px !important;
  }
  .kpi-label {
    font-size: 0.66rem; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--muted); font-weight: 600;
    padding-bottom: 11px; margin-bottom: 13px;
    border-bottom: 1px solid var(--border);
  }
  .kpi-value {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.35rem; font-weight: 600; color: var(--text);
    line-height: 1.06; margin-bottom: 11px; letter-spacing: -0.012em;
  }
  .kpi-up      { color: var(--accent-green);  font-size: 0.88rem; font-style: italic; }
  .kpi-neutral { color: var(--muted);         font-size: 0.88rem; font-style: italic; }
  .kpi-down    { color: var(--accent-red);    font-size: 0.88rem; font-style: italic; }

  .section-title {
    font-size: 0.68rem; font-weight: 600; letter-spacing: 0.26em;
    text-transform: uppercase; color: var(--muted);
    border-bottom: 1px solid var(--border); padding-bottom: 7px; margin: 8px 0 4px;
  }
  .sample-size {
      font-size: 0.80rem;
      font-style: italic;
      letter-spacing: 0.02em;
      text-transform: none;
      color: var(--muted);
      margin-top: 12px;
      display: flex;
      justify-content: flex-end;
  }

[class*="st-key-karte"] {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 0;
    padding: 1.6rem;
    /* Drei Lagen, damit box-shadow beim Hover sauber interpolieren kann:
       die Innenlinie liegt hier als unsichtbarer Platzhalter bereit. */
    box-shadow: inset 0 0 0 1px var(--card),
                inset 0 0 0 0 rgba(56, 98, 63, 0),
                0 2px 5px rgba(34, 32, 27, 0.10);
    transition: transform 220ms cubic-bezier(0.2, 0.7, 0.3, 1),
                box-shadow 220ms cubic-bezier(0.2, 0.7, 0.3, 1),
                border-color 220ms ease;
}
[class*="st-key-karte"]:hover {
    border-color: var(--rule);
    transform: translateY(-4px);
    /* Der zweite Rahmen faehrt aus: aus der Karte wird eine Urkunde. */
    box-shadow: inset 0 0 0 1px var(--card),
                inset 0 0 0 4px var(--rule),
                0 18px 34px -12px rgba(34, 32, 27, 0.42),
                0 4px 10px rgba(34, 32, 27, 0.16);
}
@media (prefers-reduced-motion: reduce) {
    [class*="st-key-karte"] { transition: none; }
    [class*="st-key-karte"]:hover { transform: none; }
}

[data-baseweb="select"] > div, .stTextInput input, .stNumberInput input {
    background: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 0 !important;
    color: var(--text) !important;
    font-family: 'EB Garamond', Georgia, serif !important;
}
[data-testid="stMetricValue"] { color: var(--text); }
hr, [data-testid="stDivider"] { border-color: var(--border); }

/* Footer */
footer{padding:40px 0;border-top:1px solid var(--rule);color:var(--muted)}

.footer-logos {
display: flex;
justify-content: center;
align-items: center;
gap: 2.5rem;
flex-wrap: wrap;
margin-bottom: 0.5rem;
}

.footer-logos img {
height: 70px;
max-width: 140px;
object-fit: contain;
opacity: 0.75;
filter: grayscale(60%) sepia(18%);
transition: filter 0.3s ease, transform 0.3s ease, opacity 0.3s ease;
}

.footer-logos img:hover {
opacity: 1;
filter: grayscale(0%);
transform: scale(1.05);
}

.footer-bottom {
display: flex;
justify-content: space-between;
gap: 1rem;
flex-wrap: wrap;
width: 100%;
}

.stat-label {
    font-size: 0.70rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.20em;
    color: var(--muted);
    margin: 0 0 0.9rem 0;
}

.stat-number {
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 700;
    font-size: 4.4rem;
    line-height: 1.02;
    letter-spacing: -0.012em;
    margin: 0;
    color: var(--rule);
}

.stat-number .percent {
    font-size: 1.85rem;
    font-weight: 500;
    font-style: italic;
    color: var(--accent-yellow);
    vertical-align: top;
    margin-left: 0.08em;
}

.stat-description {
    margin: 0.85rem 0 0 0;
    font-size: 1.06rem;
    font-style: italic;
    line-height: 1.5;
    opacity: 0.9;
}
</style>
"""
    if STYLE == "comic_brutalist":
        return """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --bg: #ece8dc;
    --card: #f4f1e8;
    --ink: #14161a;
    --border: #14161a;
    --text: #14161a;
    --muted: #6f6a60;
    --accent-red: #d8382c;
    --accent-yellow: #f2c400;
    --accent-blue: #2b7ad4;
    --accent-green: #1f8a4d;
}

  html, body, [class*="css"] { font-family: 'Archivo', Helvetica, sans-serif; }
  header[data-testid="stHeader"] { display: none; }

  /* Papierkorn: feines Rauschen ueber der ganzen Flaeche */
  .stApp {
    background-color: var(--bg);
    color: var(--text);
    background-image:
      radial-gradient(var(--ink) 0.6px, transparent 0.7px),
      radial-gradient(var(--ink) 0.6px, transparent 0.7px);
    background-size: 7px 7px, 7px 7px;
    background-position: 0 0, 3.5px 3.5px;
    background-blend-mode: multiply;
  }
  .stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: var(--bg);
    opacity: 0.955;
    pointer-events: none;
    z-index: 0;
  }
  .block-container { position: relative; z-index: 1; padding-top: 1.5rem; padding-bottom: 2rem; }

  .stApp, .stApp p, .stApp li, .stApp label,
  [data-testid="stMarkdownContainer"] { color: var(--text); }

  h1, h2, h3, h4 {
    font-family: 'Anton', Impact, sans-serif !important;
    font-weight: 400 !important;
    color: var(--text) !important;
    text-transform: uppercase;
    letter-spacing: -0.005em;
  }
  h3 { font-size: 1.5rem !important; line-height: 1.05; }

  /* KPI: harter Kasten, versetzter Schlagschatten statt Weichzeichner.
     Die farbige Oberkante kommt inline aus dem KpiRenderer. */
  .kpi-box {
    background: var(--card);
    border: 4px solid var(--ink);
    box-shadow: 7px 7px 0 0 var(--ink);
    padding: 0 0 16px 0;
    border-radius: 0;
    margin-bottom: 10px;
  }
  .kpi-box[style*="border-top"] {
    border-top-width: 14px !important;
  }
  .kpi-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem; letter-spacing: 0.16em; text-transform: uppercase;
    color: var(--card); background: var(--ink); font-weight: 700;
    padding: 7px 14px; margin: 0 0 14px 0;
  }
  .kpi-value {
    font-family: 'Anton', Impact, sans-serif;
    font-size: 3.1rem; font-weight: 400; color: var(--ink);
    line-height: 0.9; margin: 0 14px 12px 14px; letter-spacing: -0.01em;
    text-transform: uppercase;
  }
  .kpi-up      { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: var(--accent-green); margin: 0 14px; font-weight: 700; }
  .kpi-neutral { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: var(--muted);        margin: 0 14px; font-weight: 700; }
  .kpi-down    { font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: var(--accent-red);   margin: 0 14px; font-weight: 700; }

  /* Abschnittstitel: schwarzer Streifen, kein Unterstrich */
  .section-title {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem; font-weight: 700; letter-spacing: 0.16em;
    text-transform: uppercase; color: var(--card);
    background: var(--ink);
    border-bottom: none;
    padding: 7px 14px; margin: 10px 0 8px;
  }
  .sample-size {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.62rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 14px;
      display: flex;
      justify-content: flex-end;
  }

[class*="st-key-karte"] {
    background: var(--card);
    border: 4px solid var(--ink);
    border-radius: 0;
    padding: 1.4rem;
    box-shadow: 7px 7px 0 0 var(--ink);
}
[class*="st-key-karte"]:hover {
    box-shadow: 7px 7px 0 0 var(--accent-blue), 7px 7px 0 4px var(--ink);
}

[data-baseweb="select"] > div, .stTextInput input, .stNumberInput input {
    background: var(--card) !important;
    border: 3px solid var(--ink) !important;
    border-radius: 0 !important;
    color: var(--text) !important;
    font-family: 'JetBrains Mono', monospace !important;
}
[data-testid="stMetricValue"] { color: var(--text); }
hr, [data-testid="stDivider"] { border-color: var(--ink); border-width: 3px; }

/* Footer */
footer{padding:40px 0;border-top:5px solid var(--ink);color:var(--muted)}

.footer-logos {
display: flex;
justify-content: center;
align-items: center;
gap: 2.5rem;
flex-wrap: wrap;
margin-bottom: 0.5rem;
}

.footer-logos img {
height: 70px;
max-width: 140px;
object-fit: contain;
opacity: 0.9;
filter: grayscale(100%) contrast(180%);
transition: filter 0.2s ease, transform 0.2s ease, opacity 0.2s ease;
}

.footer-logos img:hover {
opacity: 1;
filter: grayscale(0%);
transform: translate(-2px, -2px);
}

.footer-bottom {
display: flex;
justify-content: space-between;
gap: 1rem;
flex-wrap: wrap;
width: 100%;
font-family: 'JetBrains Mono', monospace;
font-size: 0.68rem;
}

.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.60rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--ink);
    margin: 0 0 0.9rem 0;
}

.stat-number {
    font-family: 'Anton', Impact, sans-serif;
    font-weight: 400;
    font-size: 6.4rem;
    line-height: 0.82;
    letter-spacing: -0.02em;
    margin: 0;
    color: var(--ink);
    text-transform: uppercase;
}

.stat-number .percent {
    font-size: 2.8rem;
    font-weight: 400;
    color: var(--accent-red);
    vertical-align: top;
    margin-left: 0.04em;
}

.stat-description {
    margin: 0.9rem 0 0 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    line-height: 1.5;
    opacity: 0.78;
}
</style>
"""
    if STYLE == "black_white":
        return """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600&family=Inter:wght@300;400;500&display=swap');

:root {
    --bg: #0a0a0a;
    --papier: #111111;
    --ink: #f2f0ec;
    --text: #f2f0ec;
    --muted: #8b8985;
    --border: #f2f0ec;
    --accent-red: #1a1a1a;
    --accent-blue: #4f4f4f;
    --accent-green: #828282;
    --accent-yellow: #b3b3b3;
}

  html, body, [class*="css"] { font-family: 'Inter', Helvetica, sans-serif; }
  header[data-testid="stHeader"] { display: none; }

  /* Papierkorn: feines Rauschen, damit das Weiss nicht steril wirkt */
  .stApp {
    background-color: var(--bg);
    color: var(--text);
    background-image:
      radial-gradient(#ffffff 0.5px, transparent 0.6px),
      radial-gradient(#ffffff 0.5px, transparent 0.6px);
    background-size: 6px 6px, 6px 6px;
    background-position: 0 0, 3px 3px;
  }
  .stApp::before {
    content: "";
    position: fixed; inset: 0;
    background: var(--bg);
    opacity: 0.92;
    pointer-events: none;
    z-index: 0;
  }
  .block-container { position: relative; z-index: 1; padding-top: 1.5rem; padding-bottom: 2rem; }
  .stApp, .stApp p, .stApp li, .stApp label,
  [data-testid="stMarkdownContainer"] { color: var(--text); }
  ::selection { background: var(--ink); color: #0a0a0a; }

  h1, h2, h3, h4 {
    font-family: 'Archivo Black', Helvetica, sans-serif !important;
    font-weight: 400 !important;
    color: var(--text) !important;
    text-transform: uppercase;
    letter-spacing: -0.03em;
  }
  h3 { font-size: 1.7rem !important; line-height: 0.95; }

  /* KPI: die Zahl sprengt den Kasten, das Label ist winzig und klebt an der Kante.
     Die farbige Oberkante kommt inline vom KpiRenderer und wird hier zum Balken. */
  .kpi-box {
    background: var(--papier);
    border: none;
    box-shadow: none;
    padding: 0 0 14px 0;
    border-radius: 0;
    margin-bottom: 8px;
    position: relative;
  }
  .kpi-box[style*="border-top"] {
    border-top-width: 16px !important;
  }
  .kpi-label {
    font-family: 'Inter', Helvetica, sans-serif;
    font-size: 0.56rem; letter-spacing: 0.24em; text-transform: uppercase;
    color: var(--ink); background: none; font-weight: 500;   /* vorher: color: #0a0a0a; background: var(--ink); */
    padding: 16px 12px 0 12px; margin: 0 0 10px 0;           /* vorher: padding: 6px 12px */
    display: block;                                          /* vorher: inline-block */
  }
  /* Gross und gestreckt, aber der Wert bricht um statt abgeschnitten zu werden */
  .kpi-value {
    font-family: 'Archivo Black', Helvetica, sans-serif;
    font-size: 2.6rem; font-weight: 400; color: var(--ink);
    line-height: 0.92; margin: 0 12px 10px -0.04em; padding-left: 12px;
    letter-spacing: -0.05em;
    text-transform: uppercase;
    transform: scaleY(1.1);
    transform-origin: left top;
    overflow-wrap: break-word;
  }
  .kpi-up, .kpi-neutral, .kpi-down {
    font-family: 'Inter', Helvetica, sans-serif;
    font-size: 0.64rem; font-weight: 400; margin: 14px 12px 0 12px; display: block;
  }
  .kpi-up      { color: var(--ink); }
  .kpi-neutral { color: var(--muted); }
  .kpi-down    { color: var(--ink); opacity: 0.6; }

  /* Abschnittstitel als schwarzer Balken, links angeschnitten */
  .section-title {
    display: inline-block;
    font-family: 'Inter', Helvetica, sans-serif;
    font-size: 0.58rem; font-weight: 500; letter-spacing: 0.24em;
    text-transform: uppercase; color: #0a0a0a;
    background: var(--ink);
    border-bottom: none;
    padding: 7px 18px 7px 22px;
    margin: 18px 0 10px -22px;
  }
  .sample-size {
      font-family: 'Inter', Helvetica, sans-serif;
      font-size: 0.56rem;
      font-weight: 400;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 16px;
      display: flex;
      justify-content: flex-end;
  }

[class*="st-key-karte"] {
    background: var(--papier);
    border: none;
    border-radius: 0;
    padding: 1.4rem;
    box-shadow: none;
}
[class*="st-key-karte"]:hover { background: #1a1a1a; }

[data-baseweb="select"] > div, .stTextInput input, .stNumberInput input {
    background: var(--papier) !important;
    border: 1px solid rgba(242, 240, 236, 0.20) !important;
    border-radius: 0 !important;
    color: var(--text) !important;
    font-family: 'Inter', Helvetica, sans-serif !important;
}
[data-testid="stMetricValue"] { color: var(--text); }
hr, [data-testid="stDivider"] { border-color: rgba(242, 240, 236, 0.18); border-width: 1px; }

/* Footer */
footer{padding:34px 0;border-top:1px solid rgba(242, 240, 236, 0.18);color:var(--muted);font-size:0.56rem;letter-spacing:0.3em;text-transform:uppercase}

.footer-logos {
display: flex;
justify-content: center;
align-items: center;
gap: 2.5rem;
flex-wrap: wrap;
margin-bottom: 0.5rem;
}

.footer-logos img {
height: 70px;
max-width: 140px;
object-fit: contain;
opacity: 0.8;
filter: brightness(0) invert(1);
transition: opacity 0.2s ease, transform 0.2s ease;
}

.footer-logos img:hover { opacity: 1; transform: scale(1.04); }

.footer-bottom {
display: flex;
justify-content: space-between;
gap: 1rem;
flex-wrap: wrap;
width: 100%;
}

.stat-label {
    font-family: 'Inter', Helvetica, sans-serif;
    font-size: 0.56rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.24em;
    color: var(--ink);
    margin: 0 0 0.9rem 0;
}

.stat-number {
    font-family: 'Archivo Black', Helvetica, sans-serif;
    font-weight: 400;
    font-size: 6.2rem;
    line-height: 0.86;
    letter-spacing: -0.055em;
    margin: 0;
    color: var(--ink);
    text-transform: uppercase;
}

.stat-number .percent {
    font-size: 2.4rem;
    font-weight: 400;
    color: var(--bg);
    -webkit-text-stroke: 2px var(--ink);
    vertical-align: top;
    margin-left: 0.04em;
}

.stat-description {
    font-family: 'Inter', Helvetica, sans-serif;
    margin: 0.9rem 0 0 0;
    font-size: 0.72rem;
    line-height: 1.5;
    opacity: 1;
}
</style>
"""
GLOBAL = give_global_css()