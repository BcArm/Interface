from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui  import QLabel
from PyQt4.QtGui  import QImage
from PyQt4.QtGui  import QPixmap
import cv2
import numpy as np

class Player(QThread):
   frameReady = pyqtSignal(QImage, QImage)
   pos = np.zeros((20, 3), np.float32)

   def __init__(self):
       QThread.__init__(self)

   def getPosition(self, label):
       return 100 * self.pos[label][0], 100 * self.pos[label][1], 100 * self.pos[label][2]

   def run(self):
       DEPTH_THRESH = 1500
       AREA_THRESH = 500
       capture = cv2.VideoCapture(cv2.CAP_OPENNI)
       while True:
           capture.grab()
           ok, rgb = capture.retrieve(0, cv2.CAP_OPENNI_BGR_IMAGE)
           ok, depth = capture.retrieve(0, cv2.CAP_OPENNI_DISPARITY_MAP) 
           ok, real = capture.retrieve(0, cv2.CAP_OPENNI_POINT_CLOUD_MAP)

           height, width = rgb.shape[:2]

           depth[:, :] = depth[:, :] * ((real[:, :, 2] * 1000) < DEPTH_THRESH)
            
           if (rgb.shape[2] == 3):
                rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)

           edges  = cv2.Canny(depth, 20, 200, 3)
           edges  = cv2.GaussianBlur(edges, (5, 5), 0)
           output = cv2.connectedComponentsWithStats(edges, 8, cv2.CV_32S)

           nLabels = output[0]
           labels  = output[1]
           stats   = output[2]
           centroids = output[3]

           markedLabels = np.zeros(nLabels, np.bool)
           ret = np.zeros((height, width), np.uint8)

           markedLabels[:] = (stats[:, 4] > AREA_THRESH)
           markedLabels[0] = False

           cnt = 0 
           for i in range(centroids.shape[0]):
               if (markedLabels[i]):
                   label = chr(ord('A') + cnt)
                   y, x = int(centroids[i][0]), int(centroids[i][1])
                   cv2.putText(rgb, label, (y, x), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
                   self.pos[cnt][0] = real[x][y][0]
                   self.pos[cnt][1] = real[x][y][1]
                   self.pos[cnt][2] = real[x][y][2]
                   #print "Label: ", label, real[x][y][0], real[x][y][1], real[x][y][2]
                   cnt += 1

           ret[:, :] = 255 * (markedLabels[labels[:, :]] == True)

           rgb = QImage(rgb, width, height, QImage.Format_RGB888)
           depth = QImage(ret, width, height, QImage.Format_Indexed8)

           self.frameReady.emit(rgb, depth)
