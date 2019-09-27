import os
import boto3

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

s3.upload_file(
  Filename='./final_report.csv',
  Key='2019/final_report_2019_02_20.csv',
  Bucket='gim-staging',
  ExtraArgs={
    'ACL': 'public-read'})