from flask import Flask


def create_app():
    """Build and return the Flask app.

    The app is built inside a function so that each test can make its own
    fresh copy, and so that later slices can pass in settings.
    """
    app = Flask(__name__)

    @app.get("/health")
    def health():
        # Flask turns a dict into a JSON response with status 200.
        return {"status": "ok"}

    return app
