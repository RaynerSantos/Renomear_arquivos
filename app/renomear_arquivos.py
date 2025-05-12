import os
import pandas as pd
import shutil
import tempfile
import zipfile
import streamlit as st

st.title("Renomear e Mover Arquivos para Exclusão 🔍 ")

# Upload de arquivos
uploaded_zip = st.file_uploader("📁 Faça upload do ZIP com os arquivos", type="zip")
uploaded_excel = st.file_uploader("📄 Faça upload do Excel com os nomes dos arquivos a excluir", type=["xlsx"])
tipo_de_arquivo_a_exluir = st.text_input("Extensão dos arquivos a excluir (ex: .xlsx, .mp3)", placeholder=".xlsx")

if uploaded_zip and uploaded_excel and tipo_de_arquivo_a_exluir:
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extrair zip
        zip_path = os.path.join(temp_dir, "arquivos.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_zip.read())
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Lê o Excel
        df = pd.read_excel(uploaded_excel, dtype=str)
        nomes_a_excluir = set(df["Nome_Arquivo"].dropna().str.strip())

        pasta_destino = os.path.join(temp_dir, "Arquivos a Excluir")
        os.makedirs(pasta_destino, exist_ok=True)

        arquivos_encontrados = []
        arquivos_nao_encontrados = []

        for raiz, _, arquivos in os.walk(temp_dir):
            for arquivo in arquivos:
                nome_base, ext = os.path.splitext(arquivo)
                if ext.lower() == tipo_de_arquivo_a_exluir.lower() and nome_base in nomes_a_excluir:
                    caminho_origem = os.path.join(raiz, arquivo)
                    novo_nome = f"Excluir_{arquivo}"
                    caminho_destino = os.path.join(pasta_destino, novo_nome)
                    shutil.move(caminho_origem, caminho_destino)
                    arquivos_encontrados.append(arquivo)
                elif nome_base in nomes_a_excluir:
                    arquivos_nao_encontrados.append(arquivo)

        st.success(f"✅ {len(arquivos_encontrados)} arquivo(s) renomeado(s) e movido(s) com sucesso.")
        if arquivos_nao_encontrados:
            st.warning(f"⚠️ Alguns arquivos listados no Excel não têm a extensão indicada e não foram movidos.")

        # Oferecer os arquivos renomeados como zip para download
        shutil.make_archive(os.path.join(temp_dir, "resultado"), 'zip', pasta_destino)
        with open(os.path.join(temp_dir, "resultado.zip"), "rb") as f:
            st.download_button("📥 Baixar arquivos renomeados", f, file_name="Arquivos_a_Excluir.zip")
