import sys

sys.path.append('UI/MainUI')
sys.path.append('UI/GridUI')
sys.path.append('Classes')
sys.path.append('arm_classes')

from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtCore import QThread
from PyQt4.QtCore import QTimer

import numpy as np

import MainUI
from Player import Player
from GridWindow import GridWindow
from Calibrator import Calibrator
from moveObj import moveObj

class App(QtGui.QMainWindow, MainUI.Ui_BCARM):
    player = Player()
    calibrator = Calibrator()

    grid = None

    transMat = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.grid = GridWindow()
	self.grid.labelSignaltoGUI.connect(self.receiveLabel)
	self.grid.patterDetectedSingaltoGUI.connect(self.startClassification)

        self.player.frameReady.connect(self.display)
        self.player.objectsReady.connect(self.sendObjects)
        self.player.start()

        self.calibrator.frameReady.connect(self.display)
        self.calibrator.done.connect(self.setTransMat)

	self.grid.startDetection()

    def receiveLabel(self, label):
        self.player.setFreeze(False)
        self.player.start()
	self.grid.startDetection()
	(x, y, z) = self.player.getPosition(label)
	print(x, y, z)
	if (not(x == 0 and y == 0 and z == 0)):
		pos = np.matrix([[x],[y],[z],[1]])
		point = self.transMat * pos
		moveObj(point[0],point[1],point[2],0,21.22,12.86)

    def display(self, rgb):
        self.lbl_rgb.setPixmap(QPixmap.fromImage(rgb).scaled(self.lbl_rgb.size()))

    def setTransMat(self, mat):
        self.transMat = mat
        print self.transMat
        self.player.setFreeze(False)
        self.player.start()

    def startClassification(self):
        self.player.setFreeze(True)
        self.grid.startClassification()

    def sendObjects(self, objs):
        self.grid.setObjects(objs)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.player.setFreeze(True)
            self.calibrator.start()

def main():
	app = QtGui.QApplication(sys.argv)
	form = App();
	form.showFullScreen();
	app.exec_();

if __name__ == '__main__':
    main()
