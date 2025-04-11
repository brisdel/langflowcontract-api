from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "ed6c45f6-6029-47a5-a6ee-86d7caf24d60"
FLOW_ID = "da053891-67b1-449f-9f2e-6081bb8c6cc6"

@app.post("/query")
async def query(message: str):
    url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('APPLICATION_TOKEN')}"
    }
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))