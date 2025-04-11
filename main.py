   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   import requests
   import os

   app = FastAPI()

   BASE_API_URL = "https://api.langflow.astra.datastax.com"
   LANGFLOW_ID = "ed6c45f6-6029-47a5-a6ee-86d7caf24d60"
   FLOW_ID = "da053891-67b1-449f-9f2e-6081bb8c6cc6"

   class QueryRequest(BaseModel):
       message: str

   @app.post("/query")
   async def query(request: QueryRequest):
       url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
       headers = {
           "Content-Type": "application/json",
           "Authorization": f"Bearer {os.getenv('APPLICATION_TOKEN')}"
       }
       payload = {
           "input_value": request.message,
           "output_type": "chat",
           "input_type": "chat"
       }
       try:
           response = requests.post(url, json=payload, headers=headers)
           response.raise_for_status()
           return response.json()
       except requests.exceptions.RequestException as e:
           raise HTTPException(status_code=500, detail=str(e))