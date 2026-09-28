import pytest

from eat_it.database import database


@pytest.fixture(autouse=True)
def test_database(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DATABASE_PATH",
        db_path,
    )

    database.initialize_database()
    