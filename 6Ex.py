import cv2 as cv
import numpy as np

img = cv.imread('taj_noise.jpg')
kernel = np.ones((4,4),np.float32)/16

dst = cv.filter2D(img,-1,kernel)
mesclados = np.concatenate((img, dst), axis=1)
cv.imshow('Original x Filtro gaussiano',mesclados)

cv.waitKey(0)