
"""
Created on Fri Jun 22 13:00:10 2018

@author: arpitansh
"""
import cv2
import requests

# From line 14-29 Capturing and saving image from video 
cap = cv2.VideoCapture(0)

while True:
  
  ret, frame = cap.read()
  if ret == True:
      cv2.imshow('image',frame)
  if cv2.waitKey(1) & 0xFF == ord('s'):
      cv2.imwrite("test_image1.jpg", frame)     # save frame as JPEG file
      break
  if cv2.waitKey(1) == 27:                     # exit if Escape is hit
      break
 
  
cap.release()
cv2.destroyAllWindows()

# sending captured image to the microsoft cingitive and taking details 

subscription_key = "b063f3cbadc647f2af39154012aacab8"
assert subscription_key

face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

image_path = "/home/arpitansh/Desktop/python basic code/test_image1.jpg"  

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

analysis = response.json()
print(analysis)



