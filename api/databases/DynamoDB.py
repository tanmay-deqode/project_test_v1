import boto3

from boto3 import ServiceResource


class DynamoDBClient:
    
    def initialize_db() -> ServiceResource:

        db = boto3.resource('dynamodb',
                            region_name='us-east-1',
                            aws_access_key_id=None,
                            aws_secret_access_key=None
                            )
        return db
