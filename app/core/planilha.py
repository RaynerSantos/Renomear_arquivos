import pandas as pd

def ler_codigos_excel(uploaded_excel) -> set:
    try:
        df = pd.read_excel(uploaded_excel, dtype=str)
    except Exception as e:
        raise ValueError(f"Erro ao ler o Excel: {e}")

    if "CODIGO" not in df.columns:
        raise ValueError("A coluna 'CODIGO' não foi encontrada no Excel.")
    
    return set(df["CODIGO"].dropna().str.strip())
