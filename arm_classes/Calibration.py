from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

import cv2
import numpy as np
from goToPosition import GoToPos
from transformation import getTransformationMat
from moveObj import moveObj
from getGripperCenterNew import getGripperCenter


class Calibrator(QThread):
	frameReady = pyqtSignal(QImage)

    def __init__(self):
        QThread.__init__(self)

	def run(self):
		points = [[-10,25,8.7], [0,21.22,12.86], [0,36,8.7], [10,21,15],  [-15,31,20],
				  [10,31,20],   [10,29,15],      [15,29,15], [-15,20,15], [-10,20,15],
				  [3,18,5],     [5,20,25],       [-5,25,25], [-5,30,6],   [15,20,6]]

		DELAY = 10 

		kinect_frame_pts = []
		cntFrames = 0
		indx = 0

		capture = cv2.VideoCapture()
		capture.open(cv2.CAP_OPENNI)

		x, y = 0, 0

		while True:
		    capture.grab()
		    
		    ok, rgb = capture.retrieve(0, cv2.CAP_OPENNI_BGR_IMAGE)
		    
		    ok, real = capture.retrieve(0, cv2.CAP_OPENNI_POINT_CLOUD_MAP)

		    rgb[:, :, 0] = rgb[:, :, 0] * (real[:, :, 2] < 1.5)
		    rgb[:, :, 1] = rgb[:, :, 1] * (real[:, :, 2] < 1.5)
		    rgb[:, :, 2] = rgb[:, :, 2] * (real[:, :, 2] < 1.5)

		    rgb[:, :, 0] = rgb[:, :, 0] * (real[:, :, 2] > 0.2)
		    rgb[:, :, 1] = rgb[:, :, 1] * (real[:, :, 2] > 0.2)
		    rgb[:, :, 2] = rgb[:, :, 2] * (real[:, :, 2] > 0.2)
			
			cp = rgb.copy()

		    if (indx > 1):
		        cv2.circle(rgb, (y, x), 10, (0, 255, 0), 2)
			
			if (rgb.shape[2] == 3):
                rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
			
			self.frameReady(QImage(rgb, width, height, QImage.Format_RGB888))

		    if (indx < 16 and cntFrames % DELAY == 0):
		        y, x = getGripperCenter(cp)
		        xw = 100 * real[x][y][0]
		        yw = 100 * real[x][y][1]
		        zw = 100 * real[x][y][2]
		        if (indx > 0):
		            print "Point ", indx, ": ", xw, yw, zw
		            kinect_frame_pts.append([xw, yw, zw])
		        if (indx < 15):
		            GoToPos(points[indx][0], points[indx][1], points[indx][2], 'close')
		        indx += 1

		    if (indx == 16):
		       print "Calculating transformation matrix......"

    		   Kinect_frame_matrix = np.matrix([[kinect_frame_pts[0][0],kinect_frame_pts[0][1],kinect_frame_pts[0][2],1],
						                        [kinect_frame_pts[1][0],kinect_frame_pts[1][1],kinect_frame_pts[1][2],1],
						                        [kinect_frame_pts[2][0],kinect_frame_pts[2][1],kinect_frame_pts[2][2],1],
						                        [kinect_frame_pts[3][0],kinect_frame_pts[3][1],kinect_frame_pts[3][2],1],
						                        [kinect_frame_pts[4][0],kinect_frame_pts[4][1],kinect_frame_pts[4][2],1],
						                        [kinect_frame_pts[5][0],kinect_frame_pts[5][1],kinect_frame_pts[5][2],1],
						                        [kinect_frame_pts[6][0],kinect_frame_pts[6][1],kinect_frame_pts[6][2],1],
						                        [kinect_frame_pts[7][0],kinect_frame_pts[7][1],kinect_frame_pts[7][2],1],
						                        [kinect_frame_pts[8][0],kinect_frame_pts[8][1],kinect_frame_pts[8][2],1],
						                        [kinect_frame_pts[9][0],kinect_frame_pts[9][1],kinect_frame_pts[9][2],1],
						                        [kinect_frame_pts[10][0],kinect_frame_pts[10][1],kinect_frame_pts[10][2],1],
						                        [kinect_frame_pts[11][0],kinect_frame_pts[11][1],kinect_frame_pts[11][2],1],
						                        [kinect_frame_pts[12][0],kinect_frame_pts[12][1],kinect_frame_pts[12][2],1],
						                        [kinect_frame_pts[13][0],kinect_frame_pts[13][1],kinect_frame_pts[13][2],1],
						                        [kinect_frame_pts[14][0],kinect_frame_pts[14][1],kinect_frame_pts[14][2],1],])

    		   TRANS_MAT = getTransformationMat(Kinect_frame_matrix.transpose())
			   break

		    cntFrames += 1

