import sys

sys.path.append('UI/MainUI')
sys.path.append('UI/GridUI')
sys.path.append('Classes')

from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
from PyQt4 import QtCore
import MainUI
from Player import Player
from GridWindow import GridWindow

class App(QtGui.QMainWindow, MainUI.Ui_BCARM):
    player = Player()
    grid = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.player.start()
        self.player.frameReady.connect(self.display)
        self.grid = GridWindow()

    def display(self, rgb, seg):
        print self.player.getPosition(1)
        self.lbl_rgb.setPixmap(QPixmap.fromImage(rgb))
        self.lbl_segmented.setPixmap(QPixmap.fromImage(seg))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.grid.showFullScreen()
            self.grid.reader.start()

def main():
	app = QtGui.QApplication(sys.argv)
	form = App();
	form.showFullScreen();
	app.exec_();

if __name__ == '__main__':
    main()
