# Todo Normal — FastAPI To-Do App

Small example FastAPI application that uses Jinja2 templates and SQLite.

Prerequisites
- Python 3.10+ installed
- A virtual environment (recommended)

Quick start
1. Open a terminal in the project folder (the folder that contains this README):

```bash
cd "Todo Normal"
```

2. Create and activate a venv (macOS / Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Upgrade pip and install dependencies (note: quote extras to avoid zsh globbing):

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install "fastapi[all]" sqlalchemy jinja2 python-multipart pytest
```

If you prefer a smaller install for running the app only:

```bash
python -m pip install fastapi "uvicorn[standard]" sqlalchemy jinja2 python-multipart
```

Run the app

```bash
# from inside "Todo Normal" with the venv active
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open the UI at: http://127.0.0.1:8000/todo/

Database
- The app uses SQLite. The file `todos.db` is created automatically when the app runs (see `main.py`).

Tests
- Integration tests use `fastapi.testclient` and are under `tests/`.

```bash
python -m pytest -q
```

Notes
- If you see zsh errors when installing extras (like `uvicorn[standard]`), quote the requirement as shown above.
- A couple of small helpers were added to render nicer text in templates (Jinja filters). Templates are in the `templates/` folder.

Files of interest
- `main.py` — app entrypoint
- `crud.py` — routes and template wiring
- `database.py` — SQLAlchemy setup
- `models.py` — DB models
- `templates/` — Jinja2 HTML templates
- `tests/test_integration.py` — integration test exercising CRUD

If you want, I can add a `requirements.txt` and a small `run.sh` to simplify these commands.
