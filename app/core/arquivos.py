import os

def renomear_arquivos(diretorio: str, codigos: set, prefixo: str = "Não_Enviar_") -> tuple:
    arquivos_renomeados = set()
    nomes_encontrados = set()

    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            nome_base, ext = os.path.splitext(arquivo)
            for codigo in codigos:
                if nome_base.startswith(str(codigo)):
                    caminho_origem = os.path.join(raiz, arquivo)
                    novo_nome = f"{prefixo}{arquivo}"
                    caminho_destino = os.path.join(raiz, novo_nome)

                    if not os.path.exists(caminho_destino):
                        try:
                            os.rename(caminho_origem, caminho_destino)
                            arquivos_renomeados.add(arquivo)
                            nomes_encontrados.add(codigo)
                        except Exception as e:
                            raise RuntimeError(f"Erro ao renomear '{arquivo}': {e}")
                    break
    return arquivos_renomeados, nomes_encontrados
