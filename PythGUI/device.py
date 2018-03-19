import sys, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton, QListWidgetItem, \
    QHBoxLayout, QAction, QTreeWidget, QTreeWidgetItem, QFileDialog, QDialog, QComboBox

class Device():

    def __init__(self, id, QTreeWidgetItem):
        self.id = id
        self.WidgetItem = QTreeWidgetItem

    def getName(self):
        p1 = subprocess.Popen(['adb', '-s', self.id, 'shell', 'dumpsys', 'wifi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p2 = subprocess.Popen(['grep', 'device_name'], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p1.stdout.close()
        p3 = subprocess.Popen(['tail', '-1'], stdin=p2.stdout, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
        p2.stdout.close()
        out, errs = p3.communicate()
        out = str(out, 'utf-8')
        index1 = out.find('device_name')
        index1 = index1 + 11
        index2 = out.find('->')
        #outs = str(out, 'utf-8').split()
        self.name = out[index1:index2]
        self.WidgetItem.setText(1, out[index1:index2])