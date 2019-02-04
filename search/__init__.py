from flask import Flask

from search.search import get_search_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(get_search_blueprint())
    return app
