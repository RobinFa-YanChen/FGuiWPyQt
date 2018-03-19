import sys, subprocess
from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from device import Device
 
class MyTree(QTreeWidget):
 
    progress_signal = None
    progress = None
    devices = None


    def __init__(self, progressBar, devices):
        super().__init__()
        self.progress = progressBar
        self.devices = devices

    def setSignal(self, signal):
        self.progress_signal = signal

    def getDevices(self):
        self.progress.setMinimum(0)
        self.progress.reset()
        self.progress.setValue(0)
        names = subprocess.Popen(['adb', 'devices',  '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            if self.progress_signal != None:
                self.progress_signal.emit(i+1)

        progress_signal = None
 
    def buildDevicesWidget(self):

        self.setColumnCount(3)
        self.setHeaderLabels(['Checkbox','Name','Id'])
        
        #einlesen der self.Devices
        self.getDevices()

        for i in range(len(self.devices)):
            self.addTopLevelItem(self.devices[i].WidgetItem)