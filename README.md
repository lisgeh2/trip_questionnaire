# Streamlit questionnaire

A small survey app: login → 3 pages of questions → answers appended to a file.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Log in with the demo account `demo` / `demo1234` (created automatically on
first start). Add a real account and delete the demo one:

```bash
python auth.py add alice
```

## Files

| File            | What it does                                              |
|-----------------|-----------------------------------------------------------|
| `app.py`        | The Streamlit UI: login, sidebar, pages, submit            |
| `questions.py`  | The questions themselves — edit this to change the survey  |
| `auth.py`       | Salted SHA-256 password check + `users.json`               |
| `storage.py`    | Appends each submission to `data/responses.jsonl`          |

## The answers

Every submission is one line of JSON in `data/responses.jsonl`:

```python
import pandas as pd
df = pd.read_json("data/responses.jsonl", lines=True)
```

Or export a flat CSV for Excel:

```bash
python storage.py
```

## Notes

- `users.json` and `data/` are generated at runtime; keep them out of git.
- Session state is per browser tab, so two people can fill in the form at the
  same time without seeing each other's answers.
- The login is good enough for an internal survey. If the app is reachable
  from the internet, put it behind SSO/a reverse proxy or use
  `streamlit-authenticator`.
