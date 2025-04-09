import sqlite3
import os
import pytest
from main import add_user, get_user_by_name, update_user_email, delete_user

@pytest.fixture
def setup_db():
    if os.path.exists("test.db"):
        os.remove("test.db")
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    yield

def test_get_user(setup_db):
    add_user("Аня", "anya@example.com")
    user = get_user_by_name("Аня")
    assert user is not None
    assert user[1] == "Аня"
    assert user[2] == "anya@example.com"

def test_update_email(setup_db):
    add_user("Миша", "misha@old.com")
    update_user_email("Миша", "misha@new.com")
    user = get_user_by_name("Миша")
    assert user[2] == "misha@new.com"

def test_delete_user(setup_db):
    add_user("Лена", "lena@example.com")
    delete_user("Лена")
    user = get_user_by_name("Лена")
    assert user is None

