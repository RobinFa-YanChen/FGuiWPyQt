import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar() 
        editMenu = mainMenu.addMenu('&Edit')
        editButton = QAction('Printe Was!', self)
        editButton.triggered.connect(self.doSomething)
        editMenu.addAction(editButton)
 

        self.show()

    def doSomething(self):
        print("ja es zeigt was")
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('&File')
        exitButton = QAction('Cancel', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        self.show()


    def refreshDevices(self):
        print("hehe")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())