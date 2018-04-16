import boto3

BUCKET = "mygirlfriend"
KEY = "4.jpg"
IMAGE_ID = KEY  # S3 key as ImageId
COLLECTION = "mycollection"


def index_faces(image_id=None, attributes=(), region="ap-southeast-2"):
    rekognition = boto3.client("rekognition")
    response = rekognition.index_faces(
        CollectionId = 'mycollection',
        Image={
            "S3Object": {
                "Bucket": "mygirlfriend",
                "Name": '4.jpg'
            }
        },

        ExternalImageId='Demo',
        DetectionAttributes=['DEFAULT'],
    )
    return response['FaceRecords']

print(index_faces('mygirlfriend,'))


for record in index_faces(BUCKET, KEY, COLLECTION):
    face = record['Face']
    # details = record['FaceDetail']
    print("Face ({}%)".format(face['Confidence']))
    print("  FaceId: {}".format(face['FaceId']))
    print("  ImageId: {}".format(face['ImageId']))
