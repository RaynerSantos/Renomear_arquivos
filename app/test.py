import os
import pandas as pd
import shutil
import re

###=== Código para renomear arquivos que serão excluídos ===###
tipo_de_arquivo_a_exluir = '.xlsx'

caminho_arquivos = r"C:\PROJETOS\Renomear_arquivos\Renomear"
arquivo_excel = r"C:\PROJETOS\Renomear_arquivos\Renomear\Arquivos_Excluir.xlsx"

# Caminho da nova pasta onde os arquivos renomeados serão movidos
pasta_destino = os.path.join(caminho_arquivos, "Arquivos a Excluir")
os.makedirs(pasta_destino, exist_ok=True)

df = pd.read_excel(arquivo_excel, dtype=str)  # Garante que todas as colunas sejam strings

arquivos = os.listdir(caminho_arquivos)
for arquivo in arquivos:
    caminho_subarquivos = os.path.join(caminho_arquivos, arquivo)
    nome_atual = arquivo.split(".")[0]
    nome_atual = os.path.splitext(nome_atual)[0]

    # Verificar se arquivo está no excel
    try:
        if (df["Nome_Arquivo"] == nome_atual).any():
            novo_nome = f"Excluir_{nome_atual}{tipo_de_arquivo_a_exluir}"
            novo_caminho = os.path.join(pasta_destino, novo_nome)
            
            # Renomear e mover
            shutil.move(caminho_subarquivos, novo_caminho)

        else:
            print(f"Arquivo '{arquivo}' não renomeado.")
    except Exception as e:
        print(f"Erro inesperado ao processar {arquivo}: {e}, {type(e)=}")
