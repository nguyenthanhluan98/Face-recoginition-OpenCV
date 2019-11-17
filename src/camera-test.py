import numpy as np
import cv2
from matplotlib import pyplot as plt
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/train.yml")

img = cv2.imread("thiacm.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
print("list name: ", labels)
count = 0

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
  #  roi_color = img[y:y+h, x:x+w]
    print(x, y, w, h)
    
   
      #  print("luan", x, y, w, h)
    id_, conf = recognizer.predict(roi_gray)
    #img_name = "images/luan/luanq{}.png".format(count)
    #cv2.imwrite(img_name, gray[y:y+h, x:x+w])


    print("conf: ", conf)
    if conf < 50:
        print("id:", id_)
        font = cv2.FONT_HERSHEY_COMPLEX
        name = labels[id_]
        print("name: ", name)
        color = (230, 0, 38)
        stroke = 2
        cv2.putText(img, name, (x, y), font, 1, color,stroke, cv2.LINE_AA)
   
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
   

   # for (ex,ey,ew,eh) in eyes:
        
      #  cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()