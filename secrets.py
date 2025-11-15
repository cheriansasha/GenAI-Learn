"""AWS Secrets Manager integration for API key retrieval."""

import boto3
from botocore.exceptions import ClientError

def get_secret():
    """Retrieve API keys from AWS Secrets Manager."""
    secret_name = "sasha/genai-learn"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return get_secret_value_response['SecretString']