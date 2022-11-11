import pytest

from asserter import assert_eval, assert_equal
from session import HTTPSession
from test_utils import RequestPostParams, RequestTypes, StatusCodes, Connect
from logger import decorate_test


class Test_Post:

    @staticmethod
    @decorate_test
    def test_book_review_api_post_success():
        status_code, _ = HTTPSession.send_request(RequestTypes.POST, Connect.URL, RequestPostParams.val1)
        assert_equal(status_code, StatusCodes.STATUS_201, f'Status code of {Connect.URL} endpoint')

    @staticmethod
    @decorate_test
    def test_book_review_api_post_failure_1():
        status_code, _ = HTTPSession.send_request(RequestTypes.POST, Connect.URL, RequestPostParams.val1)
        assert_equal(status_code, StatusCodes.STATUS_409, f'Status code of {Connect.URL} endpoint')

    @staticmethod
    @decorate_test
    def test_book_review_api_post_failure_2():
        status_code, _ = HTTPSession.send_request(RequestTypes.POST, Connect.URL, RequestPostParams.val2)
        assert_equal(status_code, StatusCodes.STATUS_400, f'Status code of {Connect.URL} endpoint')

    @staticmethod
    @decorate_test
    def test_book_review_api_post_failure_3():
        status_code, res = HTTPSession.send_request(RequestTypes.POST, Connect.URL, RequestPostParams.val3)
        assert_equal(status_code, StatusCodes.STATUS_400, f'Status code of {Connect.URL} endpoint')
        assert_eval(res, 'error', f'Error string in response evaluation: {res}')
