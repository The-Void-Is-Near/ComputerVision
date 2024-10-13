import numpy as np
import cv2, time

cap = cv2.VideoCapture(1)  
fourcc = cv2.VideoWriter_fourcc(*'XVID')

time_string = time.strftime('%H:%M:%S', time.localtime()).replace(":", "_")
out = cv2.VideoWriter(f'{time_string}.avi', fourcc, 20.0, (640, 480))
  
while(True):

    ret, frame = cap.read() 
    out.write(frame) 

    cv2.imshow('Press \'q\' to close window.', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cap.release()
out.release() 
cv2.destroyAllWindows()
exit()