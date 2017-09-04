from flask import Response
import json
from urllib import parse


def create_response(json, code=200):
    resp = Response(response=json,
                    status=code,
                    mimetype="application/json")
    return resp


def json_of_response(response):
    return json.loads(response.data.decode('utf8'))


def url_encode_string(text):
    return parse.quote(text)


def test_fucntion():
    pass