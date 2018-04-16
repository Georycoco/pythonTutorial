import boto3

s3 = boto3.resource('s3')
bucket = s3.bucket('mygirlfriend')
objects = ['']
for obj in bucket.object.all():
        objects += obj.key
        print(obj.key)

client = boto3.client('rekognition')




response = client.search_faces_by_image(
    CollectionId='string',
    Image={
        'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 'string',
            'Name': 'string',
            'Version': 'string'
        }
    },
    MaxFaces=123,
    FaceMatchThreshold=...
)