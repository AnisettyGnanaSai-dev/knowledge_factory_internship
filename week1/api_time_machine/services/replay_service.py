import requests


class ReplayService:

    @staticmethod
    def replay_request(request_data):

        endpoint = request_data.get("endpoint")
        method = request_data.get("method")
        request_body = request_data.get("request_body")

        # updated by codex: replay full external URL when available
        full_url = request_data.get("full_url") or f"http://127.0.0.1:5000{endpoint}"

        try:

            if method == "POST":

                response = requests.post(
                    full_url,
                    json=request_body
                )

            elif method == "GET":

                response = requests.get(full_url)

            elif method == "PUT":
                response = requests.put(full_url, json=request_body)

            elif method == "PATCH":
                response = requests.patch(full_url, json=request_body)

            elif method == "DELETE":
                response = requests.delete(full_url, json=request_body)

            else:

                return {
                    "error": "Method not supported"
                }

            # updated by codex: prefer JSON, fall back to plain text when response is not JSON
            try:
                replay_payload = response.json()
            except ValueError:
                print("ReplayService: non-JSON response received; returning text response.")
                replay_payload = response.text

            return {
                "status_code": response.status_code,
                "response": replay_payload
            }

        except Exception as e:

            return {
                "error": str(e)
            }
