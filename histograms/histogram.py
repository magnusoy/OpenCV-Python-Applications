import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread("road.jpg")
b, g, r = cv2.split(img)
 
cv2.imshow("img", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
 
 
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()