import os
import pandas as pd
import shutil
import tempfile
import zipfile
import streamlit as st
from pathlib import Path

st.title("Renomear e mover arquivos 🔍")

# Upload de múltiplos arquivos ZIP
uploaded_zips = st.file_uploader(
    "📁 Faça upload de um ou mais arquivos ZIP", 
    type=["zip"], 
    accept_multiple_files=True
)
uploaded_excel = st.file_uploader(
    "📄 Faça upload do Excel com os nomes dos arquivos a excluir", 
    type=["xlsx"]
)
tipo_de_arquivo_a_excluir = st.text_input(
    "Extensão dos arquivos a excluir (ex: .xlsx, .mp3)", 
    placeholder=".xlsx"
)

if uploaded_zips and uploaded_excel and tipo_de_arquivo_a_excluir:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extrai todos os ZIPs enviados
        for idx, uploaded_zip in enumerate(uploaded_zips):
            zip_path = os.path.join(temp_dir, f"arquivo_{idx}.zip")
            with open(zip_path, "wb") as f:
                f.write(uploaded_zip.read())
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            os.remove(zip_path)  # Remove o ZIP após extrair

        # Lê o Excel
        df = pd.read_excel(uploaded_excel, dtype=str)
        nomes_a_excluir = set(df["Nome_Arquivo"].dropna().str.strip())

        # Cria a pasta de destino na raiz do projeto
        raiz_projeto = Path().resolve()
        pasta_destino = raiz_projeto / "Arquivos a Excluir"
        pasta_destino.mkdir(exist_ok=True)  # Cria se não existir

        arquivos_encontrados = []
        arquivos_nao_encontrados = []

        for raiz, _, arquivos in os.walk(temp_dir):
            # Ignora a pasta de destino usando caminho absoluto
            if os.path.abspath(raiz) == os.path.abspath(pasta_destino):
                continue
            for arquivo in arquivos:
                nome_base, ext = os.path.splitext(arquivo)
                if ext.lower() == tipo_de_arquivo_a_excluir.lower() and nome_base in nomes_a_excluir:
                    caminho_origem = os.path.join(raiz, arquivo)
                    novo_nome = f"Excluir_{arquivo}"
                    caminho_destino_final = pasta_destino / novo_nome
                    shutil.move(caminho_origem, str(caminho_destino_final))
                    arquivos_encontrados.append(arquivo)
                elif nome_base in nomes_a_excluir:
                    arquivos_nao_encontrados.append(arquivo)

        st.success(f"✅ {len(arquivos_encontrados)} arquivo(s) renomeado(s) e movido(s) com sucesso.")
        if arquivos_nao_encontrados:
            st.warning(f"⚠️ Alguns arquivos listados no Excel não têm a extensão indicada e não foram movidos.")
