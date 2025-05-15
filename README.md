# Renomear e Mover Arquivos para Exclusão

Esta aplicação web permite que você faça upload de arquivos ZIP contendo documentos, planilhas ou outros arquivos, além de um arquivo Excel com os nomes dos arquivos que deseja marcar para exclusão. A aplicação extrai os arquivos ZIP, identifica os arquivos a serem renomeados com base na planilha Excel, renomeia esses arquivos (adicionando o prefixo `Excluir_`) e os move para uma pasta chamada **Arquivos a Excluir** na raiz do projeto.

## Requisitos

Para executar este projeto, você precisará dos seguintes requisitos instalados em sua máquina:

- **Python 3.7 ou superior**  
  [Download Python](https://www.python.org/downloads/)

## Como funciona

1. **Preparação dos arquivos**
  - **Importante:** Para manter um backup dos seus arquivos originais, mantenha a pasta que contém todos os arquivos que podem ou não ser renomeados. Assim, você preserva os arquivos originais e envia apenas uma cópia compactada para o processamento.
  - Faça upload de um ou mais arquivos ZIP contendo os arquivos que deseja processar.
  - Faça upload de um arquivo Excel (`.xlsx`) contendo uma coluna chamada `Nome_Arquivo` com os nomes (sem extensão) dos arquivos a serem marcados para exclusão.
  - Informe a extensão dos arquivos que deseja excluir (exemplo: `.xlsx`, `.pdf`, `.mp3`).

2. **Processamento**
  - Os arquivos ZIP são extraídos em uma área temporária.
  - O Excel é lido e os nomes dos arquivos a serem excluídos são identificados.
  - Para cada arquivo extraído cujo nome base (sem extensão) corresponda a um nome listado no Excel e cuja extensão seja a informada, o arquivo é renomeado (prefixado com `Excluir_`) e movido para a pasta **Arquivos a Excluir** na raiz do projeto.

3. **Resultado**
  - Ao final, a aplicação informa quantos arquivos foram encontrados, renomeados e movidos.
  - Os arquivos renomeados ficam disponíveis na pasta **Arquivos a Excluir**.

## Como usar

1. Clone ou baixe este repositório.
2. Instale as dependências:
  ```
  pip install -r requirements.txt
  ```
3. Execute a aplicação:
  ```
  streamlit run renomear_arquivos.py
  ```
4. Acesse o endereço exibido pelo Streamlit (geralmente http://localhost:8501) no seu navegador.
5. Siga as instruções na tela para:
  - Compactar a pasta de arquivos originais em um ZIP e fazer o upload desse ZIP.
  - Fazer upload do Excel com os nomes dos arquivos a excluir.
  - Informar a extensão dos arquivos a serem excluídos.
6. Após o processamento, verifique a pasta **Arquivos a Excluir** criada na raiz do projeto para encontrar os arquivos renomeados.

## Estrutura esperada do Excel

O arquivo Excel deve conter uma coluna chamada **Nome_Arquivo** com os nomes base (sem extensão) dos arquivos a serem excluídos. Exemplo:

| Nome_Arquivo   |
|----------------|
| arquivo1       |
| documento2     |
| musica_teste   |

## Observações

- Apenas arquivos ZIP podem ser enviados para upload.
- **Antes de fazer o upload, compacte a pasta de arquivos originais em um arquivo ZIP e mantenha essa pasta original guardada em um local seguro como backup.** Assim, caso precise recuperar algum arquivo ou desfazer alterações, você terá sempre uma cópia íntegra dos seus dados originais.
- A pasta **Arquivos a Excluir** será criada automaticamente na raiz do projeto.
- Certifique-se de que os nomes no Excel correspondam exatamente aos nomes dos arquivos (sem extensão) presentes nos arquivos ZIP.
- A aplicação não exclui arquivos originais, apenas move e renomeia os arquivos identificados a partir do ZIP enviado.

---
