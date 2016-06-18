from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

class EEGReader(QThread):
   flashOn  = pyqtSignal(int)
   flashOff = pyqtSignal(int)

   def __init__(self):
       QThread.__init__(self)

   def run(self):

