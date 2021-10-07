import cv2

img = cv2.imread("ori.png", 0)

img_1 = 255 - img

cv2.imshow("original", img)
cv2.imshow("negatif", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
