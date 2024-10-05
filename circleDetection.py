import cvzone
from cvzone.ColorModule import ColorFinder
import cv2
import numpy as np
import math

prevCircle= None
dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

success, img = cap.read()
h,w,_ = img.shape

hsvVals = {'hmin': 97, 'smin': 27, 'vmin': 89, 'hmax': 179, 'smax': 87, 'vmax': 255}
myColorFinder=ColorFinder(False)

while True:

    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img,hsvVals)
    imgContour, contours = cvzone.findContours(img,mask,minArea=1_000)
    
    if contours:
        data = contours[0]['center'][0],\
            h-contours[0]['center'][1],\
            int(contours[0]['area'])
        
        x = data[0]
        y = data[1]
        area = math.ceil(math.sqrt(data[2]))
    
    mask = cv2.GaussianBlur(mask, (17,17), 0)
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=45,maxRadius=400)
#

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i  
        cv2.circle(img, (chosen[0],chosen[1]), 5, (0,100,100), 3)#draw a dot at center of detected circle
        cv2.circle(img, (chosen[0],chosen[1]), chosen[2], (255,0,255), 3)
        prevCircle = chosen

#    
    img = cvzone.stackImages([img,mask],2,.5)
    img = cv2.putText(img, f'Data: x: {x}  y: {y}  Area: {area}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.01,(255,255,255),2,cv2.LINE_AA)
    img = cv2.putText(img, f'Data: x: {x}  y: {y}  Area: {area}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)
    
    cv2.imshow("Press \'q\' To Close Window.",img)

    if cv2.waitKey(1)&0xff==ord('q'): break

cap.release()
cv2.destroyAllWindows()
