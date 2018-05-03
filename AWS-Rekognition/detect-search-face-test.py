import io
from PIL import Image
import boto3
from pprint import pprint

rekognition = boto3.client('rekognition')
s3 = boto3.resource('s3')
dynamodb = boto3.client('dynamodb')
faces_Position = [],
t = io.BytesIO()


def detect_face(bucket, key):
    print('start detecting...')
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            }
        },
        Attributes=['DEFAULT']
    )

    print('faces detected')
    return response['FaceDetails']


def search_face_by_image(faces_position):
    print('start face search by image.....')
    response = rekognition.search_face_by_image(
        CollectionId='mycollection',
        Image={
            'Bytes': faces_position,
        },
        MaxFaces=10,
        FaceMatchThreshold=70,
    )

    return response


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    image = Image.open(key)

    all_Faces = detect_face(bucket, key)
    i = 0
    for face in all_Faces:
        faces_Position = face['BoundingBox']
        print('face' + i + 'found at:')
        left = int(faces_Position['Left'])
        top = int(faces_Position['Top'])
        right = int(faces_Position['Width'])
        bottom = int(faces_Position['Height'])

        face_detected = image.crop((left, top, right, bottom))
        t = io.BytesIO()
        face_detected.save(t, format='JPG')
        face_detected_binary = t.getvalue()
        i += i

        response = search_face_by_image(faces_Position=face_detected_binary)
        pprint(response)

        if len(response['FaceMatches']) > 0:
            print('Coordinates', faces_Position)

            for match in response['FaceMatches']:
                print(match['Face']['FaceId'], match['Face']['Similarity'], match['Face']['Confidence'])
