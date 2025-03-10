import os
import boto3
from botocore.exceptions import NoCredentialsError, BotoCoreError
from werkzeug.utils import secure_filename

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Initialize S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_image_to_s3(file, user_id):
    """Uploads an image to AWS S3 and returns the file URL"""
    try:
        filename = secure_filename(file.filename)
        s3_key = f"user_{user_id}/{filename}" 

        s3.upload_fileobj(file, S3_BUCKET_NAME, s3_key)

        file_url = f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
        return {"file_url": file_url}
    
    except NoCredentialsError:
        return {"error": "AWS credentials not found"}, 500
    except BotoCoreError as e:
        return {"error": f"AWS Error: {str(e)}"}, 500
