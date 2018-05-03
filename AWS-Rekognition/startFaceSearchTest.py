import urllib
import boto3
from pprint import pprint

client = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

def start_face_search():
    response = client.start_face_search(
        Video={
            'S3Object': {
                'Bucket': 'video-income-test',
                'Name': '01.mp4',
            }
        },
        #ClientRequestToken='string',
        FaceMatchThreshold=70,
        CollectionId='mycollection',
        NotificationChannel={
            'SNSTopicArn': 'arn:aws:sns:ap-southeast-2:747748137319:start-face-search',
            'RoleArn': 'arn:aws:iam::747748137319:role/FaceDetect',
        },
        #JobTag='string'
    )
    pprint(response)
    return response['JobId']

print(start_face_search())

'''
import urllib
import boto3
from pprint import pprint

client = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')

def start_face_search(bucket, key):
    print('starts face search: ')
    response = client.start_face_search(
        Video={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
                # 'Version': 'string'
            }
        },
        # ClientRequestToken='string',
        CollectionId='mycollection',
        NotificationChannel={
            'SNSTopicArn': 'arn:aws:sns:ap-southeast-2:747748137319:start-face-search',
            'RoleArn': 'arn:aws:iam::747748137319:role/FaceDetect',
        },
        FaceMatchThreshold=70,
        JobTag='myJob',
    )
    print('here is response 1: ' + str(response))
    return response['JobId']
    
    


def get_face_search(jobID):
    response = client.get_face_search(
        JobId=jobID,
        MaxResults=5,
        #SortBy='TIMESTAMP',
    )
    return response


def lambda_handler(event, context):
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(
        event['Records'][0]['s3']['object']['key'].encode('utf8'))

    jobId = start_face_search(bucket, key)
    print('jobId1 : ' + str(jobId))
    
    print('starts get face search: ')
    #jobID = jobId['JobId']
    #print('jobID2 is: ' + str(jobID))
    response = get_face_search(jobId)
    pprint('here is response 2: ' + str(response))
    
    
    time = response['Persons'][0]['Timestamp']
    #similarity = response['Persons'][0]['Similarity']
    #print('timestamp: {}'.format(response['Timestamp']))
    faceId = response['FaceMatches'][0]['Face']['FaceId']
    
    print(str(time))
    #print(similarity)
    print(faceId)

    return response


'''