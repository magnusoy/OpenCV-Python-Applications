import cv2
import numpy as np
 
img1 = cv2.imread("road.jpg")
img2 = cv2.imread("car.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
 
ret, mask = cv2.threshold(img2_gray, 240, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
 
road = cv2.bitwise_and(img1, img1, mask=mask)
car = cv2.bitwise_and(img2, img2, mask=mask_inv)
result = cv2.add(road, car)
 
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("road background", road)
cv2.imshow("car no background", car)
cv2.imshow("mask", mask)
cv2.imshow("mask inverse", mask_inv)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()