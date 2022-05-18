import cv2

img = cv2.imread("lena_color_128_128_.jpg")

print("Altura da imagem: ", img.shape[0])
print("Largura da imagem: ", img.shape[1])
print("Quantidade de canais da imagem: ", img.shape[2])
