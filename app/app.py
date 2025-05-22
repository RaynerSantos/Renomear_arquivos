import streamlit as st
from core.planilha import ler_codigos_excel
from core.arquivos import renomear_arquivos
from utils.validations import validar_diretorio

def main():
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
        A planilha em excel deverá conter na coluna "CODIGO" os códigos iniciais dos arquivos que deverão ser renomeados.
        📥 [Exemplo da planilha](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FRaynerSantos%2FRenomear_arquivos%2Frefs%2Fheads%2Fmain%2FRenomear%2FArquivos_Excluir.xlsx&wdOrigin=BROWSELINK)
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    with st.form(key="processamento_form"):
        diretorio_arquivos = st.text_input("📁 Caminho do diretório com os arquivos a renomear")
        uploaded_excel = st.file_uploader("📄 Faça upload do Excel com os nomes dos arquivos a renomear", type=["xlsx"])
        col1, col2 = st.columns([3, 1])
        with col2:
            processar = st.form_submit_button("Processar arquivos")

    if processar:
        if not diretorio_arquivos or not uploaded_excel:
            st.error("❌ Informe o diretório e o Excel antes de processar.")
        elif not validar_diretorio(diretorio_arquivos):
            st.error("❌ O diretório informado não existe.")
        else:
            try:
                codigos = ler_codigos_excel(uploaded_excel)
            except Exception as e:
                st.error(str(e))
                return
            
            if codigos:
                try:
                    arquivos_renomeados, nomes_encontrados = renomear_arquivos(diretorio_arquivos, codigos)
                    arquivos_nao_encontrados = codigos - nomes_encontrados

                    st.success(f"✅ {len(arquivos_renomeados)} arquivo(s) renomeado(s).")
                    if arquivos_nao_encontrados:
                        st.warning(f"⚠️ Códigos não encontrados: {', '.join(arquivos_nao_encontrados)}")
                except Exception as e:
                    st.error(str(e))

if __name__ == "__main__":
    main()
