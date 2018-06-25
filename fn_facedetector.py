#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:52:16 2018

@author: arpitansh
"""

import cv2
import requests
from os.path import join, dirname
from dotenv import load_dotenv
import os



def Photo_Capture():
    cap = cv2.VideoCapture(0)
    while True:
  
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('image',frame)
            
        
        k = cv2.waitKey(1)
        # save frame as JPEG file if s is hit
        if k%256 == 115:
            cv2.imwrite("test_image.jpg", frame) 
            cap.release()
            cv2.destroyAllWindows()
            return 1
        
        # exit if Escape is hit
        if k%256 == 27:
            cap.release()
            cv2.destroyAllWindows()                  
            return 0

    
 
def Collect_Face_Info():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    subscription_key = os.getenv('key')
    

    face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

    image_path = "test_image.jpg"  # Set the image path  

    # Read the image into a byte array
    image_data = open(image_path, "rb").read()

    headers = {
         'Ocp-Apim-Subscription-Key':subscription_key,
         'Content-Type': 'application/octet-stream'
         }

    params = {
        'returnFaceId': 'True',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,smile,' + 
        'emotion,hair,makeup,accessories'
        }
    try:
        

        response = requests.post(
                face_api_url, headers=headers, params=params, data=image_data
                )

        analysis = response.json()
        return analysis
    
    except requests.exceptions.RequestException as err:
        print('Connection Error',err)
    except requests.exceptions.ConnectionError as errc:
        print('Connection Error',errc)
    except requests.exceptions.ConnectTimeout as errt:
        print('Time out',errt)
    except requests.exceptions.HTTPError as errh:
        print('HTTP err',errh)
    return None
    
    
def Print_Data(analysis):
    count = 0
    for face in analysis:
        count += 1
    
        id = (face['faceId'])
        print('face id:',id)
        print('Gender:',face['faceAttributes']['gender'])
        print('Age:',face['faceAttributes']['age'])
    
        check_emo =0
        rslt_emotion = " "
        for emotion in face['faceAttributes']['emotion']:
            if face['faceAttributes']['emotion'][emotion] > check_emo:
                check_emo = face['faceAttributes']['emotion'][emotion]
                rslt_emotion = emotion
        print('Emotion: ',rslt_emotion,'(',check_emo*100,'%',')') 
        

# Displaying Captured Image      
    image = cv2.imread('test_image.jpg')  # Set the image path
    cv2.imshow('Captured Image',image)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

    
  
    
def main():
    flag = Photo_Capture()
    if flag:
        analysis = Collect_Face_Info()
        if analysis:
            Print_Data(analysis)
            
            
main()
 
