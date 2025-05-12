import os
import pandas as pd
import shutil
import re
import streamlit as st

# CSS personalizado
st.markdown(
    """
    <style>
    /* Cor de fundo da página */
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }

    /* Cor de fundo do cabeçalho */
    [data-testid="stHeader"] {
        background-color: #000000;
    }

    /* Esconde o menu lateral */
    [data-testid="stSidebar"] {
        display: none;  /* 👈 Esconde o menu lateral */
    }

    /* Remove o espaço lateral */
    [data-testid="stAppViewContainer"] > .main {
        margin-left: 0;  /* 👈 Remove o espaço lateral */
    }

    /* Cor de fundo da barra lateral */
    [data-testid="stSidebar"] {
        background-color: #333333;
    }

    /* Cor do título */
    h1 {
    color: white !important;
    text-align: center;
    font-weight: bold;
}

    /* Cor do subtítulo */
    h2 {
        color: #FFD700;
    }

    /* Cor do texto normal */
    p, span {
        color: #FFFFFF;
    }

    /* Cor dos botões */
    button {
        background-color: #20541B !important;
        color: white !important;
    }

    /* Caixa do formulário */
    div[data-testid="stForm"] {
        background-color: #1e1e1e;  /* cinza escuro */
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #444444;
        max-width: 600px;
        margin: auto;
    }

    /* Campos de texto */
    input, select, textarea {
        /* background-color: #2e2e2e !important; */
        /* color: white !important; */
        border: none !important;
        border-radius: 6px !important;
    }

    /* Botão */
    button[kind="primary"] {
        background-color: #20541B !important;
        color: white !important;
        border-radius: 8px !important;
    }

    /* table {
    background-color: #000000;
    color: white;
    border-collapse: collapse;
    width: 100%;
    border-radius: 10px;
    overflow: hidden;
    font-size: 14px;
    }
    th, td {
        border: 1px solid #333;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #111111;
        color: #FFFFFF;
    }
    tr:nth-child(even) {
        background-color: #1c1c1c;
    } */
    </style>
    """,
    unsafe_allow_html=True
)

#=== Título ===#
st.title("Renomear Arquivos")
st.write("")
st.write("")
st.write("")

# Exemplo da planilha a ser preenchida
st.markdown(
    """
    A planilha em excel deverá conter na coluna "Nome_Arquivo" os nomes dos arquivos que deverão ser renomeados.
    📥 [Exemplo da planilha](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FRaynerSantos%2FRenomear_arquivos%2Frefs%2Fheads%2Fmain%2FRenomear%2FArquivos_Excluir.xlsx&wdOrigin=BROWSELINK)
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")

st.markdown(
    """
    <h5 style="color: white; text-align: center;">
        📝 Preencha as informações abaixo para renomear os arquivos que deseja excluir
    </h5>
    """,
    unsafe_allow_html=True
)

with st.form(key="renomear_arquivos_a_excluir"):
    caminho_arquivos = st.text_input(label="Informe o caminho dos arquivos que deseja renomear", 
                                     placeholder="C:\PROJETOS\Renomear_arquivos\Renomear")
    arquivo_excel = st.text_input(label="Informe o caminho do excel que encontra o nome dos arquivos que serão excluídos",
                                  placeholder="C:\PROJETOS\Renomear_arquivos\Renomear\Arquivos_Excluir.xlsx")
    # tipo_de_arquivo_a_exluir = st.text_input(label="Informe o tipo de arquivo que será excluído", placeholder='Exemplo: .xlsx | .mp3 | .txt')
    tipo_de_arquivo_a_exluir = st.selectbox(label="Informe o tipo de arquivo que será excluído", options=[".xlsx",".mp3",".WAV",".txt"])
    input_buttom_submit = st.form_submit_button("✔️ Renomear")

###=== Código para renomear arquivos que serão excluídos ===###
# tipo_de_arquivo_a_exluir = '.xlsx'

# caminho_arquivos = r"C:\PROJETOS\Renomear_arquivos\Renomear"
# arquivo_excel = r"C:\PROJETOS\Renomear_arquivos\Renomear\Arquivos_Excluir.xlsx"

if input_buttom_submit:
    cont_renomeados = 0
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
                cont_renomeados += 1

        except Exception as e:
            print(f"Erro inesperado ao processar {arquivo}: {e}, {type(e)=}")
            st.error(f"❌ Arquivos não renomeados. Erro inesperado {arquivo}: {e}, {type(e)=}")

    st.success(f"✅ {cont_renomeados} arquivos renomeados com sucesso!")

    
