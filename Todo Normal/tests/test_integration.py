import os
import sys
import pathlib

from fastapi.testclient import TestClient


def setup_module(module):
    # ensure project root is on path so `main` imports work
    tests_dir = pathlib.Path(__file__).parent
    project_root = str(tests_dir.parent)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # remove any existing test DB so tests start clean
    db_path = os.path.join(project_root, "todos.db")
    if os.path.exists(db_path):
        os.remove(db_path)


def teardown_module(module):
    # cleanup DB file created during tests
    tests_dir = pathlib.Path(__file__).parent
    project_root = str(tests_dir.parent)
    db_path = os.path.join(project_root, "todos.db")
    if os.path.exists(db_path):
        os.remove(db_path)


def test_full_crud_flow():
    from main import app

    client = TestClient(app)

    # list page should render
    r = client.get("/todo/")
    assert r.status_code == 200
    assert "To-Do List" in r.text

    # create a todo via form POST (follow redirect)
    r = client.post(
        "/todo/create",
        data={"title": "my first todo", "description": "a test description", "done": "on"},
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "my first todo" in r.text.lower()

    # edit page for id 1
    r = client.get("/todo/edit/1")
    assert r.status_code == 200
    assert "my first todo" in r.text.lower()

    # update the todo
    r = client.post(
        "/todo/update/1",
        data={"title": "updated title", "description": "updated desc", "done": "on"},
        follow_redirects=True,
    )
    assert r.status_code == 200
    assert "updated title" in r.text.lower()

    # delete the todo
    r = client.get("/todo/delete/1", follow_redirects=True)
    assert r.status_code == 200
    assert "updated title" not in r.text.lower()
