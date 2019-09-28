import os
import boto3
import pandas as pd

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

df_list = []

# List only objects that start with '2019/final_'
response = s3.list_objects(Bucket='gim-staging', Prefix='2019/final_')

for file in response['Contents']:
    # For each file in response load the object from s3
    obj = s3.get_object(Bucket='gim-staging', Key=file['Key'])
    # Load the object's Streaming Body with pandas
    obj_df = pd.read_csv(obj['Body'])
    # Append the resulting DataFrame to list
    df_list.append(obj_df)

# Concat all the Data Frames with pandas
df = pd.concat(df_list)

df.head()
