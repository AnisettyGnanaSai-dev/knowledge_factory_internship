from flask import Blueprint, request, jsonify

from services.request_service import RequestService

from middleware.request_logger import log_request

api = Blueprint("api", __name__)


@api.route("/test-api", methods=["POST"])
def test_api():

    request_data = request.json

    response_data = {
        "message": "API received successfully",
        "received_data": request_data
    }

    save_data = {
        "endpoint": "/test-api",
        "method": "POST",
        "request_body": request_data,
        "response": response_data,
        "status_code": 200
    }

    RequestService.save_request(save_data)

    log_request(save_data)

    return jsonify(response_data), 200


@api.route("/history", methods=["GET"])
def history():

    requests_data = RequestService.get_all_requests()

    return jsonify(requests_data)