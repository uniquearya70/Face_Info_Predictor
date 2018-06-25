import cv2
import requests



def Photo_Capture():
    cap = cv2.VideoCapture(0)
    while True:
  
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('image',frame)
            
        # save frame as JPEG file
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("test_image.jpg", frame) 
            break
        
        # exit if Escape is hit
        if cv2.waitKey(1) == 27:                    
            break
  
    cap.release()
    cv2.destroyAllWindows()
    return 1
    
 
def Collect_Face_Info():
    subscription_key = "b063f3cbadc647f2af39154012aacab8"
    assert subscription_key

    face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"

    image_path = "/home/arpitansh/Desktop/python basic code/test_image.jpg"  

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

    response = requests.post(
            face_api_url, headers=headers, params=params, data=image_data
            )

    analysis = response.json()
    return analysis
    
    
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
    image = cv2.imread('/home/arpitansh/Desktop/python basic code/test_image.jpg')
    cv2.imshow('Captured Image',image)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()

    
  
    
def main():
    Photo_Capture()
    if True:
        analysis = Collect_Face_Info()
        if analysis:
            Print_Data(analysis)
            
            
main()
 
