from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui  import QLabel
from PyQt4.QtGui  import QImage
from PyQt4.QtGui  import QPixmap
import cv2
import numpy as np

class Player(QThread):
   # a frame of RGB image from kinect is ready to be displayed
   frameReady = pyqtSignal(QImage)
   objectsReady = pyqtSignal(list)
   # 3D real coordinates for each label
   pos = np.zeros((20, 3), np.float32)

   rgb = None

   freeze = False
   flag = True

   labels = None
   # final labels to be displayed
   fLabels = []

   def __init__(self):
       QThread.__init__(self)

   def getPosition(self, label):
       if (label > len(self.pos)):
           return [0, 0, 0]
       return 100 * self.pos[label][0], 100 * self.pos[label][1], 100 * self.pos[label][2]
   
   def setFreeze(self, value):
       self.freeze = value 
       self.flag = True

   def getObjects(self):
       nLabels = len(self.fLabels)

       ret = []
       for i in range(nLabels):
           where = np.where(self.labels == self.fLabels[i])
           top   = np.amin(where[0])
           bot   = np.amax(where[0])
           left  = np.amin(where[1])
           right = np.amax(where[1])
           img = self.rgb[top:bot, left:right].copy()
           qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
           ret.append(qimg)
       return ret 

   def run(self):
        DEPTH_THRESH = 1000
        AREA_THRESH = 500
        capture = cv2.VideoCapture(cv2.CAP_OPENNI)
        while True:
            capture.grab()
            ok, self.rgb = capture.retrieve(0, cv2.CAP_OPENNI_BGR_IMAGE)
            ok, depth = capture.retrieve(0, cv2.CAP_OPENNI_DISPARITY_MAP) 
            ok, real = capture.retrieve(0, cv2.CAP_OPENNI_POINT_CLOUD_MAP)

            height, width = self.rgb.shape[:2]

            depth[:, :] = depth[:, :] * ((real[:, :, 2] * 1000) < DEPTH_THRESH)
                 
            if (self.rgb.shape[2] == 3):
                self.rgb = cv2.cvtColor(self.rgb, cv2.COLOR_BGR2RGB)

            edges  = cv2.Canny(depth, 20, 200, 3)
            edges  = cv2.GaussianBlur(edges, (5, 5), 0)
            edges[:, :] = 255 * (edges[:, :] == 0)
            mask = np.zeros((height + 2, width + 2), np.uint8)
            cv2.floodFill(edges, mask, (0, 0), 0)

            output = cv2.connectedComponentsWithStats(edges, 8, cv2.CV_32S)

            nLabels = output[0]
            self.labels  = output[1]
            stats = output[2]
            centroids = output[3]


            markedLabels = np.zeros(nLabels, np.bool)
            ret = np.zeros((height, width), np.uint8)

            markedLabels[:] = (stats[:, 4] > AREA_THRESH)
            markedLabels[0] = False

            rgb = self.rgb.copy()

            self.rgb[:, :, 0] = self.rgb[:, :, 0] * (markedLabels[self.labels[:, :]])
            self.rgb[:, :, 1] = self.rgb[:, :, 1] * (markedLabels[self.labels[:, :]])
            self.rgb[:, :, 2] = self.rgb[:, :, 2] * (markedLabels[self.labels[:, :]])

            self.fLabels = []
            cnt = 0 
            for i in range(centroids.shape[0]):
                if (markedLabels[i]):
                    self.fLabels.append(i)
                    label = chr(ord('A') + cnt)
                    y, x = int(centroids[i][0]), int(centroids[i][1])
                    cv2.putText(rgb, label, (y, x), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255))
                    if not self.freeze:
                        self.pos[cnt][0] = real[x][y][0]
                        self.pos[cnt][1] = real[x][y][1]
                        self.pos[cnt][2] = real[x][y][2]
                    #print "Label: ", label, real[x][y][0], real[x][y][1], real[x][y][2]
                    cnt += 1

            ret[:, :] = 255 * (markedLabels[self.labels[:, :]] == True)

            rgb = QImage(rgb, width, height, QImage.Format_RGB888)

            if (not self.freeze):
                self.frameReady.emit(rgb)

            if (self.freeze and self.flag):
                self.flag = False
                self.objectsReady.emit(self.getObjects())
