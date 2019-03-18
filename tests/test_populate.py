from search import index, populate
from tests.assets import get_asset


def test_populate(client, requests_mock, mocker):
    gateway = 'http://api-gateway'
    service_to_index = 'scholarly-articles'

    index.ELASTICSEARCH_HOSTS = ['http://elasticsearch']
    populate.GATEWAY_URL = gateway
    populate.CONTENT_SERVICES_TO_INDEX = [service_to_index]

    xml = get_asset('scholarly-articles-items-response.xml')
    requests_mock.get(f'{gateway}/{service_to_index}/items', text=xml)

    xml = get_asset('scholarly-articles-article1-response.xml')
    requests_mock.get(f'{gateway}/{service_to_index}/items/article1/versions/latest', text=xml)

    es_mock = mocker.patch('search.populate.index_document')

    response = client.post('/populate')
    assert response.status_code == 200
    es_mock.assert_called_once()

    kwargs = {'index': 'articles',
              'doc_type': 'article',
              'id': 'article1',
              'body': {'id': 'article1',
                       'service': 'scholarly-articles'}
              }
    es_mock.assert_called_with(**kwargs)
