import os
import boto3

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

# List only objects that start with '2019/final_'
response = s3.list_objects(
    Bucket='gim-staging', Prefix='2019/final_')

# Iterate over the objects
for obj in response['Contents']:
    # Give each object ACL of public-read
    s3.put_object_acl(Bucket='gim-staging',
                      Key=obj['Key'],
                      ACL='public-read')

    # Print the Public Object URL for each object
    print("https://{}.s3.amazonaws.com/{}".format('gim-staging', obj['Key']))