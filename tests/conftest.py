from flask import Flask

import pytest

from search import create_app
from search.errors import get_error_blueprint


@pytest.fixture(scope='module')
def app() -> Flask:
    app = create_app()
    app.config.update({'TESTING': True})
    app.register_blueprint(get_error_blueprint())
    return app


@pytest.fixture(scope='module')
def client(app) -> Flask:
    return app.test_client()
