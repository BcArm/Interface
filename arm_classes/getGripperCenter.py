import cv2
import numpy as np
def getGripperCenter(img):
    #cv2.imwrite("", img)
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
    #img = cv2.resize(img, (600, 600))
    
##    for x in range(img.shape[0]):
##        for y in range(img.shape[1]):
##            b, g, r = map(int, img[x, y, :])
##            b = 0.5 * b
##            g = 1.2 * g
##            r = 1.3 * r
##            img[x, y, 0] = b
##            img[x, y, 1] = g
##            img[x, y, 2] = r
##            for c in range(3):
##                img[x, y, c] = 0.5 * img[x, y, c] + 70
    cv2.imshow("Current", img)
    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red_hue_range = cv2.inRange(img, (0, 0, 150), (100, 100, 255))
    upper_red_hue_range = cv2.inRange(hsvImg, (160, 100, 50), (185, 255, 255))
    red_hue_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)
    redImg = red_hue_image.copy()
    
##    redImg = cv2.inRange(hsvImg, (165, 200, 30), (195, 255, 70))
##    yelImg = cv2.inRange(hsvImg, (0, 140, 90), (30, 255, 160))

    lower_yel_hue_range = cv2.inRange(img, (0, 150, 0), (100, 255, 100))
    upper_yel_hue_range = cv2.inRange(hsvImg, (20, 120, 0), (115, 255, 180))
    yel_hue_image = cv2.addWeighted(lower_yel_hue_range, 1.0, upper_yel_hue_range, 1.0, 0.0)
    yelImg = yel_hue_image.copy()
##    for x in range(img.shape[0]):
##        for y in range(img.shape[1]):
##            b, g, r = map(int, img[x, y, :])
##            if (b <= 100 and r <= 100 and g >= 50 and abs(r - g) <= 60 and min(r, g) >= 1.7 * b):
##                yelImg[x, y] = 255


    
    redImg = cv2.medianBlur(redImg, 5)
    yelImg = cv2.medianBlur(yelImg, 5)

    redImg = cv2.GaussianBlur(redImg, (9, 9), 0)
    yelImg = cv2.GaussianBlur(yelImg, (9, 9), 0)


    #cv2.imshow("RED", redImg)
    #cv2.imshow("YEL", yelImg)

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
    out = img.copy()
    cv2.circle(out, (result[1], result[0]), 10, (0, 255, 0), 2)
    #cv2.setMouseCallback('Current', onMouse)
    cv2.imshow("Output", out)
    #cv2.waitKey(0)
    return result[0], result[1]
##getGripperCenter(cv2.imread("/home/ahmed/Documents/Images Gripper/IMG_658536584.jpg"))

'''
mouseX = -1000 
mouseY = -1000
def get_xy(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseX,mouseY = x,y

def getGripperCenter(img):
    global mouseX,mouseY
    cv2.namedWindow('mouse_img')
    cv2.setMouseCallback('mouse_img', get_xy)
    while(1):
        cv2.imshow('mouse_img',img)
        k = cv2.waitKey(20) & 0xFF
        if mouseX != -1000 and mouseY != -1000:
            X = mouseX
            Y = mouseY
            mouseX = -1000
            mouseY = -1000
            return [X,Y]
'''


'''
[[ -1.02719000e-01  -6.31904416e-02   9.81135057e-01  -1.10986320e+02]
 [ -1.24248832e+00   9.78801766e-02  -7.16412005e-02   1.76916514e+01]
 [ -3.60504918e-02   1.25425754e+00   1.19402989e-01  -1.05823853e+00]
 [ -2.77555756e-16  -1.11022302e-16  -2.22044605e-16   1.00000000e+00]]
'''

'''
[[ -8.13031148e-02   2.10798064e-02   1.03109180e+00  -1.28121499e+02]
 [ -1.22028757e+00   1.21168846e-01  -7.08492755e-02   1.53721200e+01]
 [ -3.14867159e-01   1.26608999e+00   1.14829436e-01  -4.36463273e+00]
 [ -1.11022302e-16  -2.22044605e-16   0.00000000e+00   1.00000000e+00]]
'''
