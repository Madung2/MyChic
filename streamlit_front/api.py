# streamlit_app/api.py
import requests
from dotenv import load_dotenv
import json
import os
import time
load_dotenv()
mid_token = os.getenv("MID_TOKEN")
HEADERS = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {mid_token}"
    }
def generate_design(prompt, option1, option2):
    url = "https://api.mymidjourney.ai/api/v1/midjourney/imagine"
    payload = {
        "prompt": prompt,
        "ref": f"{option1}-{option2}"
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    return response.json()

def get_design(messageId):
    print(messageId)
    url = f"https://api.mymidjourney.ai/api/v1/midjourney/message/{messageId}"
    # url = f"https://api.mymidjourney.ai/api/v1/midjourney/message/8a81b461-4717-49e9-98ae-292ad00131e7"    
    response = requests.get(url, headers=HEADERS)
    return response.json()

def check_design_status(message_id):
    while True:
        message = get_design(message_id)
        if 'status' in message and message['status'] != 'PROCESSING':
            return message
        time.sleep(1)  # 1초 대기

