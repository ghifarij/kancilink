import pytest

from app import create_app


@pytest.fixture
def client():
    """A fake browser for tests: it calls the app without starting a server."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
