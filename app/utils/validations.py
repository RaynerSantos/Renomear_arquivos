import os

def validar_diretorio(diretorio: str) -> bool:
    return os.path.isdir(diretorio)
