def build_analysis_prompt(request_data):

    prompt = f"""
You are an expert backend debugging engineer.

Analyze this API request and response.

Endpoint:
{request_data.get("endpoint")}

Method:
{request_data.get("method")}

Request Body:
{request_data.get("request_body")}

Response:
{request_data.get("response")}

Status Code:
{request_data.get("status_code")}

Explain:

1. What happened
2. Possible issue
3. Possible root cause
4. Suggested fix
5. Security concerns if any
"""

    return prompt