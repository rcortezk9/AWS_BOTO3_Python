import os
import boto3
import pandas as pd

AWS_KEY_ID = os.environ.get('AWS_KEY_ID')
AWS_SECRET = os.environ.get('AWS_SECRET')

s3 = boto3.client('s3', region_name='us-east-1',
                  aws_access_key_id=AWS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET)

services_df = []

# Generate an HTML table with no border and selected columns
services_df.to_html('./services_no_border.html',
                    # Keep specific columns only
                    columns=['service_name', 'link'],
                    # Set border
                    border=0)

# Generate an html table with border and all columns.
services_df.to_html('./services_border_all_columns.html',
                    border=1)
