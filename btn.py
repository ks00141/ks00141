import cv2

img = cv2.imread("./img.jpg")
cv2.imshow("test",img)

cv2.waitKey()
cv2.destroyAllWindows()
