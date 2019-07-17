import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
 
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 100, 150)
 
    cv2.imshow("Frame", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)
 
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()