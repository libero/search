from io import BytesIO

from lxml import etree, isoschematron

from tests.schema_utils import get_schema_file_path


def test_empty_response(client, mocker):
    es_search = mocker.patch('search.search.Elasticsearch.search')
    es_search.return_value = {}

    path = get_schema_file_path('item-list.rng')
    xmlschema_doc = etree.parse(path)
    validator = isoschematron.Schematron(xmlschema_doc)

    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'

    xml = etree.parse(BytesIO(response.data))
    root = xml.getroot()

    assert validator.validate(xml) is True, validator.error_log
    assert root.getchildren() == []


def test_search(client, mocker):
    es_search = mocker.patch('search.search.Elasticsearch.search')
    es_search.return_value = {
        'hits': {
            'hits': [
                {
                    '_source': {
                        'id': 'article1', 'service': 'scholarly-articles'
                    }
                },
                {
                    '_source': {
                        'id': 'article2', 'service': 'scholarly-articles'
                    }
                },
                {
                    '_source': {
                        'id': 'post1', 'service': 'blog-articles'
                    }
                },
                {
                    '_source': {
                        'id': 'post2', 'service': 'blog-articles'
                    }
                },
            ]
        }
    }

    path = get_schema_file_path('item-list.rng')
    xmlschema_doc = etree.parse(path)
    validator = isoschematron.Schematron(xmlschema_doc)

    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'

    xml = etree.parse(BytesIO(response.data))
    assert validator.validate(xml) is True, validator.error_log

    root = xml.getroot()
    assert len(root.getchildren()) == 4
