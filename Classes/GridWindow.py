from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
import GridUI
import sys
from EEG_reader import EEGReader

class GridWindow(QtGui.QMainWindow, GridUI.Ui_BCARM):
    labelsList = []
    reader = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.labelsList = [[self.A, self.B, self.C],
                           [self.D, self.E, self.F],
                           [self.G, self.H, self.I]]
        self.reader = EEGReader();
        self.reader.flashOn.connect(self.flashOn)
        self.reader.flashOff.connect(self.flashOff)

    def showFullScreen(self):
        super(self.__class__, self).showFullScreen()
        self.reader.start()

    def flashOn(self, rc):
        dx, dy = 0, 1
        x, y = rc, 0
        if (rc > 2): 
            dx, dy = 1, 0
            x, y = 0, rc - 3 
        for i in range(3):
            self.labelsList[x][y].setStyleSheet("color: rgb(255, 255, 255)")
            font = QtGui.QFont()
            font.setPointSize(128)
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
            font.setPointSize(96)
            self.labelsList[x][y].setFont(font)
            x = x + dx
            y = y + dy
