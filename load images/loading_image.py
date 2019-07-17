import cv2
 
image = cv2.imread("lines.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow("Gray image", gray_image)
cv2.imshow("Red image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()