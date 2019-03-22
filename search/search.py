from flask import Blueprint, Response

from elasticsearch import Elasticsearch
from lxml import etree

from search.settings import ELASTICSEARCH_HOSTS

LIBERO_NAMESPACE = 'http://libero.pub'
NAMESPACE_MAP = {None: LIBERO_NAMESPACE}


def get_search_blueprint() -> Blueprint:
    blueprint = Blueprint('search', __name__)

    @blueprint.route('/', methods=['GET'])
    def search() -> Response:
        # get all documents or query for search term
        search = Elasticsearch(hosts=ELASTICSEARCH_HOSTS)
        # pylint: disable=unexpected-keyword-arg
        hits = search.search(index='_all', filter_path=['hits.hits._source'])
        # pylint: enable=unexpected-keyword-arg
        if hits:
            # get relevant information from results
            hits = hits.get('hits', {}).get('hits', [])
            hits = [hit['_source'] for hit in hits if hit.get('_source')]

        # create xml response
        root = etree.Element('item-list', nsmap=NAMESPACE_MAP)
        for hit in hits:
            attributes = {key: hit[key] for key in ['id', 'service'] if hit.get(key)}
            etree.SubElement(root, 'item-ref', attrib=attributes)

        response = etree.tostring(root, xml_declaration=True, encoding='UTF-8')
        return Response(response=response, status=200, mimetype='application/xml')

    return blueprint
