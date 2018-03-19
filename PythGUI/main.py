import sys, subprocess, time
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout, QAction, QTreeWidget, QTreeWidgetItem, QFileDialog, QDialog, QComboBox, QStatusBar, QProgressBar
from device import Device
from license import License
from myThread import Extended
from myTree import MyTree

class Main(QWidget):
    licenses = None
    devices = None
    widgets = None
    ext = None
    progress = None

    def __init__(self):
        super().__init__()
        self.licenses =["a", "b", "c"]
        self.devices = []
        self.widgets = []
        self.main()

    def refreshClicked(self, tree):

        self.progress.setMinimum(0)
        self.progress.setValue(0)
        self.progress.reset()

        self.ext = Extended(0, self.devices, self.progress, tree)
        self.ext.copied_percent_signal.connect(self.progressSignal)
        self.ext.start()

    def progressFunc(self):
        #completed = 0
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.reset()

        self.ext = Extended(1, self.devices, self.progress)
        self.ext.copied_percent_signal.connect(self.progressSignal)
        self.ext.start()

    def progressSignal(self, value):
        print("progressSignal: ")
        self.progress.setValue(value)
        #self.progress.reset()
        #print("text", self.progress.isTextVisible())

    def resetFunc(self):
        return

    def getButtons(self, QDialog, tree):
        b1=QPushButton("Refresh", QDialog)
        b1.clicked.connect(lambda: self.refreshClicked(tree))
        b2=QPushButton("TestButton", QDialog)
        b2.clicked.connect(self.progressFunc)
        b3=QPushButton("Button 3", QDialog)
        b3.clicked.connect(self.resetFunc)

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        mainLayout.addWidget(b3)

        QDialog.setLayout(mainLayout)

    # $ adb shell dumpsys wifi|grep device_name|tail -1

    def makeLayout(self, horizontal, list, window):
        layout = None
        if horizontal:
            layout = QHBoxLayout(window);
        else:
            layout = QVBoxLayout(window);

        for i in range(len(list)):
            layout.addWidget(list[i])

        window.setLayout(layout)

    def getLicenseBox(self):
        combo = QComboBox()
        for i in range(len(self.licenses)):
            combo.addItem(self.licenses[i])
        return combo

    def main(self):
        
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowTitle("EXP360 Data Control")

        window_layout = []

        window_list = QWidget()

        window_list_layout = []

        license_Layout = []

        license = QWidget()

        licenseTitel = QLabel("License:")
        license_Layout.append(licenseTitel)
        licenseBox = self.getLicenseBox()
        license_Layout.append(licenseBox)

        self.makeLayout(False, license_Layout, license)

        window_layout.append(license)

        self.progress =QProgressBar()

        list = MyTree(self.progress, self.devices)
        list.buildDevicesWidget()

        window_list_layout.append(list)

        dialog = QDialog()
        self.getButtons(dialog, list)

        self.makeLayout(True, window_list_layout, window_list)

        window_layout.append(window_list)

        window_layout.append(dialog)

        window_layout.append(self.progress)

        self.makeLayout(False, window_layout, self)

        print("devices: ", self.devices)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main = Main()

    layout = QHBoxLayout()
    layout.addWidget(main)


    sys.exit(app.exec_())