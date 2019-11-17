# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import faces_train
import faces

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 124)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(160, 60, 75, 23))
        self.btnLogin.setObjectName("btnLogin")
        self.labelUserName = QtWidgets.QLabel(self.centralwidget)
        self.labelUserName.setGeometry(QtCore.QRect(30, 20, 81, 20))
        self.labelUserName.setObjectName("labelUserName")
        self.btnCancel = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(230, 60, 75, 23))
        self.btnCancel.setObjectName("btnCancel")
        self.txtName = QtWidgets.QTextEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(120, 20, 121, 21))
        self.txtName.setObjectName("txtName")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(0, 60, 75, 23))
        self.btnRegister.setObjectName("btnRegister")
        self.btnTrainingData = QtWidgets.QPushButton(self.centralwidget)
        self.btnTrainingData.setGeometry(QtCore.QRect(80, 60, 75, 23))
        self.btnTrainingData.setObjectName("btnTrainingData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.labelUserName.setText(_translate("MainWindow", "Input your name"))
        self.btnCancel.setText(_translate("MainWindow", "Cancel"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.btnTrainingData.setText(_translate("MainWindow", "Training data"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.takePictures)
        self.btnLogin.clicked.connect(self.recognizerFace)
        self.btnTrainingData.clicked.connect(self.trainingData)
        self.btnCancel.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()
    def trainingData(self):
        faces_train.train()
        print("Training data success")
    def recognizerFace(self):
        QtWidgets.QMessageBox.about(self, "Infor login", str(faces.recogFace()) + "login success")
    '''
    @QtCore.pyqtSlot()
    def writeHello(self):
        self.firstLineEdit.setText('Hello')
    '''
    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
    def takePictures(self):
        self.close()
        
        userName = self.txtName.toPlainText()

        # Start capturing video
        cap = cv2.VideoCapture(0)

        # Detect object in video stream using Haarcascade Frontal Face
        face_detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

   
        count = 0

        self.assure_path_exists("images/" + str(userName) + "/")


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
              
                img_name = "images/" + str(userName) + "/" + str(count) + ".jpg"
                print("path: ", img_name)
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
            elif count > 100:
                break

        # Stop video
        cap.release()

        # Close all started windows
        cv2.destroyAllWindows()




class MyDialog(QtWidgets.QDialog):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 200)
        self.myButton = QtWidgets.QPushButton("Write something")
        # When I click the myButton, I want it to change the text of MainWindow lineEdit
        self.myButton.clicked.connect(self.clicked)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.myButton)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("BEM Analysis for propellers")
    w.show()
    sys.exit(app.exec())
'''
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip("hello")
    



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.takePictures)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
    def printMessage(self):
        print("Hello world")

   
    def takePictures(self):
        
        def assure_path_exists(path):
            dir = os.path.dirname(path)
            if not os.path.exists(dir):
                os.makedirs(dir)
        vid_cam = cv2.VideoCapture(0)

        # Detect object in video stream using Haarcascade Frontal Face
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # For each person, one face id
        face_id = 1

        # Initialize sample face image
        count = 0

        assure_path_exists("dataset/" + str(face_id) + "/")

        # Start looping
        while(True):

            # Capture video frame
            _, image_frame = vid_cam.read()

            # Convert frame to grayscale
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # Detect frames of different sizes, list of faces rectangles
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            # Loops for each faces
            for (x,y,w,h) in faces:

                # Crop the image frame into rectangle
                cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            
                # Increment sample face image
                count += 1

                # Save the captured image into the datasets folder
                cv2.imwrite("dataset/" + str(face_id) + "/" + str(count) + ".jpg", gray[y:y+h,x:x+w])

                # Display the video frame, with bounded rectangle on the person's face
                cv2.imshow('frame', image_frame)

            # To stop taking video, press 'q' for at least 100ms
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            # If image taken reach 100, stop taking video
            elif count > 5:
                break

        # Stop video
        vid_cam.release()

        # Close all started windows
        cv2.destroyAllWindows()

import sys
app = QtWidgets.QApplication(sys.argv); 
MainWindow = QtWidgets.QMainWindow(); 
ui = Ui_MainWindow()
ui.setupUi(MainWindow); 
MainWindow.show(); 
app.exec_()
'''