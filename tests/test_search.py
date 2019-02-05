import os
from io import BytesIO

from lxml import etree


def test_empty_response(client) -> None:

    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                        'schemas',
                        'item-list.xsd')

    with open(path, 'rb') as xmlfile:
        xmlschema_doc = etree.XML(xmlfile.read())

    xmlschema = etree.XMLSchema(xmlschema_doc)

    response = client.get('/search')
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'

    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    assert xmlschema.validate(xml) is True, xmlschema.error_log
    assert root.getchildren() == []
