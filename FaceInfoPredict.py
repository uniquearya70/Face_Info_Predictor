
"""
Created on Fri Jun 22 13:00:10 2018

@author: arpitansh
"""
import cv2
import requests
#import matplotlib.pyplot as plt
#from PIL import Image
from io import BytesIO


subscription_key = "b063f3cbadc647f2af39154012aacab8"
assert subscription_key

face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

image_path = "/home/arpitansh/Desktop/testimg.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()

headers = {
     'Ocp-Apim-Subscription-Key':subscription_key,
     'Content-Type': 'application/octet-stream'
     }

params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,smile,' + 
    'emotion,hair,makeup,accessories'
    }

response = requests.post(
        face_api_url, headers=headers, params=params, data=image_data
        )


analysis = response.json()
print(analysis)



