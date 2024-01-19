import os
from typing import List

def renomear_arquivo(caminho_atual:str, novo_nome:str)-> None:
    try:
        # Concatene o caminho atual com o novo nome do arquivo
       
        novo_caminho = os.path.join(os.path.dirname(caminho_atual), novo_nome)
        print(f"{caminho_atual} {novo_caminho}")
        # Renomeie o arquivo
        if caminho_atual != novo_caminho:
            os.rename(caminho_atual, novo_caminho)

        #print(f"Arquivo renomeado com sucesso para: {novo_caminho}")
    except OSError as e:
        print(f"Erro ao renomear o arquivo: {e}")

def listar_arquivos(diretorio:str)->List:
    try:
        # Listar todos os arquivos no diretório
        arquivos = os.listdir(diretorio)
        arquivos.remove('renomear.py')
        # Imprimir os nomes dos arquivos
        print(f"Arquivos em {diretorio}:")
        for arquivo in arquivos:
            if os.path.isfile(f"{diretorio}/{arquivo}") == True :
                pass
            else:
                arquivos.remove(arquivo)
        arquivos.sort()        
        print(len(arquivos))
    except OSError as e:
        print(f"Erro ao listar arquivos: {e}")
    return arquivos

if __name__=="__main__":
    diretorio:str = './'
    arquivos:List  = listar_arquivos('./')

    i:int = 1
    nome:str=""#nome da serie
    for arq in arquivos:
        renomear_arquivo(f"./{arq}",f"{nome}S01E0{i}.mkv")
        i+=1
       