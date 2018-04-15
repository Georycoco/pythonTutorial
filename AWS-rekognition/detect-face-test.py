import boto3
from pprint import pprint

BUCKET = 'mygirlfriend'
KEY = '1.jpg'
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")


def detect_faces(bucket, key):
    rekognition = boto3.client("rekognition", 'ap-southeast-2')
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": 'mygirlfriend',
                "Name": '2.jpg',
            }
        },
        Attributes=['DEFAULT'],
    )

    return response['FaceDetails']


pprint(detect_faces('mygirlfriend','1,jpg'))

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
