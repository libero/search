import logging
from io import BytesIO

from flask import Blueprint, Response

from lxml import etree

from search.index import index_document
from search.requests import request_data
from search.settings import CONTENT_SERVICES_TO_INDEX, GATEWAY_URL
from search.utils import strip_slashes

LOGGER = logging.getLogger(__name__)


def get_populate_blueprint() -> Blueprint:
    blueprint = Blueprint('populate', __name__)

    @blueprint.route('/populate', methods=['POST'])
    def populate() -> Response:
        """
        Route for triggering indexing of known paths. Will be used as a proof of
        concept. This should be removed before MVP release.
        """
        gateway = strip_slashes(GATEWAY_URL)
        document_count = 0

        for service in CONTENT_SERVICES_TO_INDEX:
            url = f'{gateway}/{service}/items'
            response = request_data(url)
            if not response:
                continue

            root = etree.parse(BytesIO(response.content)).getroot()
            for item in root.iter('{http://libero.pub}item-ref'):
                item_url = url + f'/{item.attrib.get("id")}/versions/latest'
                response = request_data(item_url)
                if not response:
                    continue

                item_root = etree.parse(BytesIO(response.content)).getroot()
                document = {}
                for tag in ['id', 'service']:
                    element = item_root.find(f'libero:meta/libero:{tag}',
                                             namespaces={'libero': 'http://libero.pub'})
                    if element.text:
                        document[tag] = element.text

                if document and 'id' in document:
                    index_document(
                        index='articles', doc_type='article', id=document['id'], body=document
                    )
                    document_count += 1

        return Response(response=f'{document_count} documents have been indexed')

    return blueprint
