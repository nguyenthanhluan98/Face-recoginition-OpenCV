

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import faces_train
import faces
#from gui_diemdanh import Gui_DiemDanh

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
        #self.close()
        self.gui_diemdanh = QtWidgets.QWidget()
        self.ui = Gui_DiemDanh()
        self.ui.setupUi(self.gui_diemdanh)
        self.gui_diemdanh.show()
    def trainingData(self):
        faces_train.train()
        print("Training data success")
    def recognizerFace(self):
        QtWidgets.QMessageBox.about(self, "Infor login", str(faces.recogFace()) + "login success")
   
    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
    def takePictures(self):
        self.close()
        
        userName = self.txtName.toPlainText()

        cap = cv2.VideoCapture(0)

        face_detector = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
        count = 0

        self.assure_path_exists("images/" + str(userName) + "/")
        # Start looping
        while(True):

            _, image_frame = cap.read()

            # Convert frame to grayscale
            gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # Detect frames of different sizes, list of faces rectangles
            faces = face_detector.detectMultiScale(gray, 1.3, 5)

            # Loops for each faces
            for (x, y, w, h) in faces:
                roi_gray = gray[y: y + h, x: x + w]
                count += 1
              
                img_name = "images/" + str(userName) + "/" + str(count) + ".jpg"
                cv2.imwrite(img_name, roi_gray)

                print("takes picture: ", count)
                # Crop the image frame into rectangle
                color = (128, 255, 149)
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(image_frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
            cv2.imshow('frames', image_frame)
            # To stop taking video, press 'q' for at least 100ms
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

            # If image taken reach 100, stop taking video
            if count > 200:
                break

        # Stop video
        cap.release()
        # Close all started windows
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("Login form")
    w.show()
    sys.exit(app.exec())
