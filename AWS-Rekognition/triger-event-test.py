import boto3

client = boto3.client('rekognition')
s3 = boto3.resource('s3')
bucket = s3.Bucket('test-face-detect')
for obj in bucket.objects.all():
    print(obj.key)


def search_by_image(bucket_name, key):
    response = client.search_faces_by_image(
        CollectionId='mycollection',
        Image={
            # 'Bytes': b'bytes',
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key,
            }
        },
        MaxFaces=123,
        FaceMatchThreshold=50
    )
    return response['FaceMatches']


def lambda_handler(event, context):
    # Get the object from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']  # .encode('utf8')

    try:

        # Calls Amazon Rekognition IndexFaces API to detect faces in S3 object
        # to index faces into specified collection

        response = search_by_image(bucket_name, key)

        # Print response to console
        print(response)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket))
        raise e


'''   
def list(self):
    file_prefix = 'path/to/object/'
    bucket = self.session().resource('s3').Bucket(bucket_name)
    return [obj.key for obj in bucket.objects.filter(Prefix=file_prefix)]

#from there you can:
boto3.resource('s3').Object(bucket_name, s3_obj_key).get()['Body'].read()
'''
