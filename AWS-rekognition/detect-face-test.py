import boto3
import json


client = boto3.client('rekognition')
s3 = boto3.resource('s3')


def detect_face(bucket, key):
    print('start detecting...')
    response = client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
            }
        },
        Attributes=['DEFAULT']
    )

    print('Detected faces for ' + '01.jpg')
    return response


response = detect_face('awsreko', '01.jpg')
print(str(response))

for face in response['FaceDetails']:
    print('face found at...')
    bBox = face['BoundingBox']
    for key,value in bBox.items():
        print(key, value)


'''
for face in detect_faces('mygirlfriend', '2.jpg'):
    print("Face ({Confidence}%)".format(**face))

    # emotions
    for emotion in face['Emotions']:
        print("  {Type} : {Confidence}%".format(**emotion))

    # quality
    for quality, value in face['Quality'].iteritems():
        print("  {quality} : {value}".format(quality=quality, value=value))
    # facial features
    for feature, data in face.iteritems():
        if feature not in FEATURES_BLACKLIST:
            print("  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data))
'''

'''
for face in detect_faces['FaceDetails']:

    formatStr = '{gender} age {lowage}-{highage}',

    if face['Mustache']['Value'] and face['Beard']['Value']:
        formatStr += 'with beard and mustache,'
    elif face['Mustache']['Value']:
        formatStr += 'with mustache,'
    elif face['Beard']['Value']:
        formatStr += 'with beard,'

    if face['Sunglasses']['Value']:
        formatStr +='wearing a sunglasses,'
    elif face['Eyeglasses']['Value']:
        formatStr += 'wearing glasses,'

    formatStr += 'looks {emotion}'

    print(
        formatStr.format(
            gender = face['Gender']['Value'],
            lowage = face['AgeRange']['Low'],
            highage= face['AgeRange']['High'],
            emotion= face['Emotions'][0]['Type'].lower()
        )
    )
'''
