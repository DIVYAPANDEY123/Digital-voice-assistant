# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisMainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.arcLabel = QtWidgets.QLabel(Form)
        self.arcLabel.setGeometry(QtCore.QRect(750, 30, 700, 620))
        self.arcLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/techcircle.gif);")
        self.arcLabel.setText("")
        self.arcLabel.setObjectName("arcLabel")
        self.ironmanLabel = QtWidgets.QLabel(Form)
        self.ironmanLabel.setGeometry(QtCore.QRect(1700, -20, 250, 900))
        self.ironmanLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/ironman-portrait.webp);")
        self.ironmanLabel.setText("")
        self.ironmanLabel.setObjectName("ironmanLabel")
        self.backgroundLabel = QtWidgets.QLabel(Form)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 850, 1900, 110))
        self.backgroundLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/background.gif);")
        self.backgroundLabel.setText("")
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 760, 1850, 300))
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.terminalOutputBox = QtWidgets.QPlainTextEdit(self.frame)
        self.terminalOutputBox.setGeometry(QtCore.QRect(0, 10, 1600, 91))
        self.terminalOutputBox.setStyleSheet("border: 1px solid white;\n"
"font: 600 12pt \"Segoe UI Variable Display Semib\";\n"
"background-color: transparent;\n"
"border-radius: 2px;\n"
"color:white")
        self.terminalOutputBox.setObjectName("terminalOutputBox")
        self.terminalInputBox = QtWidgets.QLineEdit(self.frame)
        self.terminalInputBox.setGeometry(QtCore.QRect(0, 100, 1600, 50))
        self.terminalInputBox.setStyleSheet("border: 1px solid white;\n"
"font: 600 12pt \"Segoe UI Variable Display Semib\";\n"
"background-color: transparent;\n"
"border-radius: 2px;\n"
"color:white")
        self.terminalInputBox.setObjectName("terminalInputBox")
        self.enterButton = QtWidgets.QPushButton(self.frame)
        self.enterButton.setGeometry(QtCore.QRect(1505, 100, 91, 50))
        self.enterButton.setStyleSheet("border-image: url(E:/Jia/GUI files/enter(with border).png);")
        self.enterButton.setText("")
        self.enterButton.setObjectName("enterButton")
        self.exitButton = QtWidgets.QPushButton(self.frame)
        self.exitButton.setGeometry(QtCore.QRect(1750, 100, 101, 50))
        self.exitButton.setStyleSheet("border-image: url(E:/Jia/GUI files/exit(with border).png);")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.codingLabel = QtWidgets.QLabel(Form)
        self.codingLabel.setGeometry(QtCore.QRect(10, 0, 300, 250))
        self.codingLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/B.G_Template_1.gif);")
        self.codingLabel.setText("")
        self.codingLabel.setObjectName("codingLabel")
        self.jarvisSpeakingLabel = QtWidgets.QLabel(Form)
        self.jarvisSpeakingLabel.setGeometry(QtCore.QRect(10, 250, 550, 490))
        self.jarvisSpeakingLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/speaking.gif);")
        self.jarvisSpeakingLabel.setText("")
        self.jarvisSpeakingLabel.setObjectName("jarvisSpeakingLabel")
        self.listeningLabel = QtWidgets.QLabel(Form)
        self.listeningLabel.setGeometry(QtCore.QRect(10, 250, 550, 490))
        self.listeningLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/listening.gif);")
        self.listeningLabel.setText("")
        self.listeningLabel.setObjectName("listeningLabel")
        self.loadingLabel = QtWidgets.QLabel(Form)
        self.loadingLabel.setGeometry(QtCore.QRect(10, 250, 550, 490))
        self.loadingLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/tech loading-cropped.gif);")
        self.loadingLabel.setText("")
        self.loadingLabel.setObjectName("loadingLabel")
        self.sleepingLabel = QtWidgets.QLabel(Form)
        self.sleepingLabel.setGeometry(QtCore.QRect(10, 250, 550, 490))
        self.sleepingLabel.setStyleSheet("border-image: url(E:/Jia/GUI files/smokecricle.gif);")
        self.sleepingLabel.setText("")
        self.sleepingLabel.setObjectName("sleepingLabel")
        self.logoLabel = QtWidgets.QLabel(Form)
        self.logoLabel.setGeometry(QtCore.QRect(260, 0, 37, 12))
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.terminalOutputBox.setPlaceholderText(_translate("Form", "Terminal Output Goes Here"))
        self.terminalInputBox.setPlaceholderText(_translate("Form", "Enter Your Command"))
        self.logoLabel.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
