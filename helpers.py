from flask import Response


def create_response(json, code=200):
    resp = Response(response=json,
                    status=code,
                    mimetype="application/json")
    return resp
