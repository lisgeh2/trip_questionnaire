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
GLOBAL = give_global_css()