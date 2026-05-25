import logging
import os

# Create logs folder automatically
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_request(data):

    logging.info(f"""
Endpoint: {data.get("endpoint")}
Method: {data.get("method")}
Request Body: {data.get("request_body")}
Status Code: {data.get("status_code")}
Response: {data.get("response")}
""")