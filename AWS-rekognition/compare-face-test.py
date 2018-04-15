import boto3
from pprint import pprint

BUCKET = "mygirlfriend"
KEY_SOURCE = "1.jpg"
KEY_TARGET = "2.jpg"


def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="ap-southeast-2"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.compare_faces(
        SourceImage={
            "S3Object": {
                "Bucket": 'mygirlfriend',
                "Name": '1.jpg',
            }
        },
        TargetImage={
            "S3Object": {
                "Bucket": 'mygirlfriend',
                "Name": '2.jpg',
            }
        },
        SimilarityThreshold=threshold,
    )
    return response['SourceImageFace'], response['FaceMatches']


source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)

# the main source face
pprint("Source Face ({Confidence}%)".format(**source_face))

# one match for each target face
for match in matches:
    print("Target Face ({Confidence}%)".format(**match['Face']))
    print("  Similarity : {}%".format(match['Similarity']))
