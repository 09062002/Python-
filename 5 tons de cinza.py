import cv2
import numpy as np

img = cv2.imread("bola_pink_blue.jpg", 0)
thresh, imgPB = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

mesclada = np.concatenate((img, imgPB), axis = 1)
cv2.imshow("Tons de Cinza x Preto e Branco", mesclada)

cv2.waitKey(0)
