# Importes das bibliotecas utilizadas no projeto
import keras
import numpy
import tensorflow
import os
import flask
import base64
import random
import string
import os
import flask_cors


# Criação da instância da aplicação do flesk
app = flask.Flask(__name__, template_folder = 'templates')
flask_cors.CORS(app)


# Definição de variáveis globais e constantes
global modelo, grafo
imagem_largura = 500
imagem_altura = 500
diretorio_uploads = 'static/images/'
diretorioBaseImagens = 'http://localhost:5000/static/images/'


# Função responsável por carregar o modelo usado na predição das imagens
def carregarModelo():
    modelo = keras.models.load_model('modelo_treinado.h5')
    modelo.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
    grafo = tensorflow.get_default_graph()

    return modelo, grafo


# Função que recebe um caminho de diretório, analiza e classifica todas as imagens do diretório e retorna uma resposta em formato Json com a URL da imagem e a classificação
def classificarImagens(nomeDoDiretorio):
    with grafo.as_default():
        todasAsImagensDoDiretorio = [arquivo for arquivo in os.listdir(diretorio_uploads + nomeDoDiretorio) if os.path.isfile(os.path.join(diretorio_uploads + nomeDoDiretorio, arquivo))]

        respostaJson = []
        for arquivoImagem in todasAsImagensDoDiretorio:
            imagem = keras.preprocessing.image.load_img(diretorio_uploads + nomeDoDiretorio + arquivoImagem, target_size = (imagem_largura, imagem_altura))
            x = keras.preprocessing.image.img_to_array(imagem)
            x = numpy.expand_dims(x, axis = 0)
            
            images = numpy.vstack([x])
            classes = modelo.predict_classes(images, batch_size = 16)
            classes = classes[0][0]
            
            if classes == 0:
                normal = {
                    'imagem_URL': diretorioBaseImagens + nomeDoDiretorio + arquivoImagem,
                    'classificacao': 'Normal'
                }
                respostaJson.append(normal)

            else:
                anormal = {
                    'imagem_URL': diretorioBaseImagens  + nomeDoDiretorio + arquivoImagem,
                    'classificacao': 'Anormal'
                }
                respostaJson.append(anormal)
    
    return respostaJson


# Função responsável por receber uma imagem em formato base64 e converter essa imagem em um arquivo de iamgem
def converterESalvarImagem(nomeDaImagem, imagemBase64, diretorio):
    nome, extensao = os.path.splitext(nomeDaImagem)
    _, imagemBase64Limpa = imagemBase64.split(',')
    nomeRandomico = gerarStringRandomica()
    with open('static/images/' + diretorio + '/' + nomeRandomico + extensao, 'wb') as arquivo:
        arquivo.write(base64.decodebytes(imagemBase64Limpa.encode()))

    return True


# Funcão responsável por renderizar uma página html para requisições recebidas em "/"
@app.route('/')
def index():
    return flask.render_template('index.html')


# Função responsável por gerar uma string randômica com 10 caracteres
def gerarStringRandomica(tamanho = 10):
    letras = string.ascii_lowercase

    return ''.join(random.choice(letras) for i in range(tamanho))


# Funcão responsável por devolver uma resposta em formato Json para requisições recebidas em "/api/classificar"
@app.route('/api/classificar', methods=['POST'])
def classificar():    
    conteudo = flask.request.get_json()

    nomeDoDiretorio = gerarStringRandomica() + '/'
    
    if not os.path.exists('static\\images\\' + nomeDoDiretorio):
        os.makedirs('static\\images\\' + nomeDoDiretorio)

    for item in conteudo:
        converterESalvarImagem(item['nome_da_imagem'], item['base64_da_imagem'], nomeDoDiretorio)

    resultadoDaClassificacao = classificarImagens(nomeDoDiretorio)    

    return flask.jsonify(resultadoDaClassificacao)

modelo, grafo = carregarModelo()

# Função main da aplicação
if __name__ == '__main__':
    app.run(debug=True)