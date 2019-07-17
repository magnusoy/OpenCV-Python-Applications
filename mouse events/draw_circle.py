import cv2
import numpy as np
 
def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        circles.append((x, y))
 
 
cap = cv2.VideoCapture(0)
 
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)
 
circles = []
while True:
    _, frame = cap.read()
 
    for center_position in circles:
        cv2.circle(frame, center_position, 5, (0, 0, 255), -1)
 
    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circles = []
 
 
cap.release()
cv2.destroyAllWindows()