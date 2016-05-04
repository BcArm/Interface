from PyQt4 import QtGui
from PyQt4.QtGui import QPixmap
from PyQt4 import QtCore
import main_form
import sys
from player import Player
from grid_window import GridWindow

class App(QtGui.QMainWindow, main_form.Ui_BCARM):
    player = Player()
    grid = None

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.player.start()
        self.player.frameReady.connect(self.display)
        self.grid = GridWindow()

    def display(self, img):
        self.lbl_rgb.setPixmap(QPixmap.fromImage(img))
        self.lbl_segmented.setPixmap(QPixmap.fromImage(img))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.grid.showFullScreen()

def main():
	app = QtGui.QApplication(sys.argv)
	form = App();
	form.showFullScreen();
	app.exec_();

if __name__ == '__main__':
    main()
