from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import QApplication, QDialog,QLabel,QWidget, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap,QImage, QBrush, QPalette
from PyQt5.uic import loadUi
from PIL import Image
import cv2
import pickle
import pandas as pd
from datetime import datetime



class Register(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(946, 590)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 40, 751, 230))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("#frame {border: 1px solid black}")

        self.lblImage = QtWidgets.QLabel(Dialog)
        self.lblImage.setGeometry(QtCore.QRect(50, 40, 751, 230))
       # self.lblImage.resize(300, 250)
        self.lblImage.setObjectName("lblImage")
        

        self.btnRecognitionFaces = QtWidgets.QPushButton(Dialog)
        self.btnRecognitionFaces.setGeometry(QtCore.QRect(840, 120, 75, 23))
        self.btnRecognitionFaces.setObjectName("btnRecognitionFaces")

        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(50, 290, 751, 230))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("#frame_2 {border: 1px solid black}")


        self.lblResultRecog = QtWidgets.QLabel(Dialog)
        self.lblResultRecog.setGeometry(QtCore.QRect(50, 290, 751, 230))
        self.lblResultRecog.setObjectName("lblResultRecog")

        self.originalImage = ''

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 16))
        self.label.setObjectName("label")

        self.btnChoosePicture = QtWidgets.QPushButton(Dialog)
        self.btnChoosePicture.setGeometry(QtCore.QRect(840, 60, 75, 23))
        self.btnChoosePicture.setObjectName("btnChoosePicture")

        self.btnDiemDanh = QtWidgets.QPushButton(Dialog)
        self.btnDiemDanh.setGeometry(QtCore.QRect(840, 160, 75, 23))
        self.btnDiemDanh.setObjectName("btnDiemDanh")


        self.retranslateUi(Dialog)

        self.btnChoosePicture.clicked.connect(self.openFileNameDialog)
        self.btnDiemDanh.clicked.connect(self.diemDanh)
        self.btnRecognitionFaces.clicked.connect(self.recogImage)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.arrListSVCoMat = []
       

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnRecognitionFaces.setText(_translate("Dialog", "Nhan dang"))
        self.label.setText(_translate("Dialog", "GUI DIEM DANH"))
        self.btnChoosePicture.setText(_translate("Dialog", "Chon anh"))
        self.btnDiemDanh.setText(_translate("Dialog", "Diem danh"))
    def openFileNameDialog(self, Dialog):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
    
            pixmap = QPixmap(fileName)
            self.originalImage = fileName

            self.lblImage.setPixmap(pixmap.scaled(self.frame.size()))
    def recogImage(self, Dialog):
        face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("./recognizers/train.yml")

        img = cv2.imread(self.originalImage)
            
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
            #print("conf: ", conf)
            #if conf < 140:
            print("id:", id_)
            font = cv2.FONT_HERSHEY_COMPLEX
            name = labels[id_]
            self.arrListSVCoMat.append(id_)
            print("name: ", name)
            color = (230, 0, 38)
            stroke = 2 # độ dày
            cv2.putText(img, name, (x, y), font, 1, color,stroke, cv2.LINE_AA)

       # self.lblResultRecog.setPixmap(img)
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)                                           
        QImg = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)
        # test show orinal image

        pixmap = QPixmap.fromImage(QImg)
        self.lblResultRecog.setPixmap(pixmap.scaled(self.frame_2.size()))

        
    def diemDanh(self):
        data = pd.read_excel(r"diemdanh.xlsx")
        df = pd.DataFrame(data)
        newColumn = pd.Series(("N" for i in range(len(data))))

      
        
        for i in range(len(self.arrListSVCoMat)):
            for j in range(len(data)):
                if data["MSSV"][j] == self.arrListSVCoMat[i]:
                    newColumn[i] = "Y"
                    break
                
        today = datetime.now()
        d1 = today.strftime("%d/%m/%Y %H:%M:%S")
        data.insert(len(df.columns), d1, newColumn)     # get column next   
        writer = pd.ExcelWriter(r"diemdanh.xlsx", engine="xlsxwriter")
        data.to_excel(writer, index=False)
        writer.save()
       


  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Register()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
