from asserter import assert_equal
from session import HTTPSession
from test_utils import Endpoints, RequestTypes, StatusCodes
from logger import decorate_test

params = {'accept': 'application/json'}


class Test_Get:

    @staticmethod
    @decorate_test
    def test_book_review_api_get_success():
        status_code, _ = HTTPSession.send_request(RequestTypes.GET, Endpoints.get_url1, params)
        assert_equal(status_code, StatusCodes.STATUS_200, f'Status code of {Endpoints.get_url1} endpoint')

    @staticmethod
    @decorate_test
    def test_book_review_api_get_failure():
        status_code, _ = HTTPSession.send_request(RequestTypes.GET, Endpoints.get_url2, params)
        assert_equal(status_code, StatusCodes.STATUS_404, f'Status code of {Endpoints.get_url2} endpoint')
