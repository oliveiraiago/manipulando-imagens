from PIL import Image
import os
os.chdir(r'C:\Users\IagoR\PycharmProjects\manipulando-imagens\images')
catIm = Image.open('zophie.png')
# cria uma copia para não perder a imagem original
copycatIm = catIm.copy()
# recorta o rosto da gatinha
faceIm = copycatIm.crop((335,345,565,560))
# retorna os valores de altura e largura da imagem copiada
copycatImWidth, copycatImHeight = catIm.size
# retorna os valores de altura e largura do rosto da gatinha
faceImWidth, faceImHeight = faceIm.size
# loop para colar as caras da gatinha ao longo da imagem
# o loop 1 considera do ponto inicial zero até o ponto final do largura, pulando o valor da largura
# da cara da gatinha
for left in range(0, copycatImWidth, faceImWidth):
    # o loop 2 considera do ponto inicial zero até o ponto final da altura, pulando o valor da altura
    # da cara da gatinha
    for top in range(0, copycatImHeight, faceImHeight):
        print(left, top)
        copycatIm.paste(faceIm,(left,top))

copycatIm.save('tiled.png')