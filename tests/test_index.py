import elasticsearch

from search.index import index_document
from search.settings import ELASTICSEARCH_HOSTS


def test_index_document_logs_connection_errors(caplog, mocker):
    es_index = mocker.patch('search.index.Elasticsearch.index')
    es_index.side_effect = elasticsearch.exceptions.ConnectionError()

    index = 'test-index'
    doc_type = 'article'
    id = '1'
    body = {'body': 'test'}
    index_document(index=index, doc_type=doc_type, id=id, body=body)

    expected_log = f'Unable to connect to {ELASTICSEARCH_HOSTS}'
    assert caplog.messages[-1] == expected_log
