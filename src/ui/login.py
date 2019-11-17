# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
