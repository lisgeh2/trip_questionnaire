"""
Shared fixtures for the dashboard test suite.

The real data file (fertig_all_waves_UV_RANDOM.sav) is gitignored, so the suite
works two ways:

  * If the real .sav sits next to streamlit_app.py, tests run against it.
  * If not, a synthetic .sav with the same column/label structure is generated
    into a temp dir and used instead, so CI stays green without the real data.

Force one mode with the DASHBOARD_TEST_DATA env var:
    DASHBOARD_TEST_DATA=real       -> fail (not skip) if the real .sav is absent
    DASHBOARD_TEST_DATA=synthetic  -> always use the generated file
"""

import os
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat
import pytest

# dashboard_code/ - the app's modules are flat here and import each other by
# bare name ("import HandleMeta"), so it has to be on sys.path.
APP_DIR = Path(__file__).resolve().parents[1]
APP_FILE = APP_DIR / "streamlit_app.py"
SAV_NAME = "fertig_all_waves_UV_RANDOM.sav"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


# ---------------------------------------------------------------------------
# Synthetic data shaped like the real survey file
# ---------------------------------------------------------------------------

# Every column streamlit_app.py touches, plus the labels it renders.
ZUSTIMMUNG = {
    1.0: "1 - stimme überhaupt nicht zu",
    2.0: "2 - stimme eher nicht zu",
    3.0: "3 - stimme eher zu",
    4.0: "4 - stimme voll und ganz zu",
    99999997.0: "keine Angabe",  # sentinel, must be filtered by clean_value_labels
}
ZUFRIEDENHEIT = {
    1.0: "sehr zufrieden",
    2.0: "eher zufrieden",
    3.0: "eher nicht zufrieden",
    4.0: "überhaupt nicht zufrieden",
}

VALUE_LABELS = {
    "GFS1_1": ZUSTIMMUNG,
    "GFS2_1": ZUFRIEDENHEIT,
    "GFS2_2": ZUFRIEDENHEIT,
    "GFS2_3": ZUFRIEDENHEIT,
    "GFS2_4": ZUFRIEDENHEIT,
    "gender_break": {1.0: "Frau", 2.0: "Mann"},
    "alter_break": {1.0: "18-39 Jahre", 2.0: "40-64 Jahre", 3.0: "65+ Jahre"},
    "education_break": {1.0: "tief", 2.0: "mittel", 3.0: "hoch"},
    "gemeinde_gr_break": {1.0: "< 2000", 2.0: "2000-9999", 3.0: "10000+"},
    "einkommen_break_spez": {1.0: "bis 4000", 2.0: "4001-8000", 3.0: "über 8000"},
    "siedlungsart_break": {1.0: "ländlich", 2.0: "Agglomeration", 3.0: "städtisch"},
    "tz": {1.0: "Total"},
}

COLUMN_LABELS = {
    "GFS1_1": "Wie stark stimmen Sie folgender Aussage zu?",
    "GFS2_1": "Wie zufrieden sind Sie damit? Webseite der Gemeinde/Stadt",
    "GFS2_2": "Wie zufrieden sind Sie damit? Social Media-Kanäle der Gemeinde/Stadt",
    "GFS2_3": "Wie zufrieden sind Sie damit? Mitteilungsblatt/Gemeindeblatt",
    "GFS2_4": "Wie zufrieden sind Sie damit? Newsletter per E-Mail",
    "gender_break": "Geschlecht",
    "alter_break": "Alter",
    "education_break": "Bildung",
    "gemeinde_gr_break": "Gemeindegrösse",
    "einkommen_break_spez": "HH-Einkommen",
    "siedlungsart_break": "Siedlungsart",
    "tz": "Total",
    "gewicht": "Gewichtungsfaktor",
    "DURINT": "Interviewdauer in Sekunden",
    "Jahr": "Erhebungsjahr",
}

# Columns the app selects on / filters by - referenced from the tests too.
BREAK_COLUMNS = [
    "tz",
    "gemeinde_gr_break",
    "education_break",
    "alter_break",
    "gender_break",
    "einkommen_break_spez",
    "siedlungsart_break",
]
QUESTION_COLUMNS = ["GFS1_1", "GFS2_1", "GFS2_2", "GFS2_3", "GFS2_4"]


