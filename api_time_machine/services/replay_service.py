import requests


class ReplayService:

    @staticmethod
    def replay_request(request_data):

        endpoint = request_data.get("endpoint")
        method = request_data.get("method")
        request_body = request_data.get("request_body")

        full_url = f"http://127.0.0.1:5000{endpoint}"

        try:

            if method == "POST":

                response = requests.post(
                    full_url,
                    json=request_body
                )

            elif method == "GET":

                response = requests.get(full_url)

            else:

                return {
                    "error": "Method not supported"
                }

            return {
                "status_code": response.status_code,
                "response": response.json()
            }

        except Exception as e:

            return {
                "error": str(e)
            }