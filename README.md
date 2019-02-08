# Classificação de Imagens Radiográficas Utilizando Rede Neural Convolucional

### Trabalho desenvolvido pelos acadêmicos:

- [Michel Motta](https://www.facebook.com/michel.mottadasilva)
- Thiago Machado

## Descrição do Trabalho

A proposta do trabalho foi desenvolver um modelo de Inteligência Artificial utilizando Rede Neural Convolucional capaz de analisar imagens Radiográficas de ossos quebrados. As imagens utilizadas para o treinamento da Rede Neural Convolucional foram obtidas através do projeto [MURA](https://stanfordmlgroup.github.io/competitions/mura/), mantido pelo Stanford Machine Learning Group.

O modelo de classificação binária deveria receber como entrada um conjunto de imagens e classificar cada uma das imagens como sendo normal ou anormal. Todos os detalhes e metodologias utilizados neste trabalho podem ser lidos no [artigo final](https://github.com/michelmotta/Trabalho-Inteligencia-Artificial/blob/master/Artigo%20-%20Trabalho%20de%20Inteligência%20Artificial.pdf).

## Metodologia do trabalho
- Ajuste do conjunto de imagens
- Desenvolvimento e trainamento da Rede Neural Convolucional
- Avaliação do Modelo
- Desenvolvimento do ambiente de Implantação

Todos os detalhes sobre a metodologia e processos utilizados no trabalho podem ser lidos [neste artigo](https://github.com/michelmotta/Trabalho-Inteligencia-Artificial/blob/master/Artigo%20-%20Trabalho%20de%20Inteligência%20Artificial.pdf).

## Implantação do modelo de classificação

O modelo gerado com o treinamento da Rede Neural Convolucional foi utilizado em uma [API desenvolvida em Python](https://github.com/michelmotta/Trabalho-Inteligencia-Artificial/tree/master/python-server-api). Essa API foi responsável por receber dados em formato JSON e devolver uma resposta em formato Json. Essa resposta é a classificação de cada uma das imagens enviadas. Assim como também foi desenvolvida uma [aplicação FrontEnd](https://github.com/michelmotta/Trabalho-Inteligencia-Artificial/tree/master/client-api) para interagir com a API.

## Resultados

Apesar da limitação de processamento físico por causa dos equipamentos utilizandos durante o desenvolvimento deste trabalho, nós tivemos alguns resultados muito interessantes. Conforme pode-se visualizar no gráfico ROC do classificador.

![Gráfico ROC](https://github.com/michelmotta/Trabalho-Inteligencia-Artificial/blob/master/grafico_roc.png)
