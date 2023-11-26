import requests

"""
This module provides a class for interfacing with the OpenAI API to analyze images using a vision model. 
If a location_type is provided, it assess whether the image represent the interior or exterior of buildings and detects the presence of human faces or car license plates.
Else, it checks if the image does not contain any dangerous content.

Classes:
    OpenAIAnalyzer: Manages interactions with the OpenAI API for image analysis.

Attributes:
    API_URL (str): URL of the OpenAI API endpoint for chat completions.
    CONTENT_TYPE (str): The MIME type for the request header, indicating the format of the body sent to the API.
    MODEL (str): Identifier of the OpenAI GPT-4 vision model used for image analysis.

OpenAIAnalyzer:
    This class facilitates the sending of image data to the OpenAI API for analysis.

    Methods:
        __init__(api_key): Constructor that initializes the OpenAIAnalyzer with an API key.
        analyze_image(base64_image, location_type): Analyzes the given base64-encoded image. The method constructs a prompt to assess if the image looks like the specified 'location_type' (interior/exterior) of a mosque and whether it contains identifiable human faces or readable license plates. The analysis results are formatted as per the specified criteria.

Usage:
    An instance of OpenAIAnalyzer is created by passing an API key. The analyze_image method is used to send base64-encoded images to the OpenAI API. The method returns a JSON response containing the analysis results, which can include the validity of the image in the context of the specified criteria and reasons for any rejections.
"""


class OpenAIAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def analyze_image(self, base64_image, location_type):
        if location_type:
            prompt = f'Does this image look like the {location_type} of a building? And does it contain a human face that could be identifiable or a readable license plate? If everything is ok return me "valid" else return me the reasons inside this list ["PRESENCE_OF_FACES", "PRESENCE_OF_CAR_LICENCES", "WRONG_LOCATION"]. There can be multiple reasons. Always respect this output format.'
        else:
            prompt = f'Check if this image has safe content. If everything is ok return me "valid" else return me the reasons inside this list ["PRESENCE_OF_SEXUAL_CONTENT", "PRESENCE_OF_HATEFUL_CONTENT", "PRESENCE_OF_HARASSING_CONTENT", "PRESENCE_OF_VIOLENT_CONTENT", "PRESENCE_OF_GRAPHIC_CONTENT", "PRESENCE_OF_THREATENING_CONTENT", "PRESENCE_OF_POLITICAL_CONTENT"]. There can be multiple reasons. Always respect this output format.'        
        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
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
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=self.headers, json=payload)
        return response.json()
