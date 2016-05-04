#import the necessary modules
import freenect
import cv2
import numpy as np
import math

#function to get RGB image from kinect
def get_frame():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#function to get depth image from kinect
def get_depth():
    global depth 
    depth, _ = freenect.sync_get_depth()
