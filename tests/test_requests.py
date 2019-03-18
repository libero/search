import logging

from search.requests import request_data


def test_request_data_returns_response(requests_mock):
    url = 'http://some-url.com'
    response_text = 'response received'
    requests_mock.get(url, text=response_text)

    response = request_data(url)
    assert response.status_code == 200
    assert response.text == response_text


def test_request_data_logs_errors_and_returns_none(requests_mock, caplog):
    caplog.set_level(logging.ERROR, logger='search')

    url = 'http://some-url.com'
    reason = 'Not Found'
    status_code = 404
    requests_mock.get(url, reason=reason, status_code=status_code)

    response = request_data(url)
    assert response is None
    expected_log = f'{reason} {status_code}: Unable to retrieve content from {url}.'
    assert caplog.messages[-1] == expected_log
