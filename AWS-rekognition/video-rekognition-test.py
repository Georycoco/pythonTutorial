import boto3
from pprint import pprint

BUCKET = 'fishing-video'
COLLECTION = "mycollection"

client = boto3.client('rekognition')


def start_face_detection():
    response = client.start_face_detection(
        Video={
            'S3Object': {
                'Bucket': 'fishing-video',
                'Name': '01.mp4',
                # 'Version': 'string'
            }
        },
        ClientRequestToken='string',
        NotificationChannel={
            'SNSTopicArn': 'arn:aws:sns:ap-southeast-2:523640935742:AmazonRekognition',
            'RoleArn': 'arn:aws:iam::523640935742:role/Rekognition'
        },
        FaceAttributes=['ALL'],
        JobTag='myJob'
    )
    return response['JobId']


def get_face_detection():
    getList = client.get_face_detection(
        JobId=start_face_detection().response['JobId'],
        # SortBy = 'INDEX' | 'TIMESTAMP'
    )
    return getList['']


pprint(get_face_detection())
