import cv2
import numpy as np

img = cv2.imread("bolas_cores.jpg")
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh, imgPB = cv2.threshold(imgCinza, 127, 255, cv2.THRESH_BINARY)
imgPBRGB = cv2.cvtColor(imgPB, cv2.COLOR_GRAY2RGB)

mesclada = np.concatenate((img, imgPBRGB), axis = 1)
cv2.imshow("Original x Preto e Branco", mesclada)

cv2.waitKey(0)
