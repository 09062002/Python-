import cv2

imgRosto = cv2.imread("face_a.jpg")
imgMao = cv2.imread("hand_b.jpg")

recorteOlhos = imgRosto[106: 125,50:149]
recorteDedo = imgMao[151:192, 187:265]
cv2.imshow("RecorteDedo", recorteDedo)
cv2.imshow("RecorteOlhos", recorteOlhos)

cv2.waitKey(0)
