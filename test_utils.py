import requests


class Connect:
    URL = 'https://fw-qainterview-books-app.azurewebsites.net/api/book/'


class RequestGetParams:
    isbn1 = '9788418196553'
    isbn2 = '9781776742318'


class RequestPostParams:
    val1 = {
        "isbn": "9788418196554",
        "title": "Fire & Blood",
        "author": "George R. R. Martin",
        "review": "93% liked this book"
    }
    val2 = {
        "isbn": "9781776742318",
        "title": "Fire and Ice",
        "author": "Robert FROST",
        "review": ""
    }
    val3 = {
        "isbn": "9781776742318",
        "title": "Dragon Books",
        "author": "Robert FROST"
    }


class RequestTypes:
    GET = requests.get
    POST = requests.post


class Endpoints:
    get_url1 = Connect.URL + RequestGetParams.isbn1
    get_url2 = Connect.URL + RequestGetParams.isbn2


class StatusCodes:
    STATUS_200 = '200'  # Success for Get
    STATUS_201 = '201'  # Success for Post
    STATUS_400 = '400'  # Bad request
    STATUS_404 = '404'  # Not Found
    STATUS_409 = '409'  # Conflict


class Req_Headers:
    header = {'Content-type': 'application/json', 'Accept': 'text/plain'}
