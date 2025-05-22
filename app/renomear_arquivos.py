import os
import pandas as pd
import streamlit as st

st.title("Renomeação de arquivos 🔍")

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
    A planilha em excel deverá conter na coluna "CODIGO" os codigos iniciais dos arquivos que deverão ser renomeados.
    📥 [Exemplo da planilha](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FRaynerSantos%2FRenomear_arquivos%2Frefs%2Fheads%2Fmain%2FRenomear%2FArquivos_Excluir.xlsx&wdOrigin=BROWSELINK)
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.write("")

with st.form(key="processamento_form"):
    diretorio_arquivos = st.text_input(
        "📁 Caminho do diretório com os arquivos a renomear",
        help="Exemplo: C:/Users/Usuario/Downloads/MeusArquivos"
    )
    uploaded_excel = st.file_uploader(
        "📄 Faça upload do Excel com os nomes dos arquivos a renomear",
        type=["xlsx"]
    )
    col1, col2 = st.columns([3, 1])
    with col2:
        processar = st.form_submit_button("Processar arquivos")

if processar:
    if not diretorio_arquivos or not uploaded_excel:
        st.error("❌ Por favor, informe o diretório e faça upload do Excel antes de processar.")
    elif not os.path.isdir(diretorio_arquivos):
        st.error("❌ O diretório informado não existe. Por favor, verifique o caminho.")
    else:
        try:
            # Lê o Excel
            df = pd.read_excel(uploaded_excel, dtype=str)
            if "CODIGO" not in df.columns:
                st.error("❌ A coluna 'CODIGO' não foi encontrada no Excel.")
            else:
                nomes_a_renomear = set(df["CODIGO"].dropna().str.strip())

                arquivos_renomeados = set()
                nomes_encontrados = set()

                for raiz, _, arquivos in os.walk(diretorio_arquivos):
                    for arquivo in arquivos:
                        nome_base, ext = os.path.splitext(arquivo)
                        for codigo in nomes_a_renomear:
                            if nome_base.startswith(str(codigo)):
                                caminho_origem = os.path.join(raiz, arquivo)
                                novo_nome = f"Não_Enviar_{arquivo}"
                                caminho_destino = os.path.join(raiz, novo_nome)
                                os.rename(caminho_origem, caminho_destino)
                                arquivos_renomeados.add(arquivo)
                                nomes_encontrados.add(codigo)
                                break  

                arquivos_nao_encontrados = nomes_a_renomear - nomes_encontrados

                st.success(f"✅ {len(arquivos_renomeados)} arquivo(s) renomeado(s) com sucesso.")
                if arquivos_nao_encontrados:
                    st.warning(
                        f"⚠️ Os seguintes códigos listados no Excel não foram encontrados no diretório:"
                        f"\n\n{', '.join(arquivos_nao_encontrados)}"
                    )
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar: {e}")
