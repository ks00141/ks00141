import cv2
import numpy as np

img = cv2.imread("../img/img1.JPG",cv2.IMREAD_UNCHANGED)

f = open('./imgbit.txt','w')
f.write(str(np.array(img)))
f.close()
