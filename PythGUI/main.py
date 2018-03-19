import sys, subprocess, time
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout, QAction, QTreeWidget, QTreeWidgetItem, QFileDialog, QDialog, QComboBox, QStatusBar, QProgressBar
from device import Device
from license import License
from myThread import Extended

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

    def progressFunc(self):
        self.ext
        #completed = 0
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.reset()

        """while completed < 100:
            time.sleep(0.08)
            completed += 1
            self.progress.setValue(completed)"""

        self.ext = Extended()
        self.ext.copied_percent_signal.connect(self.resetFunc)
        self.ext.start()

    def resetFunc(self, value):
        print("restFunc: ")
        self.progress.setValue(value)
        #self.progress.reset()
        #print("text", self.progress.isTextVisible())

    def getDevices(self):
        self.progress.setMinimum(0)
        self.progress.reset()
        self.progress.setValue(0)
        names = subprocess.Popen(['adb', 'self.devices',  '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, errs = names.communicate()
        outs = str(out, 'utf-8').split()
        del outs[0:4]
        length = len(outs)
        n = length/7
        
        self.progress.setMaximum(n)
        


        # bilde neue Struktur
        struct = [[] for i in range(int(n))]
        for i in range(int(n)):

            struct[i] = outs[i*7:(i+1)*7]
            id = struct[i][0]

            item = QTreeWidgetItem()
            item.setCheckState(0, 2)
            item.setText(2, id)

            device = Device(id, item)
            device.getName()
            self.devices.append(device)
            self.progress.setValue(i+1)

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

    def buildDevicesWidget(self, tree):

        tree.setColumnCount(3)
        tree.setHeaderLabels(['Checkbox','Name','Id'])
        
        #einlesen der self.Devices
        self.getDevices()

        for i in range(len(self.devices)):
            tree.addTopLevelItem(self.devices[i].WidgetItem)

    def refreshClicked(self, tree):
        self.progress.setValue(0)
        for i in range(len(self.devices)):
            del self.devices[0]
        for j in range(tree.topLevelItemCount()):
            tree.takeTopLevelItem(0)
        self.buildDevicesWidget(tree)
        print("len: ", len(self.devices))
        print("zeilen: ", tree.topLevelItemCount())

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

        list = QTreeWidget()
        self.buildDevicesWidget(list)

        window_list_layout.append(list)

        dialog = QDialog()
        self.getButtons(dialog, list)

        self.makeLayout(True, window_list_layout, window_list)

        window_layout.append(window_list)

        window_layout.append(dialog)

        window_layout.append(self.progress)

        self.makeLayout(False, window_layout, self)

        print("self.devices: ", self.devices)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    main = Main()

    sys.exit(app.exec_())