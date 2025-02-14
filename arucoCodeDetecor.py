import cv2

port = cv2.VideoCapture(0)

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

while True:
    ret, image = port.read()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
    cv2.imshow("LIVE", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

port.close()        
cv2.destroyAllWindows()
exit()
