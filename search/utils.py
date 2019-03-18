import re
from typing import List

from search import settings
from search.exceptions import RequiredSettingNotSet

REQUIRED_SETTINGS: List[str] = [
    'GATEWAY_URL',
    'ELASTICSEARCH_HOSTS'
]


def strip_slashes(path: str) -> str:
    """removes forward slashes from the beginning and the end of a string"""
    return re.sub(r'^/|/$', '', path)


def check_required_settings() -> None:
    for setting in REQUIRED_SETTINGS:
        if not getattr(settings, setting, None):
            message = f'{setting} is required and must be set in search/constants.py\n'
            raise RequiredSettingNotSet(message)
