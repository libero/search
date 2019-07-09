"""
Search application settings.
"""
from typing import List

GATEWAY_URL: str = 'http://unstable--api-gateway.libero.pub'

ELASTICSEARCH_HOSTS: List[str] = [
    'http://elasticsearch:9200',
]

CONTENT_SERVICES_TO_INDEX: List[str] = [
    'blog-articles',
    'scholarly-articles',
]
