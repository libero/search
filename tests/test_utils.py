import pytest

from search import settings
from search.exceptions import RequiredSettingNotSet
from search.utils import check_required_settings, strip_slashes


@pytest.mark.parametrize('input, expected', [
    ('http://api-gateway/', 'http://api-gateway'),
    ('/test-path', 'test-path'),
    ('test-path/', 'test-path'),
    ('/test-path/', 'test-path'),
    ('test-path', 'test-path'),
    ('/test-path/somewhere/', 'test-path/somewhere')
])
def test_strip_slashes(input, expected):
    assert strip_slashes(input) == expected


@pytest.mark.parametrize('gateway, es_hosts', [
    ('', ['elasticsearch host']),
    ('api-gateway', [])
])
def test_check_required_settings_raises_exception(gateway, es_hosts):
    settings.GATEWAY_URL = gateway
    settings.ELASTICSEARCH_HOSTS = es_hosts
    with pytest.raises(RequiredSettingNotSet):
        check_required_settings()


def test_check_required_settings_does_not_raise_exception():
    settings.GATEWAY_URL = 'test value'
    settings.ELASTICSEARCH_HOSTS = ['elasticsearch host 1']
    check_required_settings()
