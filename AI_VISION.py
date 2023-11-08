import base64
import requests

API_URL = "https://api.openai.com/v1/chat/completions"
CONTENT_TYPE = "application/json"
MODEL = "gpt-4-vision-preview"

class OpenAIAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": CONTENT_TYPE,
            "Authorization": f"Bearer {self.api_key}"
        }

    def analyze_image(self, image_bytes):
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        payload = {
            "model": MODEL,
            "messages": [
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": "Describe this image."
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                  }
                ]
              }
            ],
            "max_tokens": 300
        }
        response = requests.post(API_URL, headers=self.headers, json=payload)
        return response.json()
