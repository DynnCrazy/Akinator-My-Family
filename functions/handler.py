from flask import jsonify
from app import app
from werkzeug.wrappers import Request, Response

def handler(event, context):
    request = Request(event)
    with app.test_request_context(request.path, method=request.method, data=request.get_data(), headers=request.headers):
        response = app.full_dispatch_request()
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(as_text=True)
    }
