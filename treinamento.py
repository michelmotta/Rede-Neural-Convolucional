# Importação de bibliotecas utilizadas no projeto
import keras
import matplotlib.pyplot as plt


# Definição de constantes
imagem_largura = 500
imagem_altura = 500
diretorio_imagens_treino = 'dataset_treino'
diretorio_imagens_teste = 'dataset_teste'
exemplos_treino = 9756
exemplos_teste = 659
epochs = 10
batch_size = 16


# Define qual o formato de dados Keras seguirá Para dados 2d (imagens) "channels_last" espera o formato (rows, cols, channels), enaquanto "channels_first" espera o formato (channels, rows, cols)
def defineInputShape():
    if keras.backend.image_data_format() == 'channels_first':
        inputShape = (3, imagem_largura, imagem_altura)
    else:
        inputShape = (imagem_largura, imagem_altura, 3)
    
    return inputShape


# Inicialização do modelo sequencial utilizando Keras
def criarModelo(inputShape):

    # Instanciação do modelo
    modelo = keras.models.Sequential()

    # Camada 1 - Convolução
    modelo.add(keras.layers.Conv2D(32, (3, 3), input_shape = inputShape, activation = 'relu'))
    
    # Camada 2 - Max Pooling
    modelo.add(keras.layers.MaxPooling2D(pool_size = (3, 3)))

    modelo.add(keras.layers.Dropout(0.1))

    # Camada 3 - Convolução
    modelo.add(keras.layers.Conv2D(32, (3, 3), activation = 'relu'))
    
    # Camada 4 - Max Pooling
    modelo.add(keras.layers.MaxPooling2D(pool_size = (3, 3)))

    modelo.add(keras.layers.Dropout(0.1))

    # Camada 5 - Convolução
    modelo.add(keras.layers.Conv2D(32, (3, 3), activation = 'relu'))
    
    # Camada 6 - Max Pooling
    modelo.add(keras.layers.MaxPooling2D(pool_size = (3, 3)))

    modelo.add(keras.layers.Dropout(0.1))

    # Camada 7 - Convolução
    modelo.add(keras.layers.Conv2D(64, (3, 3), activation = 'relu'))
    
    # Camada 8 - Max Pooling
    modelo.add(keras.layers.MaxPooling2D(pool_size = (3, 3)))

    modelo.add(keras.layers.Dropout(0.1))

    # Camada 9 - Convolução
    modelo.add(keras.layers.Conv2D(64, (3, 3), activation = 'relu'))
    
    # Camada 10 - Max Pooling
    modelo.add(keras.layers.MaxPooling2D(pool_size = (3, 3)))

    modelo.add(keras.layers.Dropout(0.1))
    
    # Camada 11 - Flattening
    modelo.add(keras.layers.Flatten())

    # Camada 12 - FullyConnected
    modelo.add(keras.layers.Dense(units = 128, activation = 'relu'))
  
    # Camada 13 - FullyConnected com apenas 1 saída binária
    modelo.add(keras.layers.Dense(units = 1, activation = 'sigmoid'))

    # Realiza a compilação do modelo criado
    modelo.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

    # Printa um resumo do modelo
    modelo.summary()

    return modelo


# Função responsável por realizar o treinamento do modelo recebido por parâmetro
def treinamentoDoModelo(inputShape, modelo):
    dados_treino = keras.preprocessing.image.ImageDataGenerator(rescale = 1. / 255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
    dados_teste = keras.preprocessing.image.ImageDataGenerator(rescale = 1. / 255)

    treino_gerador = dados_treino.flow_from_directory(diretorio_imagens_treino, target_size = (imagem_largura, imagem_altura), batch_size = batch_size, class_mode = 'binary')
    print(treino_gerador.class_indices)

    teste_gerador = dados_teste.flow_from_directory(diretorio_imagens_teste, target_size = (imagem_largura, imagem_altura), batch_size = batch_size, class_mode = 'binary')
    print(treino_gerador.class_indices)

    print('Iniciando o treinamento...')
    historico = modelo.fit_generator(treino_gerador, steps_per_epoch = exemplos_treino, epochs = epochs, validation_data = teste_gerador, validation_steps = exemplos_teste)
    print('Treinamento finalizado.')
    print('Iniciando criação do arquivo de modelo do treinamento.')
    modelo.save('modelo_treinado.h5')
    print('Arquivo de treinamento criado com sucesso.')

    return historico


# Plota um gráfico com o histórico de Acurácia x época
def plotarGraficoPrecisao(historico):
    plt.plot(historico.history['acc'])
    plt.plot(historico.history['val_acc'])
    plt.title('Acurácia do Modelo')
    plt.ylabel('Acurácia')
    plt.xlabel('Época')
    plt.legend(['Dataset Treino', 'Dataset de Teste'], loc = 'upper left')
    plt.show()


# Plota um gráfico com o histórico de perda resumido x época
def plotarGraficoPerda(historico):
    plt.plot(historico.history['loss'])
    plt.plot(historico.history['val_loss'])
    plt.title('Perda do Modelo')
    plt.ylabel('Perda')
    plt.xlabel('Época')
    plt.legend(['Dataset de Treino', 'Dataset de Teste'], loc = 'upper left')
    plt.show()


if __name__ == '__main__':
    InputShape = defineInputShape()
    modelo = criarModelo(InputShape)
    historico = treinamentoDoModelo(InputShape, modelo)
    plotarGraficoPrecisao(historico)
    plotarGraficoPerda(historico)