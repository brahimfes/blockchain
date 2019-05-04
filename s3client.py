import boto3
import botocore
import json

AWS_ACCESS_KEY_ID = 'AKIAIMYSTA2Z4UPR5N2A'
AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'its2019'
key_object = 'data.json'

s3 = boto3.resource(
    's3',
    aws_access_key_id='AKIAIMYSTA2Z4UPR5N2A',
    aws_secret_access_key='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',
)

#s3.Bucket(bucket_name).put_object(Key='blockchain.json', Body='toto')

data = ''
try:
    obj = s3.Object(bucket_name, key_object)
    data = obj.get()['Body'].read()
    print(json.loads(data))
except botocore.exceptions.ClientError as e:
    print(e)