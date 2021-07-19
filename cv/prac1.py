import cv2
import numpy as np

f = open('./gsv.txt','w')
img = np.full((400,400),255,np.uint8)

cv2.imshow('test',img)
cv2.waitKey()