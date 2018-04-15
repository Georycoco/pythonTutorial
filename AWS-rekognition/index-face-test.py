import boto3

BUCKET = "mygirlfriend"
KEY = "4.jpg"
IMAGE_ID = KEY  # S3 key as ImageId
COLLECTION = "mycollection"


def index_faces(bucket, key, collection_id, image_id=None, attributes=(), region="ap-southeast-2"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.index_faces(
        Image={
            "S3Object": {
                "Bucket": "mygirlfriend",
                "Name": '4.jpg',
            }
        },
        CollectionId=collection_id,
        ExternalImageId=image_id,
        DetectionAttributes=attributes,
    )
    return response['FaceRecords']


for record in index_faces(BUCKET, KEY, COLLECTION, IMAGE_ID):
    face = record['Face']
    # details = record['FaceDetail']
    print("Face ({}%)".format(face['Confidence']))
    print("  FaceId: {}".format(face['FaceId']))
    print("  ImageId: {}".format(face['ImageId']))
