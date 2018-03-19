import time
from PyQt5 import QtCore
from myTree import MyTree

class Extended(QtCore.QThread):
    
    copied_percent_signal = QtCore.pyqtSignal(int)
    option = None
    devices = None
    progress = None
    tree = None

    def __init__(self, option, devices, progress, tree = None):
        super().__init__()
        self.option = option
        self.tree = tree
        self.devices = devices
        self.progress = progress

    def refresh(self):
        print("refresh():")
        self.tree.setSignal(self.copied_percent_signal)
        for i in range(len(self.devices)):
            del self.devices[0]
        for j in range(self.tree.topLevelItemCount()):
            self.tree.takeTopLevelItem(0)
        self.tree.buildDevicesWidget()
        print("len: ", len(self.devices))
        print("zeilen: ", self.tree.topLevelItemCount())

    def test(self):
        completed = 0
        while completed < 100:
            time.sleep(0.08)
            completed += 1
            self.copied_percent_signal.emit(completed)
            print("completed: ", completed)

    def run(self):
        print("run: ")
        self.options[self.option](self)

    options = {0 : refresh,
             1 : test}
