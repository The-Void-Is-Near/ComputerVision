import cv2
import numpy as np
vid = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(1)
while(True):
	ret, frame1 = vid.read()
	ret, frame2 = vid2.read()
	VIDEO = np.concatenate((frame1,frame2))
	try:	
		cv2.imshow('Press "q" To Close Windows.', VIDEO)
	except Exception as e:
		print(e)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
vid.release()
cv2.destroyAllWindows()
