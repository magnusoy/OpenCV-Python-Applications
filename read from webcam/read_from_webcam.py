import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    cv2.imshow("gray scale", gray_frame)
    cv2.imshow("frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
 
cap.release()
cv2.destroyAllWindows()