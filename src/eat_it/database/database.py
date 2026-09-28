import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]

DATABASE_PATH = BASE_DIR / "data" / "eat_it.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")

    return connection


def initialize_database():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as connection:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")
        connection.executescript(schema)


if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")