from flask import Blueprint, jsonify

# updated by codex: switched to package-safe imports
from api_time_machine.services.request_service import RequestService
from api_time_machine.services.replay_service import ReplayService
from api_time_machine.services.compare_service import CompareService

replay = Blueprint("replay", __name__)


@replay.route("/replay/<request_id>", methods=["GET"])
def replay_request(request_id):

    old_request = RequestService.get_request_by_id(request_id)

    if not old_request:

        return jsonify({
            "error": "Request not found"
        }), 404

    replay_response = ReplayService.replay_request(old_request)

    comparison = CompareService.compare_json(
        old_request.get("response"),
        replay_response.get("response", {})
    )

    return jsonify({
        "replay_response": replay_response,
        "comparison": comparison
    })
