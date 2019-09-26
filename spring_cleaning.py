import os
import boto3

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

# Create boto3 client to S3
s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

# List only objects that start with '2018/final_'
response = s3.list_objects(Bucket='gid-staging',
                           Prefix='2018/final_')

# Iterate over the objects
if 'Contents' in response:
    for obj in response['Contents']:
        # Delete the object
        s3.delete_object(Bucket='gid-staging', Key=obj['Key'])

# Print the keys of remaining objects in the bucket
response = s3.list_objects(Bucket='gid-staging')

for obj in response['Contents']:
    print(obj['Key'])
