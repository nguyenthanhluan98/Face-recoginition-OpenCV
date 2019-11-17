import numpy as np
import cv2 
import pickle
def recogFace():

	face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
	eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
	smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')


	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("./recognizers/train.yml")

	img_counter = 0

	labels = {"person_name": 1}
	with open("pickles/face-labels.pickle", 'rb') as f:
		og_labels = pickle.load(f)
		labels = {v:k for k,v in og_labels.items()}

	print("labels: ", labels)

	cap = cv2.VideoCapture(0)



	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.2, minNeighbors=5)
		for (x, y, w, h) in faces:
			#print(x,y,w,h)
			roi_gray = gray[y:y+h, x:x+w] #(ycord_start, yclscord_end)
			roi_color = frame[y:y+h, x:x+w]
			'''
			if(img_counter < 100):
				img_name = "images/luan/luan{}.png".format(img_counter)
				cv2.imwrite(img_name, roi_gray)
				print("count: ", img_counter)
				img_counter += 1
			'''
			# recognize? deep learned model predict keras tensorflow pytorch scikit learn
			id_, conf = recognizer.predict(roi_gray)

			print("conf: ", conf)

			if conf >= 40 and conf <= 85:
			#	print("id: ", id_)qqqqq
			#	print(labels[id_])
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = labels[id_]
				color = (230, 0, 38)
				stroke = 2
				cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
				return name

			

			color = (128, 255, 149) #BGR 0-255 
			stroke = 2
			end_cord_x = x + w
			end_cord_y = y + h
			cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
			
			#subitems = smile_cascade.detectMultiScale(roi_gray)
			#for (ex,ey,ew,eh) in subitems:
			#	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		# Display the resulting frame
		cv2.imshow('frame',frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break



	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
