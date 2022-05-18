import cv2
import numpy as np
img = cv2.imread("taj_noise.jpg",0)

blur = cv2.GaussianBlur(img, (5,5),0)
canny = cv2.Canny(blur, 30,220)
mescladas = np.concatenate((img, canny), axis = 1)

cv2.imshow("Bordas", mescladas)

cv2.waitKey(0)
