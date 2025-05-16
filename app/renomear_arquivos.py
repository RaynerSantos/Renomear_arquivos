import os
import pandas as pd
import shutil
import tempfile
import zipfile
import streamlit as st
from pathlib import Path

st.title("Renomeação de arquivos 🔍")

# Exemplo da planilha a ser preenchida
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] { background-color: #000000; }
    [data-testid="stHeader"] { background-color: #000000; }
    [data-testid="stSidebar"] { background-color: #333333; }
    h1 { color: #20541B; text-align: center; }
    h2 { color: #FFD700; }
    p, span { color: #FFFFFF; }
    button { background-color: #20541B !important; color: white !important; }
    div[data-testid="stDropdownMenu"] * { color: black !important; }
    div[data-testid="stDropdownMenu"] { background-color: white !important; }
    </style>
    A planilha em excel deverá conter na coluna "Nome_Arquivo" os nomes dos arquivos que deverão ser renomeados.
    📥 [Exemplo da planilha](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FRaynerSantos%2FRenomear_arquivos%2Frefs%2Fheads%2Fmain%2FRenomear%2FArquivos_Excluir.xlsx&wdOrigin=BROWSELINK)
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.write("")

with st.form(key="processamento_form"):
    uploaded_zips = st.file_uploader(
        "📁 Faça upload de um ou mais arquivos ZIP", 
        type=["zip"], 
        accept_multiple_files=True
    )
    uploaded_excel = st.file_uploader(
        "📄 Faça upload do Excel com os nomes dos arquivos a excluir", 
        type=["xlsx"]
    )
    tipo_de_arquivo_a_excluir = st.selectbox(
        "Extensão dos arquivos a excluir (ex: .xlsx, .mp3)", 
        options=[".xlsx", ".mp3", ".txt", ".csv", ".jpg", ".png", ".pdf"]
    )
    # Alinha o botão à direita usando colunas
    col1, col2 = st.columns([3, 1])
    with col2:
        processar = st.form_submit_button("Processar arquivos")

# Validação dos uploads
if processar:
    if not uploaded_zips or not uploaded_excel:
        st.error("❌ Por favor, faça upload de pelo menos um arquivo ZIP e um arquivo Excel antes de processar.")
    else:
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
