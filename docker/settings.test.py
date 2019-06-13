"""
Search application settings.
"""
from typing import List

GATEWAY_URL: str = 'http://test-api-gateway'

ELASTICSEARCH_HOSTS: List[str] = [
    'http://test-elasticsearch',
]

CONTENT_SERVICES_TO_INDEX: List[str] = [
    'test-scholarly-articles',
]
