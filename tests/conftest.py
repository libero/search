from flask import Flask

import pytest

from search import create_app
from search.errors import get_error_blueprint


@pytest.fixture(scope='module')
def client() -> Flask:
    app = create_app()
    app.register_blueprint(get_error_blueprint())
    return app.test_client()
