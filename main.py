import base64
import json
import os

from image_processor import ImageProcessor

def lambda_handler(event, context):
    """
    AWS Lambda handler function to process images using OpenAI's image analysis.

    This function is triggered by an AWS Lambda event, expecting an image in base64 
    encoded format and an optional location type parameter for image analysis context.
    It decodes the image, processes it using the ImageProcessor class, and returns the result.

    Parameters:
    - event (dict): Contains the data sent to the Lambda function during invocation.
        Expected keys:
        - 'base64_image': A base64 encoded string of the image to be analyzed.
        - 'location_type' (optional): A string specifying the context ('interior' or 'exterior') for image analysis.
    - context: AWS Lambda uses this parameter to provide runtime information to your handler.

    Returns:
    - dict: A response object containing:
        - 'statusCode': HTTP status code representing the result of the operation.
        - 'body': A JSON string containing the analysis results or error message.
        - 'headers': Dictionary containing response headers.

    The function handles different scenarios:
    - Successful analysis: Returns HTTP 200 with analysis results.
    - Analysis identified issues: Returns HTTP 403 with details about the issues.
    - Missing or invalid data: Returns HTTP 400 with an error message.
    - Any unexpected errors: Returns HTTP 500 with an error message.

    Environment Variables:
    - 'API_KEY': The API key for authenticating with the OpenAI service.

    Note: 
    - The API key must be set in the AWS Lambda environment variables.
    - The image_processor module must be properly configured and able to communicate with OpenAI's API.
    """
    
    
    try:
        base64_image = event.get('image')
        location_type = event.get('location_type', None)

        api_key = os.environ['OPENAI_API_KEY']
        processor = ImageProcessor(api_key)
        
        result = processor.process_image(base64_image, location_type)

        if result.get('http_status') == 200:
            del result['http_status']
            return {
                'statusCode': 200,
                'body': json.dumps(result),
                'headers': {'Content-Type': 'application/json'}
            }
        else:
            del result['http_status']
            return {
                'statusCode': 403,
                'body': json.dumps(result),
                'headers': {'Content-Type': 'application/json'}
            }
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Missing or invalid data: {str(e)}'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Unexpected error: {str(e)}'}),
            'headers': {'Content-Type': 'application/json'}
        }
