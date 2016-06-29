from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
import GridUI
import sys
from EEG_reader import EEGReader
from PyQt4.QtCore import pyqtSignal

class GridWindow(QtGui.QMainWindow, GridUI.Ui_BCARM):
    labelsList = []
    reader = None
    receiveLabel = pyqtSignal(int)    

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.labelsList = [[self.A, self.B, self.C],
                           [self.D, self.E, self.F],
                           [self.G, self.H, self.I]]
        self.objList = [self.objA, self.objB, self.objC, self.objD, self.objE]
        self.lblObjList = [self.lbl_objA, self.lbl_objB, self.lbl_objC, self.lbl_objD, self.lbl_objE]
        self.reader = EEGReader();
        self.reader.flashOn.connect(self.flashOn)
        self.reader.flashOff.connect(self.flashOff)
	self.reader.sendLabel.connect(self.sendLabel)

    def showFullScreen(self):
        super(self.__class__, self).showFullScreen()
        for lbl in self.lblObjList:
            lbl.hide()
        self.reader.start()
 
    def sendLabel(self, label):
	self.receiveLabel.emit(label)
        self.close()
    
    def setObjects(self, l):
        i = 0
        for obj in l:
            self.lblObjList[i].show()
            self.objList[i].setPixmap(QPixmap.fromImage(obj).scaled(self.objList[i].size()))
            i += 1
	
    def flashOn(self, rc):
        dx, dy = 0, 1
        x, y = rc, 0
        if (rc > 2): 
            dx, dy = 1, 0
            x, y = 0, rc - 3 
        for i in range(3):
            self.labelsList[x][y].setStyleSheet("color: rgb(255, 255, 255)")
            font = QtGui.QFont()
            font.setPointSize(64)
            self.labelsList[x][y].setFont(font)
            x = x + dx
            y = y + dy

    def flashOff(self, rc):
        dx, dy = 0, 1
        x, y = rc, 0
        if (rc > 2): 
            dx, dy = 1, 0
            x, y = 0, rc - 3 
        for i in range(3):
            self.labelsList[x][y].setStyleSheet("color: rgb(61, 61, 61)")
            font = QtGui.QFont()
            font.setPointSize(48)
            self.labelsList[x][y].setFont(font)
            x = x + dx
            y = y + dy
