from flask import Flask

import pytest

from search import create_app


@pytest.fixture(scope='module')
def client() -> Flask:
    app = create_app()
    return app.test_client()
