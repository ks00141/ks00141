import cv2

src = cv2.imread("./img/img.JPG",cv2.IMREAD_GRAYSCALE)

cv2.imshow("img",src)

cv2.waitKey(0)
cv2.destroyAllWindows()