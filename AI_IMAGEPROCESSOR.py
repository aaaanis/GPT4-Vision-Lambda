import json
from AI_VISION import OpenAIAnalyzer

class ImageProcessor:
    def __init__(self, api_key):
        self.analyzer = OpenAIAnalyzer(api_key)

    def process_image_data(self, image_bytes):
        analysis_result = self.analyzer.analyze_image(image_bytes)
        text = analysis_result['choices'][0]['message']['content']
        content_data = json.loads(text.strip('```json\n').rstrip('\n```'))
        return content_data
