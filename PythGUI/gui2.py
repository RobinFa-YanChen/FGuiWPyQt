import sys, subprocess
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTreeWidget, QTreeWidgetItem, QGroupBox, QPushButton, QApplication
from PyQt5 import QtCore

class MyApp(object):    
    def __init__(self):
        super(MyApp, self).__init__()                
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)

        self.hLayout = QHBoxLayout()
        self.mainLayout.insertLayout(0, self.hLayout)


        self.listA=QTreeWidget()
        self.listA.setColumnCount(3)
        self.listA.setHeaderLabels(['Checkbox','Name','Data'])
        for i in range(3):
            item=QTreeWidgetItem()
            item.setCheckState(0, 2)
            item.setText(1, 'Item '+str(i))
            item.setData(2, 256, id(item) )
            item.setText(2, str(id(item) ) )
            self.listA.addTopLevelItem(item)

        self.hLayout.addWidget(self.listA)

        self.buttonGroupbox = QGroupBox()
        self.buttonlayout = QVBoxLayout()
        self.buttonGroupbox.setLayout(self.buttonlayout)

        okButton = QPushButton('Remove Selected')
        okButton.clicked.connect(self.removeSel)
        self.buttonlayout.addWidget(okButton)

        getDataButton = QPushButton('Get Items Data')
        getDataButton.clicked.connect(self.getItemsData)
        self.buttonlayout.addWidget(getDataButton)

        self.mainLayout.addWidget(self.buttonGroupbox)
        self.mainWidget.show()
        sys.exit(app.exec_())

    def removeSel(self):
        listItems = []
        for i in range(self.listA.topLevelItemCount()):
            item=self.listA.topLevelItem(i)
            print("item", item)
            if (item.checkState(0) == 2):
                listItems.append(item)

        print("listItems: ",listItems)

        for item in listItems:
            print("item: ", item)
            itemIndex=self.listA.indexOfTopLevelItem(item)
            print("itemIndex", itemIndex)
            self.listA.takeTopLevelItem(itemIndex)
        print('\n\t Number of items remaining', self.listA.topLevelItemCount())

    def getItemsData(self):
        for i in range(self.listA.topLevelItemCount()):
            item=self.listA.topLevelItem(i)
            itmData=item.data(2, 256)
            print('\n\t Item Id Stored as Item Data:', itmData, 'Item Checkbox State:', item.checkState(0))

if __name__ == '__main__':
    what = subprocess.Popen(['adb', 'devices',  '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, errs = what.communicate()
    out = str(out, 'utf-8')
    outs = out.split()
    del outs[0:4]
    length = len(outs)
    n = length/6
    struct = [[] for i in range(int(n))]
    for i in range(int(n)):
        print(n, i)
        struct[i] = outs[i*6:(i+1)*6]
        print(struct[i])
    app = QApplication(sys.argv)
    MyApp()