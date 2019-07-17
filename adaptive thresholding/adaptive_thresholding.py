import cv2
import numpy as np
 
img = cv2.imread("book_page.jpg")
 
_, threshold = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)
 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
mean_c = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 12)
gaus = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 12)
 
cv2.imshow("Img", img)
cv2.imshow("Binary threshold", threshold)
cv2.imshow("Mean C", mean_c)
cv2.imshow("Gaussian", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()