import cv2
import numpy as np
def getGripperCenter(img):
    def onMouse(event, x, y, f, g):
        print("hsv" + str(hsvImg[y, x, :]))
        print("img" + str(img[y, x, :]))
    def getCentroids(img):
        nLabels, labels = cv2.connectedComponents(img, 8)
        X = [0] * nLabels
        Y = [0] * nLabels
        cnt = [0] * nLabels
        for r in xrange(img.shape[0]):
            for c in xrange(img.shape[1]):
                label = labels[r, c]
                X[label] += r
                Y[label] += c
                cnt[label] += 1
        ret = []
        for i in xrange(1, nLabels):
            if (cnt[i] > 50):
                ret.append((X[i] / cnt[i], Y[i] / cnt[i]))
        return ret

    def getDistance(X, Y):
        dx = X[0] - Y[0]
        dy = X[1] - Y[1]
        return dx * dx + dy * dy

    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red_hue_range = cv2.inRange(img, (0, 0, 150), (100, 100, 255))
    upper_red_hue_range = cv2.inRange(hsvImg, (160, 100, 50), (185, 255, 255))
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)
    redImg = red_hue_image.copy()
    
    lower_yel_hue_range = cv2.inRange(img, (0, 150, 0), (100, 255, 100))
    upper_yel_hue_range = cv2.inRange(hsvImg, (20, 120, 0), (115, 255, 180))
    yel_hue_image = cv2.addWeighted(lower_yel_hue_range, 1.0, upper_yel_hue_range, 1.0, 0.0)
    yelImg = yel_hue_image.copy()
    
    redImg = cv2.medianBlur(redImg, 5)
    yelImg = cv2.medianBlur(yelImg, 5)

    redImg = cv2.GaussianBlur(redImg, (9, 9), 0)
    yelImg = cv2.GaussianBlur(yelImg, (9, 9), 0)

    cenRed = getCentroids(redImg)
    cenYel = getCentroids(yelImg)

    minD = -1
    result = (0, 0)
    for a in cenRed:
        for b in cenYel:
            d = getDistance(a, b)
            if (minD < 0 or d < minD):
                minD = d
                result = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

    return result

