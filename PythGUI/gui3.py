import sys, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout, QAction, QTreeWidget, QTreeWidgetItem, QFileDialog, QDialog, QComboBox
from device import Device
from license import License


licenses = ["A","B","C"]
devices = []

def getDevices():
    names = subprocess.Popen(['adb', 'devices',  '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = names.communicate()
    outs = str(out, 'utf-8').split()
    del outs[0:4]
    length = len(outs)
    n = length/6

    # bilde neue Struktur
    struct = [[] for i in range(int(n))]
    for i in range(int(n)):

        struct[i] = outs[i*6:(i+1)*6]
        id = struct[i][0]

        item = QTreeWidgetItem()
        item.setCheckState(0, 2)
        item.setText(2, id)

        device = Device(id, item)
        device.getName()
        devices.append(device)

def getButtons(QDialog):
    b1=QPushButton("Button 1")
    b2=QPushButton("Button 2")
    b3=QPushButton("Button 3")

    mainLayout = QHBoxLayout()
    mainLayout.addWidget(b1)
    mainLayout.addWidget(b2)
    mainLayout.addWidget(b3)

    QDialog.setLayout(mainLayout)

# $ adb shell dumpsys wifi|grep device_name|tail -1

def makeLayout(horizontal, list, window):
    layout = None
    if horizontal:
        layout = QHBoxLayout(window);
    else:
        layout = QVBoxLayout(window);

    for i in range(len(list)):
        layout.addWidget(list[i])

    window.setLayout(layout)

def getLicenseBox():
    combo = QComboBox()
    for i in range(len(licenses)):
        combo.addItem(licenses[i])
    return combo

    QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    window.left = 10
    window.top = 10
    window.width = 640
    window.height = 400
    window.setGeometry(window.left, window.top, window.width, window.height)

    window.setWindowTitle("EXP360 Data Control")

    window_layout = []

    window_list = QWidget()
    window_list_layout = QHBoxLayout(window_list)

    license_Layout = []

    license = QWidget()

    licenseTitel = QLabel("License:")
    license_Layout.append(licenseTitel)
    licenseBox = getLicenseBox()
    license_Layout.append(licenseBox)

    makeLayout(False, license_Layout, license)

    window_layout.append(license)

    list = QTreeWidget()
    list.setColumnCount(3)
    list.setHeaderLabels(['Checkbox','Name','Id'])
    
    #einlesen der Devices
    getDevices()

    for i in range(len(devices)):
        list.addTopLevelItem(devices[i].WidgetItem)


    window_list_layout.addWidget(list)

    dialog = QDialog()
    getButtons(dialog)

    window_list.setLayout(window_list_layout)

    window_layout.append(window_list)

    window_layout.append(dialog)

    makeLayout(False, window_layout, window)

    print("devices: ", devices)

    window.show()

    sys.exit(app.exec_())