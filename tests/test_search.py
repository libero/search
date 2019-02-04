from io import BytesIO

from lxml import etree


def test_empty_response(client) -> None:
    response = client.get('/search')
    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    assert root.getchildren() == []


def test_empty_response_is_well_formed(client) -> None:
    response = client.get('/search')
    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'
    assert xml.docinfo.encoding == 'UTF-8'
    assert xml.docinfo.xml_version == '1.0'
    assert xml.docinfo.root_name == 'item-list'
    assert root.tag == '{http://libero.pub}item-list'  # check namespace
