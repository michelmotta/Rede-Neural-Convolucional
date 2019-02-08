import os
import shutil
import csv

def copiarArquivosPositivos(src, dst, counter, symlinks = False, ignore = None):
    for arquivo in os.listdir(src):
        novoArquivoDividido = arquivo.split('.')
        s = os.path.join(src, arquivo)
        d = os.path.join(dst, 'positivo.' + str(counter) + '.' + novoArquivoDividido[1])
        if os.path.isdir(s):
            print('Diretório encontrado')
        else:
            shutil.copy2(s, d)
            counter += 1 
    return counter        

def copiarArquivosNegativos(src, dst, counter, symlinks = False, ignore = None):
    for arquivo in os.listdir(src):
        novoArquivoDividido = arquivo.split('.')
        s = os.path.join(src, arquivo)
        d = os.path.join(dst, 'negativo.' + str(counter) + '.' + novoArquivoDividido[1])
        if os.path.isdir(s):
            print('Diretório encontrado')
        else:
            shutil.copy2(s, d)
            counter += 1
    return counter

def main():
    with open('MURA-v1.1/train_labeled_studies.csv') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter = ',')
        contador_de_linhas = 0

        contador_positivo_xr_elbow = 1
        contador_negativo_xr_elbow = 1

        contador_positivo_xr_finger = 1
        contador_negativo_xr_finger = 1

        contador_positivo_xr_forearm = 1
        contador_negativo_xr_forearm = 1

        contador_positivo_xr_hand = 1
        contador_negativo_xr_hand = 1

        contador_positivo_xr_humerus = 1
        contador_negativo_xr_humerus = 1

        contador_positivo_xr_shoulder = 1
        contador_negativo_xr_shoulder = 1

        contador_positivo_xr_wrist = 1
        contador_negativo_xr_wrist = 1

        for linha in leitor_csv:
            contador_de_linhas += 1
            
            linhaDividida = linha[0].split('/')
            
            if(linhaDividida[2] == 'XR_ELBOW'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_elbow = copiarArquivosPositivos(linha[0], 'datasets/XR_ELBOW/dataset_treino/positivo', contador_positivo_xr_elbow, False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_elbow = copiarArquivosNegativos(linha[0], 'datasets/XR_ELBOW/dataset_treino/negativo', contador_negativo_xr_elbow, False, None)

            if(linhaDividida[2] == 'XR_FINGER'):  
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    copiarArquivosPositivos(linha[0], 'datasets/XR_FINGER/dataset_treino/positivo', contador_positivo_xr_finger, False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    copiarArquivosNegativos(linha[0], 'datasets/XR_FINGER/dataset_treino/negativo', contador_negativo_xr_finger, False, None)  
            
            if(linhaDividida[2] == 'XR_FOREARM'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_forearm = copiarArquivosPositivos(linha[0], 'datasets/XR_FOREARM/dataset_treino/positivo', contador_positivo_xr_forearm , False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_forearm = copiarArquivosNegativos(linha[0], 'datasets/XR_FOREARM/dataset_treino/negativo', contador_negativo_xr_forearm, False, None)

            if(linhaDividida[2] == 'XR_HAND'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_hand  = copiarArquivosPositivos(linha[0], 'datasets/XR_HAND/dataset_treino/positivo', contador_positivo_xr_hand , False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_hand = copiarArquivosNegativos(linha[0], 'datasets/XR_HAND/dataset_treino/negativo', contador_negativo_xr_hand, False, None)

            if(linhaDividida[2] == 'XR_HUMERUS'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_humerus = copiarArquivosPositivos(linha[0], 'datasets/XR_HUMERUS/dataset_treino/positivo', contador_positivo_xr_humerus, False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_humerus = copiarArquivosNegativos(linha[0], 'datasets/XR_HUMERUS/dataset_treino/negativo', contador_negativo_xr_humerus, False, None)

            if(linhaDividida[2] == 'XR_SHOULDER'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_shoulder = copiarArquivosPositivos(linha[0], 'datasets/XR_SHOULDER/dataset_treino/positivo', contador_positivo_xr_shoulder, False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_shoulder = copiarArquivosNegativos(linha[0], 'datasets/XR_SHOULDER/dataset_treino/negativo', contador_negativo_xr_shoulder, False, None)

            if(linhaDividida[2] == 'XR_WRIST'):
                if(linha[1] == '1'): # Caso Positivo
                    print(f'\t Pasta: {linha[0]} - Positivo')
                    contador_positivo_xr_wrist = copiarArquivosPositivos(linha[0], 'datasets/XR_WRIST/dataset_treino/positivo', contador_positivo_xr_wrist, False, None)
                if(linha[1] == '0'): # Caso Negativo
                    print(f'\t Pasta: {linha[0]} - Negativo')
                    contador_negativo_xr_wrist = copiarArquivosNegativos(linha[0], 'datasets/XR_WRIST/dataset_treino/negativo', contador_negativo_xr_wrist, False, None)
                
        print(f'Total de linhas processadas: {contador_de_linhas}')
    arquivo_csv.close()

if __name__ == '__main__':
    main()