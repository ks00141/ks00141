import cv2

img = cv2.imread("../img/img1.JPG",cv2.IMREAD_UNCHANGED)

cv2.imshow('img',img)
print(img)
cv2.waitKey()
cv2.destroyAllWindows()