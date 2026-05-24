from flask import Blueprint, jsonify

from services.request_service import RequestService
from services.ai_service import AIService

ai = Blueprint("ai", __name__)


@ai.route("/analyze/<request_id>", methods=["GET"])
def analyze_request(request_id):

    request_data = RequestService.get_request_by_id(request_id)

    if not request_data:

        return jsonify({
            "error": "Request not found"
        }), 404

    analysis = AIService.analyze_request(request_data)

    return jsonify({
        "analysis": analysis
    })