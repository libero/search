from flask import Flask

import pytest

from search import create_app, settings
from search.errors import get_error_blueprint


@pytest.fixture(scope='module')
def app() -> Flask:
    settings.ELASTICSEARCH_HOSTS = ['http://libero-elasticsearch']
    settings.GATEWAY_URL = 'http://libero-api-gateway'
    app = create_app()
    app.config.update({'TESTING': True})
    app.register_blueprint(get_error_blueprint())
    return app


@pytest.fixture(scope='module')
def client(app) -> Flask:
    return app.test_client()
