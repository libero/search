import logging

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

from search.settings import ELASTICSEARCH_HOSTS

LOGGER = logging.getLogger(__name__)


def index_document(index: str, doc_type: str, id: str, body: dict) -> None:
    try:
        search = Elasticsearch(hosts=ELASTICSEARCH_HOSTS)
        search.index(index=index, doc_type=doc_type, id=id, body=body)
        LOGGER.debug('Document %s saved at /%s/%s/%s', id, index, doc_type, id)
    except ConnectionError:
        LOGGER.exception('Unable to connect to %s', ELASTICSEARCH_HOSTS)
