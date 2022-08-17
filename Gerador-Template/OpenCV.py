#Objetivo
#Gerar uma Imagem em OpenCV de tamanho grande, adicionar nessa imagem mascaras de outras imagens/Elementos de forma 100% randomica.
#Sendo assim será criado um Template em alta qualidade para ser utilizado no Instagram da Insper Dynamics
#Esse template depois deverá passar por uma função que corta a imagem, disponobilizando a versão final na resolução 1080x1080

import cv2
import os
diretorioraiz = r'/Users/antonioamaralegydiomartins/Desktop/Gerador-Template'
os.chdir(diretorioraiz)
img = cv2.imread("template.png")
diretorio = r'/Users/antonioamaralegydiomartins/Desktop/Gerador-Template/Recortes'
min_width = 0
max_width = 1080
min_height = 0
max_height = 1080

for e in range(20):
    if max_width == 4320:
        min_width = 0
        max_width = 1080
        min_height += 1080
        max_height += 1080
    if max_height == 5400:
        min_width += 1080
        max_width += 1080
    recorte = img[min_height:max_height, min_width:max_width]
    os.chdir(diretorio)
    cv2.imwrite(str(e) + ".png",recorte)
    #Algoritmo para Alteração de Width
    min_width += 1080
    max_width += 1080


cv2.imshow('template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()