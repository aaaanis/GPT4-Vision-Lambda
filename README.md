# OpenAI GPT-4 Vision for AWS Lambda

This repository contains a Python application that utilizes OpenAI's GPT-4 Vision model to describe images. It's designed to be deployed as a function on AWS Lambda for serverless operation.

## Overview

The project is structured into three main files:

- `AI_VISION.py`: Defines the `OpenAIAnalyzer` class which handles communication with OpenAI's API to analyze images.
- `AI_IMAGEPROCESSOR.py`: Contains the `ImageProcessor` class that uses `OpenAIAnalyzer` to process the image data.
- `main.py`: The entry point for the AWS Lambda function that orchestrates the image processing.

## Requirements

- Python 3.8 or higher
- An OpenAI API key with access to the GPT-4 model

## Setup

1. Clone this repository.
2. Install the required Python packages:

pip install -r requirements.txt

3. Set your OpenAI API key as an environment variable:

4. Deploy the function to AWS Lambda.

## Usage

The Lambda function expects a base64-encoded image in the `event['body']`. Once invoked, it will return a description of the image provided.

## Deployment

You can deploy this function to AWS Lambda manually or by using infrastructure as code tools like AWS CloudFormation or Terraform.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

[MIT License](LICENSE)
