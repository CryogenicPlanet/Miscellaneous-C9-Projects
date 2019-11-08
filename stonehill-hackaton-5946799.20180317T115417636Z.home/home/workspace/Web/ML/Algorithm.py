
import cv2
import os
from os import listdir
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "C:\\Users\\rithv\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'D:/FaceRecog/train3/rahul/'

def get_images_and_labels(path):
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in listdir(path):
         # Read the image and convert to grayscale
        image_pil = Image.open(path + image_path).convert('L')

         # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        image = cv2.resize(image, (500, 500))
         # Get the label of the image
        nbr = 0
         #nbr=int(''.join(str(ord(c)) for c in nbr))
         # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
         # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
             images.append(image[y: y + h, x: x + w])
             labels.append(nbr)
             cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
             cv2.waitKey(10)
     # return the images list and labels list
    return images, labels


images, labels = get_images_and_labels(path)

path = 'D:/FaceRecog/train3/baala/'

def get_images_and_labels2(path):
    images2 = []
    # labels will contains the label that is assigned to the image
    labels2 = []
    for image_path in listdir(path):
         # Read the image and convert to grayscale
        image_pil = Image.open(path + image_path).convert('L')
         # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        image = cv2.resize(image, (500, 500))
         # Get the label of the image
        nbr = 1
         #nbr=int(''.join(str(ord(c)) for c in nbr))
         # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
         # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
             images2.append(image[y: y + h, x: x + w])
             labels2.append(nbr)
             cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
             cv2.waitKey(10)
     # return the images list and labels list
    return images2, labels2


images2, labels2 = get_images_and_labels2(path)
print(images, labels)
print("**************")
print(images2, labels2)

final_images = images+images2
final_labels = labels+labels2


recognizer.train(final_images, np.array(final_labels))
recognizer.save('trainer.yml')
print("Finished!")
cv2.destroyAllWindows()
