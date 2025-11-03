import os
import sqlite3
import pytest
from src.db import init_db, add_task, get_all_tasks, remove_task, update_task, complete_task

TEST_DB = "test_todo.db"


@pytest.fixture
def test_db():
    """Fixture to set up and tear down a temporary test database."""
    # Setup: ensure clean start
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    init_db(TEST_DB)
    yield TEST_DB
    # Teardown: clean up
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def table_exists(db_path, table_name):
    """Helper function to check if a table exists in the SQLite DB."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,)
        )
        return cursor.fetchone() is not None


def test_init_db_creates_tasks_table(test_db):
    assert table_exists(test_db, "tasks"), "Table 'tasks' should exist after initialization"


def test_add_task_and_retrieve(test_db):
    add_task(test_db, "Buy milk")

    tasks = get_all_tasks(test_db)
    assert len(tasks) == 1
    _, description, status, _ = tasks[0]  # ignore id and timestamp
    assert description == "Buy milk"
    assert status == "Pending"


def test_delete_task(test_db):
    add_task(test_db, "Buy milk")
    remove_task(test_db, 1)

    tasks = get_all_tasks(test_db)

    assert len(tasks) == 0


def test_update_task(test_db):
    add_task(test_db,"Buy milk")
    update_task(test_db,1,'Buy bread')
    tasks = get_all_tasks(test_db)

    assert len(tasks) == 1
    _, description, status, _ = tasks[0]
    assert description == 'Buy bread'


def test_complete_task(test_db):
    add_task(test_db,"Buy milk")
    complete_task(test_db,"Buy milk")

    tasks = get_all_tasks(test_db)
    assert len(tasks) == 1
    _, description, status, _ = tasks[0]
    assert description == 'Buy milk'
    assert status == 'Done'