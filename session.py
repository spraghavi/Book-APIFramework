import json
from requests import RequestException
from logger import Logger
from test_utils import Req_Headers


class HTTPSession:

    @staticmethod
    def send_request(request_type, endpoint, params):
        do_logging = params.pop('do_logging', True)

        try:
            response = request_type(endpoint, data=json.dumps(params), headers=Req_Headers.header)
            if do_logging:
                Logger.log_request(request_type, endpoint, params, response.status_code)
            return response.status_code, json.loads(response.text)
        except RequestException as e:
            Logger.log('Could not send {} request due to exception: {}'.format(request_type, e))
