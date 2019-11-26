# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_diemdanh.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(946, 590)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(50, 40, 751, 230))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnRecognitionFaces = QtWidgets.QPushButton(Dialog)
        self.btnRecognitionFaces.setGeometry(QtCore.QRect(840, 120, 75, 23))
        self.btnRecognitionFaces.setObjectName("btnRecognitionFaces")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(50, 290, 751, 230))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(370, 10, 91, 16))
        self.label.setObjectName("label")
        self.btnChoosePicture = QtWidgets.QPushButton(Dialog)
        self.btnChoosePicture.setGeometry(QtCore.QRect(840, 60, 75, 23))
        self.btnChoosePicture.setObjectName("btnChoosePicture")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnRecognitionFaces.setText(_translate("Dialog", "Nhan dang"))
        self.label.setText(_translate("Dialog", "GUI DIEM DANH"))
        self.btnChoosePicture.setText(_translate("Dialog", "Chon anh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
