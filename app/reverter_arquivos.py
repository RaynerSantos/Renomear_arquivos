import os
import streamlit as st
import shutil
import string

def prefixo_valido(prefixo):
    if not prefixo or prefixo.strip() == "":
        return False
    invalid_chars = set('<>:"/\\|?*')
    return not any(char in invalid_chars for char in prefixo)

def fazer_backup(diretorio_arquivos):
    backup_dir = diretorio_arquivos.rstrip(os.sep) + "_backup"
    if not os.path.exists(backup_dir):
        shutil.copytree(diretorio_arquivos, backup_dir)
        return backup_dir
    return None

st.title("Remover prefixo escolhido dos arquivos")

with st.form(key="remover_prefixo_form"):
    diretorio_arquivos = st.text_input(
        "📁 Caminho do diretório com os arquivos a renomear",
        help="Exemplo: C:/Users/Usuario/Downloads/Arquivos_Renomeados_Não_Enviar_25-04"
    )
    prefixo = st.text_input(
        "🔤 Prefixo a ser removido",
        help='Exemplo: "Não_Enviar_", ou qualquer outro prefixo que você deseja remover'
    )
    col1, col2 = st.columns([3, 1])
    with col2:
        processar = st.form_submit_button("Remover prefixo dos arquivos")

if processar:
    if not diretorio_arquivos or not prefixo:
        st.error("❌ Por favor, informe o diretório e o prefixo antes de processar.")
    elif not os.path.isdir(diretorio_arquivos):
        st.error("❌ O diretório informado não existe. Por favor, verifique o caminho.")
    elif not prefixo_valido(prefixo):
        st.error("❌ Prefixo inválido. Não pode ser vazio, só espaços ou conter caracteres especiais como <>:\"/\\|?*")
    else:
        backup_dir = fazer_backup(diretorio_arquivos)
        try:
            arquivos_renomeados = []
            arquivos_puloados = []
            arquivos_ignorados = []
            for raiz, _, arquivos in os.walk(diretorio_arquivos):
                for arquivo in arquivos:
                    # Ignora arquivos ocultos ou de sistema 
                    if arquivo.startswith('.') or arquivo.startswith('~'):
                        arquivos_ignorados.append(arquivo)
                        continue
                    if arquivo == prefixo:
                        arquivos_ignorados.append(arquivo)
                        continue
                    if arquivo.startswith(prefixo):
                        caminho_origem = os.path.join(raiz, arquivo)
                        novo_nome = arquivo[len(prefixo):]
                        if not novo_nome:
                            arquivos_ignorados.append(arquivo)
                            continue
                        caminho_destino = os.path.join(raiz, novo_nome)
                        if not os.path.exists(caminho_destino):
                            try:
                                os.rename(caminho_origem, caminho_destino)
                                arquivos_renomeados.append(arquivo)
                            except Exception as e:
                                arquivos_puloados.append(f"{arquivo} (erro: {e})")
                        else:
                            arquivos_puloados.append(arquivo)
            st.success(f"✅ {len(arquivos_renomeados)} arquivo(s) tiveram o prefixo removido com sucesso.")
            if arquivos_puloados:
                st.warning(f"⚠️ {len(arquivos_puloados)} arquivo(s) não puderam ser renomeados pois o nome de destino já existe ou houve erro:\n{', '.join(arquivos_puloados)}")
            if arquivos_ignorados:
                st.info(f"ℹ️ {len(arquivos_ignorados)} arquivo(s) foram ignorados (ocultos, inválidos ou só prefixo):\n{', '.join(arquivos_ignorados)}")
            if backup_dir:
                st.info(f"Backup criado em: {backup_dir}")
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar: {e}")
