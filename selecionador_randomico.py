import shutil, os, random

# Definição de variáveis globais
caminho = 'dataset_teste/positivo'

def copiarArquivoParaOutroDiretorio(source, destino):
    shutil.copyfile(source, destino)

def carregarArrayDeArquivos(caminho):
    arquivos = []
    for arquivo in os.listdir(caminho):
        arquivos.append(os.path.join(caminho, arquivo))

    return arquivos   

def selecionarArquivosRandomicos(arquivos, quantidadeDeArquivosParaSelecionar):

    arquivosSelecionadosRandomicamente = []

    i = 1
    while i <= quantidadeDeArquivosParaSelecionar:
        arquivoRandomico = arquivos[random.randint(1, len(arquivos))]
        if(arquivoRandomico not in arquivosSelecionadosRandomicamente):
            arquivosSelecionadosRandomicamente.append(arquivoRandomico)
            i += 1

    return arquivosSelecionadosRandomicamente
    


if __name__ == '__main__':
    arquivos = carregarArrayDeArquivos(caminho)
    arquivosSelecionadosRandomicamente = selecionarArquivosRandomicos(arquivos, 100)
    
    for arquivo in arquivosSelecionadosRandomicamente:
        copiarArquivoParaOutroDiretorio(arquivo, 'exemplos/' + os.path.basename(arquivo))
    

    