from xml.dom import XML_NAMESPACE

from flask import Blueprint, Response, abort, request

from lxml import etree
from lxml.builder import ElementMaker
from werkzeug.exceptions import HTTPException

NAMESPACE_MAP = {None: 'urn:ietf:rfc:7807'}


def http_error_handler(error: HTTPException) -> Response:
    doc = ElementMaker(nsmap=NAMESPACE_MAP)
    # pylint: disable=no-member
    error_doc = doc.problem(
        doc.status(str(error.code)),
        doc.title(error.name),
        doc.detail(error.description),
    )
    # pylint: enable=no-member
    error_doc.set('{%s}lang' % XML_NAMESPACE, "en")
    response = etree.tostring(error_doc, xml_declaration=True, encoding='UTF-8')
    return Response(response=response, status=error.code, mimetype='application/problem+xml')


def get_error_blueprint() -> Blueprint:
    blueprint = Blueprint('error', __name__)

    @blueprint.route('/error', methods=['GET'])
    def error() -> None:  # pylint: disable=unused-variable
        """
        /error endpoint designed to test error pages
        """
        status_code = request.args.get('code')
        if isinstance(status_code, str) and status_code.isnumeric():
            status_code = int(status_code)
        else:
            status_code = 404
        abort(status_code)

    return blueprint
