import numpy as np
import cv2

img=cv2.imread("tree_for_OpenCV.jpg")
cv2.imshow("Tree", img)

# Translation
def translate(img,x,y):
    rows, cols = img.shape[:2]
    input_pts = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    output_pts = np.float32([[x,y], [x+cols - 1, y], [x, y+rows - 1]])

    # Calculate the transformation matrix using cv2.getAffineTransform()
    M = cv2.getAffineTransform(input_pts, output_pts)
    return cv2.warpAffine(img,M,(cols,rows))

# Rotation
def rotate(img, angle, rotPoint=None):
    height,width=img.shape[0:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    return cv2.warpAffine(img,rotMat,(height,width))


#Flipping
flippedImg=cv2.flip(img,-1)
cv2.imshow("Flipped Image", flippedImg)

# translated=translate(img,30,100)
# cv2.imshow("Translated",translated)

rotated=rotate(img,-90)
cv2.imshow("Rotation", rotated )
rotated_rotated=rotate(rotated,-20)
cv2.imshow("Rotation2", rotated_rotated)
print(img.shape)
cv2.waitKey(0)
