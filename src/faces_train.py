import cv2
import os
import numpy as np
from PIL import Image
import pickle

def train():
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	image_dir = os.path.join(BASE_DIR, "images")

	face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
	recognizer = cv2.face.LBPHFaceRecognizer_create()

	current_id = 0
	label_ids = {}
	y_labels = []
	x_train = []

	for root, dirs, files in os.walk(image_dir):
		for file in files:
			if file.endswith("png") or file.endswith("jpg"):
				path = os.path.join(root, file)
				label = os.path.basename(root).replace(" ", "-").lower()
				#print(label, path)
				if not label in label_ids:
					label_ids[label] = current_id
					current_id += 1
				id_ = label_ids[label]
				#print(label_ids)
				#y_labels.append(label) # some number
				#x_train.append(path) # verify this image, turn into a NUMPY arrray, GRAY
				pil_image = Image.open(path).convert("L") # grayscale

				width, height = pil_image.size
				
				
				if(width > 300 or height > 300):
					size = (300, 300)
					pil_image = pil_image.resize(size, Image.ANTIALIAS)
				#width1, height1 = pil_image.size
				#print("after width: " , width1, "height: ", height1)
				

			#	size = (550, 550)
			#	final_image = pil_image.resize(size, Image.ANTIALIAS)
				image_array = np.array(pil_image, "uint8")

				#faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
				faces = face_cascade.detectMultiScale(image_array)

				for (x,y,w,h) in faces:
					roi = image_array[y:y+h, x:x+w]
					x_train.append(roi)
					y_labels.append(id_)
					
				


	with open("pickles/face-labels.pickle", 'wb') as f:
		pickle.dump(label_ids, f)

	recognizer.train(x_train, np.array(y_labels))
	recognizer.save("recognizers/train.yml")