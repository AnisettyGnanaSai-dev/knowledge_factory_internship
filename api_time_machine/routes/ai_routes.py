from flask import Blueprint, jsonify

# updated by codex: switched to package-safe imports
from api_time_machine.services.request_service import RequestService
from api_time_machine.services.ai_service import AIService

ai = Blueprint("ai", __name__)


@ai.route("/analyze/<request_id>", methods=["GET"])
def analyze_request(request_id):

    request_data = RequestService.get_request_by_id(request_id)

    if not request_data:

        return jsonify({
            "error": "Request not found"
        }), 404

    # updated by codex: return friendly error response if AI/Ollama call fails
    try:
        analysis = AIService.analyze_request(request_data)
    except Exception as error:
        return jsonify({
            "error": f"AI analyze failed: {error}"
        }), 500

    return jsonify({
        "analysis": analysis
    })
