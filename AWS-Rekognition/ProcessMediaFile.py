import boto3
import os
import sys
import uuid
from PIL import Image, ImageOps

s3_client = boto3.client('s3')


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        thumb = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
        thumb.save(resized_path)


def lambda_handler(event, context):
    for record in event['Records']:
        bucket_input = record['s3']['bucket']['name']
        bucket_output = "output-bucket-name"

        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)

        s3_client.download_file(bucket_input, key, download_path)
        resize_image(download_path, upload_path)
        s3_client.upload_file(upload_path, bucket_output, key)
