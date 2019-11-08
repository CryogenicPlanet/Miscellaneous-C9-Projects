import requests

url = "http://stonehill-server.bkmodding.c9users.io/postreq"

import cv2
import time
size = 4
webcam = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0) #Flip to act as a mirror

    mini = cv2.resize(im, (im.shape[1] / size, im.shape[0] / size))

    faces = classifier.detectMultiScale(mini)

    for f in faces:
        print"Hello"
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
        #Save just the cropped face
        sub_face = im[y:y+h, x:x+w]
        FaceFileName = "face_" + str(y) + ".jpg"
        cv2.imwrite(FaceFileName, sub_face)
        # Post the cropped face
        files = {'media': open(FaceFileName, 'rb')}
        headers = {
            'Content-Type': "multipart/form-data",
            'accept': "application/json",
            'apikey': "API0KEY0"
            }
        response = requests.post(url, files=files)

        print(response.text)
        time.sleep(5)
    # Show the image
    cv2.imshow('Face detected',   im)
    key = cv2.waitKey(10)
    # if Esc key is press then break out of the loop 
    #if key == 27: #Esc key
    #break
