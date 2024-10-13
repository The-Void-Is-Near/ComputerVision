from pupil_apriltags import *
import cv2

def ignore(Error = None):
  pass
   
# Specifying AprilTag attributes
at_detector = Detector(families="tag36h11",nthreads=1,quad_decimate=1.0,quad_sigma=0.0,refine_edges=1,decode_sharpening=0.25,debug=0)
# Setting Camera Port to Webcam
vid = cv2.VideoCapture(0)

while(True):
  # Reading Grayscale Image
  ret, Image = vid.read()
  Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
  try:
    # Detect all Tags in Captured Frame
    Answer = at_detector.detect(img = Image)
    for apriltag in Answer:
      #Data from AT
      tagFamily = apriltag.tag_family.decode("utf-8")
      tagID = apriltag.tag_id
      text = f"{tagFamily} : {tagID}"
      # Converting to tuples from arrays
      (ptA, ptB, ptC, ptD) = apriltag.corners
      ptB = (int(ptB[0]), int(ptB[1]))
      ptC = (int(ptC[0]), int(ptC[1]))
      ptD = (int(ptD[0]), int(ptD[1]))
      ptA = (int(ptA[0]), int(ptA[1]))
      (cX, cY) = (int(apriltag.center[0]), int(apriltag.center[1]))
      #Draw
      cv2.line(Image, ptA, ptB, (0, 255, 0), 2)
      cv2.line(Image, ptB, ptC, (0, 255, 0), 2)
      cv2.line(Image, ptC, ptD, (0, 255, 0), 2)
      cv2.line(Image, ptD, ptA, (0, 255, 0), 2)
      cv2.circle(Image, (cX, cY), 5, (0, 0, 255), -1)
      cv2.putText(Image, text, (ptA[0], ptA[1] - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 3)
      cv2.putText(Image, text, (ptA[0], ptA[1] - 15),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
  except Exception as E:
    ignore(Error=E)

  cv2.imshow('Press "q" To Close Window.', Image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    vid.release()
    cv2.destroyAllWindows()
    break
exit()
