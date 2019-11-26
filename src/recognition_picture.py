import numpy as np
import cv2
from matplotlib import pyplot as plt
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/train.yml")

img = cv2.imread("thiacm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
print("list name: ", labels)
count = 0

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    count+= 1
     #  print("luan", x, y, w, h)
    id_, conf = recognizer.predict(roi_gray)
    # img_name = "test{}.png".format(count)
    #  cv2.imwrite(img_name, gray[y:y+h, x:x+w])
    print("conf: ", conf)
    if conf < 140:
        print("id:", id_)
        font = cv2.FONT_HERSHEY_COMPLEX
        name = labels[id_]
        print("name: ", name)
        color = (230, 0, 38)
        stroke = 2 # độ dày
        cv2.putText(img, name, (x, y), font, 1, color,stroke, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()