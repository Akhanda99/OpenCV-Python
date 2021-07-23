import cv2
import numpy as np

img=cv2.imread("/home/nashit/Desktop/Card.jpeg")
width, height=400,650

point1=np.float32([[550,42],[745,155],[387,327],[582,435]])
point2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(point1,point2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Card Image",img)
cv2.imshow("Output Image",imgOutput)

cv2.waitKey(0)