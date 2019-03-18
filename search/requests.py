import logging
from typing import Union

import requests

LOGGER = logging.getLogger(__name__)


def request_data(url: str) -> Union[requests.Response, None]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.HTTPError as error:
        LOGGER.exception('%s %s: Unable to retrieve content from %s.',
                         error.response.reason,
                         error.response.status_code,
                         url)
        return None
