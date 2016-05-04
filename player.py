from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui  import QLabel
from PyQt4.QtGui  import QImage
from PyQt4.QtGui  import QPixmap
import cv2
import kinect

class Player(QThread):
   frameReady = pyqtSignal(QImage)

   def __init__(self):
       QThread.__init__(self)

   def run(self):
       cap = cv2.VideoCapture(0)
       while True:
           ret, frame = cap.read()
           #frame = kinect.get_video()
           height, width = frame.shape[:2]
           if (frame.shape[2] == 3):
               frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
           img = QImage(frame, width, height, QImage.Format_RGB888)
           self.frameReady.emit(img)
