from database.mongo_connection import request_collection
from datetime import datetime


class RequestService:

    @staticmethod
    def save_request(data):

        request_data = {
            "endpoint": data.get("endpoint"),
            "method": data.get("method"),
            "request_body": data.get("request_body"),
            "response": data.get("response"),
            "status_code": data.get("status_code"),
            "timestamp": datetime.now()
        }

        result = request_collection.insert_one(request_data)

        return str(result.inserted_id)

    @staticmethod
    def get_all_requests():

        requests = list(
            request_collection.find().sort("timestamp", -1)
        )

        for request in requests:
            request["_id"] = str(request["_id"])

        return requests

    @staticmethod
    def get_request_by_id(request_id):

        from bson import ObjectId

        request = request_collection.find_one({
            "_id": ObjectId(request_id)
        })

        if request:
            request["_id"] = str(request["_id"])

        return request