#final deployment vision
import boto3
from django.conf import settings


client = boto3.client('rekognition', settings.AWS_SETTINGS['region_name'], aws_access_key_id = settings.AWS_SETTINGS['aws_access_key_id'],
    aws_secret_access_key = settings.AWS_SETTINGS['aws_secret_access_key'])


def rekognition_check_face(file):
    is_face_detected = False
    response = client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': settings.AWS_SETTINGS['students-images-bucket'],
                'Name': file
            }
        }
    )
    print(response)
    if (not response['FaceDetails']):
        is_face_detected = False
    else:
        is_face_detected = True
    return is_face_detected


def rekognition_delete_face(face_id):
    response = client.delete_faces(CollectionId='default_collection' , FaceIds=[face_id])
    print(response)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return True


def rekognition_add_face(file, student_id):
    print(file, student_id)
    response = client.index_faces(
        CollectionId='default_collection',
        Image={
            'S3Object': {
                'Bucket': settings.AWS_SETTINGS['students-images-bucket'],
                'Name': file
            }
        },
        ExternalImageId=str(student_id),
        DetectionAttributes=[
            'ALL',
        ]
    )
    return response['FaceRecords'][0]['Face']['FaceId']


def rekognition_face_match(file):
    response = client.search_faces_by_image(CollectionId='default_collection',
        Image={
            'S3Object': {
                'Bucket': settings.AWS_SETTINGS['students-images-bucket'],
                'Name': file
            }
        },
        MaxFaces=5,
        FaceMatchThreshold=85
    )
    if (not response['FaceMatches']):
        is_face_matched = False
    else:
        is_face_matched = True

    return is_face_matched, response