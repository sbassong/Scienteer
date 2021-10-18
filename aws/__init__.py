import boto3
from dotenv import load_dotenv
import os


S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")
S3_REGION = os.getenv("S3_REGION")

s3 = boto3.client('s3', aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET, region_name=S3_REGION)


def upload(file, acl='public-read'):
  try:
    uploaded = s3.upload_fileobj(file, S3_BUCKET, file.filename, ExtraArgs={
      "ACL": acl,
      "ContentType": file.content_type,
      
    })
    return "https://{bucket}.s3.amazonaws.com/{filename}".format(bucket=S3_BUCKET, filename=file.filename)
    # return "https://d1jgdfywsic76t.cloudfront.net/{filename}".format(filename=file.filename)
  except:
    print('Upload Failed')







