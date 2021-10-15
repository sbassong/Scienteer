from dotenv import load_dotenv
import os
import boto3


S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")
S3_REGION = os.getenv("S3_REGION")

s3_client = boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET, region_name=S3_REGION)


def upload_file(file, acl='public-read'):
  try:
    uploaded = s3_client.upload_fileobj(file, S3_BUCKET, file.filename, ExtraArgs={
      "ACL": acl,
      "ContentType": file.content_type
    })
    return "https://d1jgdfywsic76t.cloudfront.net/{filename}".format(filename=file.filename)
  except:
    print('Upload Failed')







