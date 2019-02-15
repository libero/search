from io import BytesIO

from lxml import etree, isoschematron

from tests.schema_utils import get_schema_file_path


def test_empty_response(client) -> None:
    path = get_schema_file_path('item-list.rng')
    xmlschema_doc = etree.parse(path)
    validator = isoschematron.Schematron(xmlschema_doc)

    response = client.get('/search')
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'

    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    assert validator.validate(xml) is True, validator.error_log
    assert root.getchildren() == []
