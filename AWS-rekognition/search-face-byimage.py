from __future__ import print_function
import boto3
import urllib

dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')


def search_faces_by_image(bucket, key):
    response = rekognition.search_faces_by_image(
        CollectionId='mycollection',
        Image={
            # 'Bytes': b'bytes',
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            }
        },
        MaxFaces=5,
        FaceMatchThreshold=50,
    )
    return response


def update_dytable(tablename, faceID, similarity):
    response = dynamodb.put_item(
        TableName=tablename,
        Item={
            'faceID': {'S': faceID},
            # 'Confidence':{'f': confidence},
            'Similarity': {'S': similarity},
        }
    )


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(
        event['Records'][0]['s3']['object']['key'].encode('utf8'))

    try:
        response = search_faces_by_image(bucket, key)

        faceId = response['FaceMatches'][0]['Face']['FaceId']
        # confidence = response['FaceRecords'][0]['Face']['Confidence']
        similarity = response['FaceMatches'][1]['Similarity']

        update_dytable('face_search', faceId,str(similarity))

        print(response)
        return response


    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket))
        raise e


'''
for record in search_by_image():
    face = record['Face']
    print("Matched Face ({}%)".format(record['Similarity']))
    print("  FaceId : {}".format(face['FaceId']))
# print("  ImageId : {}".format(face['ExternalImageId']))
'''
