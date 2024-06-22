import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from loginWindowGUI import Ui_Form

class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        # print("Login File")
        self.loginUi = Ui_Form()
        self.loginUi.setupUi(self)


        self.loginUi.illegalEntryMovie = QtGui.QMovie("E:/Jia/GUI files/illegalEntry.gif")
        self.loginUi.illegalEntry.setMovie(self.loginUi.illegalEntryMovie)

        self.loginUi.illegalEntry.hide()
        self.loginUi.loginButton.clicked.connect(self.ValidateLogin)
        self.loginUi.passwordEntry.setEchoMode(QLineEdit.Password)
        self.loginUi.exitButton.clicked.connect(self.close)
        self.loginUi.retryButton.clicked.connect(self.retryButton)
        self.loginUi.backButton.clicked.connect(self.connectToStartWindow)

    def ValidateLogin(self):
        username = self.loginUi.usernameEntry.text()
        pas = self.loginUi.passwordEntry.text()
        if username == 'jia' and pas == '1234':
            print("login sucessful")
            self.connectToJarvisMain()
        else:
            self.startMovie()

    def retryButton(self):
        self.loginUi.usernameEntry.clear()
        self.loginUi.passwordEntry.clear()
        self.stopMovie()

    def startMovie(self):
        self.loginUi.illegalEntry.show()
        self.loginUi.illegalEntryMovie.start()

    def stopMovie(self):
        self.loginUi.illegalEntry.hide()
        self.loginUi.illegalEntryMovie.stop()

    def connectToJarvisMain(self):
        from subprocess import call
        self.close()
        call(["python", "jarvisMainfile.py"])

    def connectToStartWindow(self):
        from subprocess import call
        self.close()
        call(["python", "main.py"])

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())