import cv2
import numpy as np
img=np.zeros((512,512,3))
print(img.shape)
img[:]=0,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(0,20),(250,200),(255,255,255),cv2.FILLED)
cv2.circle(img,(400,400),30,(255,255,0),cv2.FILLED)
cv2.putText(img,"OpenCV",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(150,0,0),1)

cv2.imshow("Image",img)
cv2.waitKey(0)