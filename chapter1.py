import cv2
import numpy as np

print("Package Imported")
#Importing Image
img= cv2.imread("tree_for_OpenCV.jpg")
kernel=np.ones((5,5),np.uint8)

imgGray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
imgCanny=cv2.Canny(imgGray,200,300)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow("Output",img)
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilate Image",imgDilation)
cv2.imshow("Erode Image",imgEroded)


cv2.waitKey(0)