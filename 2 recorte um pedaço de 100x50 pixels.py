import cv2

img = cv2.imread("lena_color_128_128_.jpg")

recorte = img[110: 110+50,107:107+100]

cv2.imshow("Original", img)
cv2.imshow("Recorte", recorte)
cv2.waitKey(0)
