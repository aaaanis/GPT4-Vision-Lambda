import json
import base64
import os
from AI_VISION import OpenAIAnalyzer
from AI_IMAGEPROCESSOR import ImageProcessor

def lambda_handler(event, context):
    api_key = os.environ['OPENAI_API_KEY']
    
    image_data = base64.b64decode(event['body'])
    
    processor = ImageProcessor(api_key)
    
    results = processor.process_image_data(image_data)
    
    response = {
        "statusCode": 200,
        "body": json.dumps(results),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    
    return response