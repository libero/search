from flask import Blueprint, Response

from lxml import etree

LIBERO_NAMESPACE = 'http://libero.pub'
NAMESPACE_MAP = {None: LIBERO_NAMESPACE}


def get_search_blueprint() -> Blueprint:
    blueprint = Blueprint('search', __name__)

    @blueprint.route('/search', methods=['GET'])
    def search() -> Response:  # pylint: disable=unused-variable
        root = etree.Element('item-list', nsmap=NAMESPACE_MAP)
        response = etree.tostring(root, xml_declaration=True, encoding='UTF-8')
        return Response(response=response, status=200, mimetype='application/xml')

    return blueprint
