from io import BytesIO

import pytest
from lxml import etree

from search.errors import NAMESPACE_MAP
from tests.schema_utils import get_schema_file_path


@pytest.mark.parametrize('status_code, name', [
    (400, 'Bad Request'),
    (401, 'Unauthorized'),
    (403, 'Forbidden'),
    (404, 'Not Found'),
    (405, 'Method Not Allowed'),
    (406, 'Not Acceptable'),
    (408, 'Request Timeout'),
    (409, 'Conflict'),
    (410, 'Gone'),
    (411, 'Length Required'),
    (412, 'Precondition Failed'),
    (413, 'Request Entity Too Large'),
    (414, 'Request URI Too Long'),
    (415, 'Unsupported Media Type'),
    (416, 'Requested Range Not Satisfiable'),
    (417, 'Expectation Failed'),
    (418, 'I\'m a teapot'),
    (428, 'Precondition Required'),
    (429, 'Too Many Requests'),
    (431, 'Request Header Fields Too Large'),
    (500, 'Internal Server Error'),
    (501, 'Not Implemented'),
    (502, 'Bad Gateway'),
    (503, 'Service Unavailable'),
    (504, 'Gateway Timeout'),
    (505, 'HTTP Version Not Supported')
])
def test_custom_error_handler(client, status_code, name) -> None:
    url = '/error?code=%s' % status_code
    response = client.get(url)
    assert response.status_code == status_code
    assert response.content_type == 'application/problem+xml; charset=utf-8', status_code

    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    schema_path = get_schema_file_path('error.rng')
    xmlschema_doc = etree.parse(schema_path)
    validator = etree.RelaxNG(xmlschema_doc)

    assert validator.validate(xml) is True, validator.error_log
    assert int(root.find('status', namespaces=NAMESPACE_MAP).text) == status_code
    assert root.find('title', namespaces=NAMESPACE_MAP).text == name


def test_default_error_code(client):
    response = client.get('/error')
    assert response.status_code == 404
