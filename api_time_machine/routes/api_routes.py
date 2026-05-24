from flask import Blueprint, request, jsonify

# updated by codex: switched to package-safe imports
from api_time_machine.services.request_service import RequestService

# updated by codex: switched to package-safe imports
from api_time_machine.middleware.request_logger import log_request

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


@api.route("/test-external", methods=["POST"])
def test_external_api():

    # updated by codex: allow testing/storing different external APIs from dashboard
    payload = request.json or {}
    target_url = payload.get("url")
    method = (payload.get("method") or "GET").upper()
    request_body = payload.get("request_body")

    if not target_url:
        return jsonify({"error": "url is required"}), 400

    import requests

    try:
        if method == "GET":
            response = requests.get(target_url)
        elif method == "POST":
            response = requests.post(target_url, json=request_body)
        elif method == "PUT":
            response = requests.put(target_url, json=request_body)
        elif method == "PATCH":
            response = requests.patch(target_url, json=request_body)
        elif method == "DELETE":
            response = requests.delete(target_url, json=request_body)
        else:
            return jsonify({"error": f"Unsupported method: {method}"}), 400

        try:
            response_payload = response.json()
        except ValueError:
            response_payload = response.text

        save_data = {
            "endpoint": target_url,
            "method": method,
            "request_body": request_body,
            "response": response_payload,
            "status_code": response.status_code,
            "full_url": target_url
        }

        RequestService.save_request(save_data)
        log_request(save_data)

        return jsonify({
            "message": "External API tested and saved",
            "result": response_payload,
            "status_code": response.status_code
        }), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500


@api.route("/history", methods=["GET"])
def history():

    requests_data = RequestService.get_all_requests()

    return jsonify(requests_data)
