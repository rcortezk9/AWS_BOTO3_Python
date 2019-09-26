import os
import boto3

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

# Get the list_buckets response
response = s3.list_buckets()

# Iterate over Buckets from .list_buckets() response
for bucket in response['Buckets']:
    # Print the Name for each bucket
    print(bucket['Name'])