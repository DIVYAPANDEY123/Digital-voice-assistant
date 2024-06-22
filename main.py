import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from mainGUI import Ui_mainGUIfile

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main File")
        self.mainUI = Ui_mainGUIfile()
        self.mainUI.setupUi(self)

        # this for gif movie
        self.mainUI.movie =QtGui.QMovie("E:\\Jia\\GUI files\\Hero_Template.gif")
        self.mainUI.label_2.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()
        
        # this part for button
        self.mainUI.pushButton_3.clicked.connect(self.close)
        self.mainUI.pushButton_2.clicked.connect(self.connectToLogingWindow)

        self.mainUI.pushButton.clicked.connect(self.connectToLogingWindow)

    # connect the all page code 
    # def connectToFaceRecognition(self):
    #     from faceRECOG import faceRECOG
    #     self.showFaceRecogWindow = faceRecog()
    #     ui.close()
    #     self.showFaceRecogWindow.show()

    def connectToLogingWindow(self):
        from subprocess import call
        self.close()
        call(["python", "loginWindow.py"])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())