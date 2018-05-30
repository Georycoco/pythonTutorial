import urllib
import boto3
import time
import sys

client = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
face_match = []
similarity = []
faces = []
face_ID = []


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
            outcome = response['Persons']
            print('Succeeded..')
            first_level_exact(outcome)
            print('here is face match details...')
            print(face_match)
            second_level_exact(face_match)
            print('here is similarity...')
            print(similarity)
            print('here is face details...')
            print(faces)
            third_level_exact(faces)
            # print('here is faceID list:')
            # print(face_ID)
            print('here is faceId with similarity...')
            print(similarity)
            break

        elif response['JobStatus'] == 'FAILED':
            print('Return job detail failed...')
            break

        else:
            print('Error....Return job detail failed')
            break


def first_level_exact(dic):
    for item in dic:
        print('item found...')
        for k, v in item.items():
            print('Key:')
            print(k)
            print('Value:')
            print(v)
            if k == 'FaceMatches':
                face_match.extend(v)


def second_level_exact(dic):
    print('start exacting from face_match list............')
    print('-' * 30)
    for item in dic:
        print('item found.....')
        for k, v in item.items():
            print('Key:')
            print(k)
            print('Value:')
            print(v)
            if k == 'Similarity':
                similarity.append('Similarity:')
                similarity.append(v)
            elif k == 'Face':
                faces.append(v)


def third_level_exact(dic):
    i = 0
    print('start exacting from faces list............')
    print('-' * 30)
    for item in dic:
        print('item found.....')
        for k, v in item.items():
            print('Key:')
            print(k)
            print('Value:')
            print(v)
            if k == 'FaceId':
                face_ID.append('FaceId:')
                face_ID.append(v)
                similarity.insert(i,'FaceId:')
                i = i + 1
                similarity.insert(i,v)
                i = i + 3


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
    outcome = read_job_status(jobId)
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


