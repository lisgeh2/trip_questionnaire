# Dashboard tests (`testing/`)

Smoke + regression tests for the `.sav` data path. The headline check is that
`streamlit_app.py` executes top to bottom without raising.

Lives in `full_database/dashboard_code/testing/`, alongside `pytest.ini`
in the parent folder.

## Install

```bash
pip install pytest streamlit plotly pandas numpy pyreadstat streamlit-extras scipy
```

## Run

```bash
cd full_database/dashboard_code
pytest              # runs everything in testing/
pytest testing/     # same thing, explicitly
```

## Real vs synthetic data

`fertig_all_waves_UV_RANDOM.sav` is gitignored, so the suite runs either way:

| Mode | Behaviour |
|---|---|
| *(default)* | Uses the real `.sav` if it sits next to `streamlit_app.py`, otherwise generates a synthetic one |
| `DASHBOARD_TEST_DATA=real` | Fails loudly if the real `.sav` is missing |
| `DASHBOARD_TEST_DATA=synthetic` | Always uses generated data — for CI |

```bash
DASHBOARD_TEST_DATA=real pytest      # before a release
DASHBOARD_TEST_DATA=synthetic pytest # in CI
```

The synthetic file is a genuine `.sav` written by `pyreadstat.write_sav`, with
the same columns, codes, value labels and sentinel values as the real one — so
it exercises the identical `pyreadstat` → `HandleMeta` → chart pipeline. If you
add a column to the dashboard, add it to `VALUE_LABELS` / `COLUMN_LABELS` in
`testing/conftest.py`.

## What's covered

**`test_streamlit_app_smoke.py`** — runs the actual app through Streamlit's
`AppTest`:
- executes without exceptions, and renders no `st.error` elements
- charts, KPI cards and header actually render (not just "didn't crash")
- no label leaks to the UI as the string `"None"`
- every one of the 7 break options in the selectbox
- the Gemeindegrösse slider at its narrowest setting
- all 4 channel tabs

Streamlit catches exceptions internally and parks them on `at.exception`
instead of propagating, so these assert on `at.exception` explicitly — a test
that merely imports the module would pass on a broken app.

**`test_sav_data_path.py`** — the failure modes that don't announce themselves:
- `config.DATA_TYPE == "sav"`, and `HandleMeta`'s import-time copy agrees
- the `WEIGHTING` column exists in the data
- every column label is a non-empty string, every value-label lookup a dict
- **every code present in the data has a matching value label** — this is the
  `KeyError: np.float64(1.0)` bug
- each chart helper builds a non-empty figure for every column the app uses
- weighted percentages sum to ~100

## Notes

Two things the tests work around rather than fix, both worth tidying up:

1. `streamlit_app.py` reads its data with a bare relative path
   (`pyreadstat.read_sav("fertig_all_waves_UV_RANDOM.sav")`) and no longer
   calls `os.chdir`, so the app only works when launched from this folder. The
   `in_app_dir` fixture chdirs to compensate. Using `Path(__file__).parent /
   "fertig_all_waves_UV_RANDOM.sav"` would remove the constraint.

2. The `elif config.DATA_TYPE == "jsonl"` branch calls `build_df()` and
   `transform_to_meta()`, neither of which is defined or imported anywhere —
   that branch is a `NameError`. `test_data_type_is_sav` pins the config to the
   working path in the meantime.