def build_synthetic_frame(n: int = 400, seed: int = 42) -> pd.DataFrame:
    """A dataframe with the same columns/codes the real .sav is expected to have."""
    rng = np.random.default_rng(seed)
    data = {}
    for col, labels in VALUE_LABELS.items():
        codes = [c for c in labels if c < 99999990]
        data[col] = rng.choice(codes, n).astype(float)
    # A few sentinel responses so the cleaning logic is genuinely exercised.
    data["GFS1_1"][: max(1, n // 40)] = 99999997.0
    data["tz"] = np.ones(n, dtype=float)
    data["gewicht"] = rng.uniform(0.4, 1.8, n)
    # Columns read directly by KpiRenderer rather than through the chart helpers.
    data["DURINT"] = rng.uniform(180.0, 2100.0, n)  # interview duration, seconds
    data["Jahr"] = rng.choice([1.0, 2.0], n).astype(float)  # 1 = current, 2 = prior
    return pd.DataFrame(data)


def write_synthetic_sav(target: Path) -> Path:
    """Write the synthetic frame to a real .sav, labels and all."""
    df = build_synthetic_frame()
    target.parent.mkdir(parents=True, exist_ok=True)
    pyreadstat.write_sav(
        df,
        str(target),
        column_labels=[COLUMN_LABELS.get(c, c) for c in df.columns],
        variable_value_labels={k: v for k, v in VALUE_LABELS.items() if k in df.columns},
    )
    return target


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def app_dir() -> Path:
    return APP_DIR


@pytest.fixture
def app_file(sav_dir) -> Path:
    """
    Path to the streamlit_app.py that the tests execute.

    This deliberately resolves to the copy inside sav_dir rather than to
    APP_DIR. The app loads its data two different ways - load_data() builds an
    absolute path from Path(__file__).parent, while the DATA_TYPE == "sav"
    branch uses a bare relative filename - so the .sav has to sit next to the
    script *and* in the working directory for both to resolve.
    """
    assert APP_FILE.exists(), f"streamlit_app.py not found at {APP_FILE}"
    staged = sav_dir / "streamlit_app.py"
    assert staged.exists(), f"streamlit_app.py not found at {staged}"
    return staged


@pytest.fixture(scope="session")
def data_mode() -> str:
    """Decide up front whether we're running on real or synthetic data."""
    requested = os.environ.get("DASHBOARD_TEST_DATA", "auto").lower()
    real_exists = (APP_DIR / SAV_NAME).exists()

    if requested == "real":
        if not real_exists:
            pytest.fail(f"DASHBOARD_TEST_DATA=real but {SAV_NAME} is missing from {APP_DIR}")
        return "real"
    if requested == "synthetic":
        return "synthetic"
    return "real" if real_exists else "synthetic"


@pytest.fixture(scope="session")
def sav_dir(tmp_path_factory, data_mode) -> Path:
    """
    Directory that contains a usable .sav next to a copy of the app.

    For 'real' this is just APP_DIR. For 'synthetic' we mirror the app folder
    into a temp dir (app code + images) and drop a generated .sav beside it, so
    the app's relative read_sav("...sav") resolves.
    """
    if data_mode == "real":
        return APP_DIR

    staging = tmp_path_factory.mktemp("dashboard_app")
    for item in APP_DIR.iterdir():
        if item.name in {"testing", "tests", "__pycache__", ".git"}:
            continue
        if item.is_file():
            shutil.copy2(item, staging / item.name)
    write_synthetic_sav(staging / SAV_NAME)
    return staging


@pytest.fixture
def in_app_dir(sav_dir, monkeypatch) -> Path:
    """
    chdir into the folder holding the .sav.

    streamlit_app.py reads the file with a bare relative path
    (pyreadstat.read_sav("fertig_all_waves_UV_RANDOM.sav")), so the working
    directory decides whether the app can find its data at all.
    """
    monkeypatch.chdir(sav_dir)
    monkeypatch.syspath_prepend(str(sav_dir))
    return sav_dir


@pytest.fixture
def loaded_sav(in_app_dir):
    """(df, meta) straight from pyreadstat - the same objects the app builds on."""
    df, meta = pyreadstat.read_sav(str(in_app_dir / SAV_NAME))
    return df, meta
