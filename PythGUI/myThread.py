import time
from PyQt5 import QtCore

class Extended(QtCore.QThread):
    
    copied_percent_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
    
    def run(self):
        print("run: ")
        completed = 0
        while completed < 100:
            time.sleep(0.08)
            completed += 1
            self.copied_percent_signal.emit(completed)
            print("completed: ", completed)
