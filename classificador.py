import keras as k
import numpy
from keras.models import load_model
from keras.preprocessing import image
from os import listdir
from os.path import isfile, join


# Definição de constantes
imagem_largura = 500
imagem_altura = 500
diretorio_exemplos = "exemplos/"

# Carregado o modelo salvo
modelo = load_model('modelo_treinado.h5')
modelo.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


apenasArquivos = [arquivo for arquivo in listdir(diretorio_exemplos) if isfile(join(diretorio_exemplos, arquivo))]

print('')
print('---------------------------------------------------')
print('Relatório individual por arquivo')
print('---------------------------------------------------')
print('')

contador_normal = 0
contador_anormal = 0

contador_acertos = 0
contador_erros = 0

pp = 0
pn = 0
np = 0
nn = 0


for file in apenasArquivos:
    imagem = k.preprocessing.image.load_img(diretorio_exemplos + file, target_size = (imagem_largura, imagem_altura))
    x = k.preprocessing.image.img_to_array(imagem)
    x = numpy.expand_dims(x, axis = 0)
    
    images = numpy.vstack([x])
    classes = modelo.predict_classes(images, batch_size = 10)
    classes = classes[0][0]
    
    if classes == 0:
        print(file + ': ' + 'negativo')
        contador_normal += 1
        
        classe = file.split('.')
        if(classe[0] == 'negativo'):
            contador_acertos += 1
            nn += 1
        else:
            contador_erros += 1
            np += 1
    else:
        print(file + ': ' + 'positivo')
        contador_anormal += 1

        classe = file.split('.')
        if(classe[0] == 'positivo'):
            contador_acertos += 1
            pp += 1
        else:
            contador_erros += 1
            pn += 1

print('')
print('---------------------------------------------------')
print('Relatório de radiografias normais e anormais:')
print('---------------------------------------------------')
print('')
print('Total de radiografias normais: ' , contador_normal)
print('Total de radiografias anormais: ', contador_anormal)
print('')
print('')
print('Acertos: ' , contador_acertos)
print('Erros: ', contador_erros)
print('')
print('')
print('Positivo - Positivo: ', pp)
print('Positivo - Negativo: ', pn)
print('Negativo - Positivo: ', np)
print('Negativo - Negativo: ', nn)
print('')
print('')
print('Taxa de Verdadeiro Positivo: ', pp / (pp + np))
print('Taxa de Falso Positivo: ', pn / (pn + nn))
print('Taxa de Acerto: ', (pp + nn) / (pp + pn + np + nn))
print('Taxa de Erro: ', (np + pn) / (pp + pn + np + nn))
print('')
