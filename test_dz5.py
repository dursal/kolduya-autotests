import sqlite3
import os
import pytest
from main import add_user

#Таблица users с полями: id, name, email, age
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
        email TEXT NOT NULL,
        age INTEGER
    )
    """)
    conn.commit()
    conn.close()
    yield


def test_users_in_db(setup_db):
    #Заполни таблицу минимум 3 пользователями
    add_user("Аня", "anya@example.com", 17)
    add_user("Ваня", "vanya@example.com", 23)
    add_user("Таня", "tanya@example.com", 15)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    assert len(users) == 3
    assert any('@' in user[2] for user in users)  # проверка email

    conn.close()