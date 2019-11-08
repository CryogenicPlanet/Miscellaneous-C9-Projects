import cv2
from keras.models import load_model
import numpy as np

img_width, img_height = 150, 150
model = load_model("model_HE.h5")
model.load_weights('weights_HE.h5')

img_width, img_height = img_width, img_height
img = cv2.imread('images\\test.jpg')
img = cv2.resize(img, (img_width, img_height))
img = img.reshape(img_width, img_height, 3)
predict = model.predict_classes(img[None, :, :, :]/255)
print(predict)

