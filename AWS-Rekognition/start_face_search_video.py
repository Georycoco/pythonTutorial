import urllib
import boto3
import time
import sys
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
    print('start read get face search...')
    response = client.get_face_search(
        JobId=jobID,
        MaxResults=5,
        # SortBy='TIMESTAMP',
    )
    print('get_face_search done')
    print(str(response))
    return response


def read_job_status(jobId):
    # response = get_face_search(jobId)
    # time.sleep(0.5)

    while True:
        # get_face_search(jobID=jobId)
        response = get_face_search(jobID=jobId)
        if response['JobStatus'] == 'IN_PROGRESS':
            print('in progress')
            print('here is response 2: ' + str(response))
            sys.stdout.flush()
            time.sleep(5)
            continue


        elif response['JobStatus'] == 'SUCCEEDED':
            print('Succeeded..')
            similarity_list = []
            # timeStamp = response['Persons'][0]['Timestamp']
            # similarity = response['Persons'][0]['FaceMatches']['Similarity']
            # print('timestamp: {}'.format(response['Timestamp']))
            # faceId = response['Persons'][0]['FaceMatches']['Face']['FaceId']
            print('face match at...')
            for face in response['Persons']:
                similarity = face['FaceMatches'].get('Similarity')
                similarity_list.append(similarity)
            print(similarity_list)
            break

        elif response['JobStatus'] == 'FAILED':
            print('Return job detail failed...')
            break

        else:
            print('Error....Return job detail failed')
            break


def lambda_handler(event, context):
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(
        event['Records'][0]['s3']['object']['key'].encode('utf8'))

    jobId = start_face_search(bucket, key)
    print('jobId1 is: ' + str(jobId))
    sys.stdout.flush()
    time.sleep(5)

    print('starts get face search: ')
    read_job_status(jobId)
    # detail = get_face_search(jobId)
    # print(str(detail))


'''
    for status in get_face_search(jobId):
        #response = get_face_search(jobID = jobId)
        pprint('here is response 2: ' + str(response))

        if status['JobStatus'] == 'IN_PROGRESS':
            print('in progress')
            continue

        elif status['JobStatus'] == 'SUCCEEDED':
            time = response['Persons'][0]['Timestamp']
            # similarity = response['Persons'][0]['Similarity']
            # print('timestamp: {}'.format(response['Timestamp']))
            faceId = response['FaceMatches'][0]['Face']['FaceId']

            print(str(time))
            # print(similarity)
            print(faceId)
            break

        elif status['JobStatus'] == 'FAILED':
            print('Return job failed')

        else:
            print('error')

    return response
'''


