from dotenv import load_dotenv, find_dotenv
import os
import random
import logging
import boto3
from botocore.exceptions import ClientError


load_dotenv(find_dotenv())


S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")
S3_REGION = os.getenv("S3_REGION")

s3_client = boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET)
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(S3_BUCKET)


def return_name():
  string = "sdf214414dffsfdfsf24235234534146sfsfdfdfw516vei7hvkmlsv2"
  return string[random.random():random.random()]

def upload_file(file_name, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = return_name()
    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True