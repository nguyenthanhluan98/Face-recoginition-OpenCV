####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
import cv2
import os

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Start capturing video
cap = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

# For each person, one face id
face_id = 1

# Initialize sample face image
count = 0

#assure_path_exists("dataset/")

# Start looping
while(True):

    # Capture video frame
    _, image_frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y: y + h, x: x + w]


        # Increment sample face image
      

        # Crop the image frame into rectangle
        color = (128, 255, 149)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(image_frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

        count += 1

        img_name = "images/luan/luan{}.png".format(count)
        cv2.imwrite(img_name, roi_gray)

        print("takes picture: ", count)

        # Save the captured image into the datasets folder
       # cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])


        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count > 200:
        break

# Stop video
cap.release()

# Close all started windows
cv2.destroyAllWindows()
