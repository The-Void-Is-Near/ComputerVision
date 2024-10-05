import cvzone
from cvzone.ColorModule import ColorFinder
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

success, img = cap.read()
h,w,_ = img.shape

myColorFinder=ColorFinder(True)
hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 0, 'hmax': 0, 'smax': 0, 'vmax': 0}#CHANGE THIS

while True:

    success, img = cap.read()
    imgColor, mask = myColorFinder.update(img,hsvVals)
    imgContour, contours = cvzone.findContours(img,mask,minArea=1_000)
    imgStack = cvzone.stackImages([imgColor,mask],2,.5)
    cv2.imshow("Press \'q\' To Close Window.",imgStack)

    if cv2.waitKey(1)&0xff==ord('q'): break
print(hsvVals)
cap.release()
cv2.destroyAllWindows()
