from html import escape
from colors import MULTIPLE_COLORS, CORE_COLOR, FARBEN_4_ABSTUFUNGEN
import base64
from config import STYLE

def give_subtitle_block(subtitle):
  if STYLE == "gfs":
    return f"""
    <div style="
      font-size: 0.80rem;
      letter-spacing: 0.08em;
      color: #7a7269;
      margin-bottom: 6px;
      font-weight: 600;
    "><br>
      {subtitle}
    </div>
    """
  if STYLE == "cool_black":
    return f"""
    <div style="
      font-size: 0.86rem;
      letter-spacing: 0.02em;
      color: rgba(234, 240, 255, 0.50);
      margin-top: 14px;
      margin-bottom: 0;
      font-weight: 400;
      max-width: 58ch;
      line-height: 1.5;
    ">
      {subtitle}
    </div>
    """

def give_header_css(window, year, title, subtitle_block, image_b64):
  if STYLE == "gfs":
    return f"""
      <div style="
      background: #ffffff;
      border: 0px solid {FARBEN_4_ABSTUFUNGEN["blau"]["sehr_dunkel"]};
      border-radius: 2px;
      padding: 34px 56px 28px 56px;
      margin-bottom: 22px;
      box-shadow: 0 10px 30px rgba(80, 60, 40, 0.20);
      ">

      <!-- Horizontale Zeile: Text links, Logo rechts -->
      <div style="
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 20px;
      ">

      <!-- Linke Spalte: Badge + Titel + Subtitle -->
      <div style="
      flex: 1 1 auto;
      min-width: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      ">

      <div style="
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: {CORE_COLOR[0]};
      background: {CORE_COLOR[9]};
      padding: 7px 12px;
      border-radius: 999px;
      margin-bottom: 14px;
      width: fit-content;
      ">
      <span>{window}</span>
      <span style="opacity: 0.45;">•</span>
      <span>Schweiz {year}</span>
      </div>

      <div style="
      font-size: 2.5rem;
      font-weight: 700;
      color: {MULTIPLE_COLORS[5]};
      line-height: 1.08;
      letter-spacing: 0.02em;
      margin: 0;
      ">
      {title}
      </div>

      {subtitle_block}

      </div>

      <!-- Rechte Spalte: Logo -->
      <div style="
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      ">
      <img src="data:image/png;base64,{image_b64}" alt="GFS" style="
      max-height: 110px;
      width: auto;
      display: block;
      object-fit: contain;
      border-radius: 12px;
      ">
      </div>
      </div>
      """

  if STYLE == "cool_black":
    return f"""
      <div style="
      background: transparent;
      border: none;
      border-bottom: 1px solid rgba(234, 240, 255, 0.12);
      padding: 8px 0 30px 0;
      margin-bottom: 30px;
      position: relative;
      ">

      <!-- Glow hinter dem Titel -->
      <div style="
      position: absolute;
      top: -40px; left: -60px;
      width: 420px; height: 220px;
      background: radial-gradient(closest-side, {CORE_COLOR[0]}, transparent);
      opacity: 0.13;
      filter: blur(40px);
      pointer-events: none;
      "></div>

      <!-- Horizontale Zeile: Text links, Logo rechts -->
      <div style="
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 20px;
      position: relative;
      ">

      <!-- Linke Spalte: Badge + Titel + Subtitle -->
      <div style="
      flex: 1 1 auto;
      min-width: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      ">

      <div style="
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 0.66rem;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: {CORE_COLOR[0]};
      background: {CORE_COLOR[9]};
      border: 1px solid {CORE_COLOR[7]};
      padding: 6px 14px;
      border-radius: 999px;
      margin-bottom: 18px;
      width: fit-content;
      box-shadow: 0 0 24px {CORE_COLOR[8]};
      ">
      <span>{window}</span>
      <span style="opacity: 0.45;">/</span>
      <span>Schweiz {year}</span>
      </div>

      <div style="
      font-family: 'Archivo', 'Inter', sans-serif;
      font-variation-settings: 'wdth' 112;
      font-size: 4.2rem;
      font-weight: 800;
      line-height: 0.94;
      letter-spacing: -0.03em;
      margin: 0;
      text-transform: uppercase;
      background: linear-gradient(100deg,
                  {MULTIPLE_COLORS[5]} 0%,
                  {MULTIPLE_COLORS[5]} 38%,
                  {MULTIPLE_COLORS[5]} 78%,
                  {MULTIPLE_COLORS[5]} 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      color: {MULTIPLE_COLORS[5]};
      ">
      {title}
      </div>

      {subtitle_block}

      </div>

      <!-- Rechte Spalte: Logo -->
      <div style="
      flex: 0 0 auto;
      display: flex;
      align-items: center;
      ">
      <img src="data:image/png;base64,{image_b64}" alt="GFS" style="
      max-height: 90px;
      width: auto;
      display: block;
      object-fit: contain;
      filter: brightness(0) invert(1);
      opacity: 0.85;
      ">
      </div>
      </div>
      </div>
      """

def header(title=None, subtitle=None, year=None, window=None, image="gfs.png"):
    title = escape(title or "Untitled Dashboard")
    subtitle = escape(subtitle or "")
    year = escape(str(year or "2026"))
    window = escape(window or "Marktforschung")

    with open(image, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    if subtitle:
      subtitle_block = give_subtitle_block(subtitle)
    else:
      subtitle_block=""

    return give_header_css(window, year, title, subtitle_block, image_b64)