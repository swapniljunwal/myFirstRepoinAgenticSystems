import json


api_response = '''{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}'''

data = json.loads(api_response)

request_id = data["id"]
status = data["status"]
text = data["result"]["text"]
confidence = data["result"]["confidence"]

print(f"Request ID: {request_id}")
print(f"Status: {status}")
print(f"Text: {text}")
print(f"Confidence: {confidence}")

if confidence < 0.9:
    print("Warning: Low confidence score!")

follow_up = {
    "id": request_id,
    "processed": True,
    "message": "Data processed successfully"
}

json_output = json.dumps(follow_up, indent=4)


with open("response.json", "w") as f:
    json.dump(follow_up, f, indent=4)

print("\nJSON saved to response.json")