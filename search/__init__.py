from flask import Flask

from werkzeug.exceptions import HTTPException

from search.errors import http_error_handler
from search.ping import get_ping_blueprint
from search.search import get_search_blueprint


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(get_search_blueprint())
    app.register_blueprint(get_ping_blueprint())

    app.register_error_handler(HTTPException, http_error_handler)

    return app
