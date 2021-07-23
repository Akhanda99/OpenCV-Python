import cv2
import numpy as np

img= cv2.imread("tree_for_OpenCV.jpg")
imgResize=cv2.resize(img,(300,400))
imgCropped=img[0:200,50:]

cv2.imshow("Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)