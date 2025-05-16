# Renomeação de Arquivos por Código

## 1. Introdução

Esta aplicação web permite que você faça upload de uma planilha Excel contendo os códigos iniciais dos arquivos que deseja renomear em um diretório local do seu computador. A aplicação percorre o diretório informado, identifica os arquivos cujo nome começa com algum dos códigos listados na planilha e os renomeia, adicionando o prefixo `Não_Enviar_` ao nome do arquivo original.

---

## 2. Guia de Uso

### Requisitos

- **Python 3.7 ou superior**  
- **Pip** (gerenciador de pacotes do Python)
- **Bibliotecas Python necessárias:**  
  As dependências do projeto estão listadas no arquivo `requirements.txt`. Você pode instalá-las com:
  pip install -r requirements.txt

As principais bibliotecas utilizadas são:
- [streamlit](https://streamlit.io/) – para a interface web
- [pandas](https://pandas.pydata.org/) – para manipulação de dados e leitura de Excel
- [openpyxl](https://openpyxl.readthedocs.io/) – para leitura de arquivos `.xlsx`
- Outras bibliotecas padrão do Python: `os`

- **Sistema operacional:**  
Compatível com Windows, macOS e Linux.

- **Recomendação:**  
Tenha pelo menos **4GB de RAM** para processar pastas grandes com conforto.

---

## 3. Passo a passo para utilizar o aplicativo

### 3.1 Preparação dos arquivos

- **Importante:** Para manter um backup dos seus arquivos originais, mantenha uma cópia da pasta que contém todos os arquivos que podem ou não ser renomeados. Assim, você preserva os arquivos originais e pode restaurá-los se necessário.
- Prepare um arquivo Excel (`.xlsx`) contendo uma coluna chamada **CODIGO** com os códigos (iniciais do nome do arquivo) dos arquivos a serem renomeados.

### 3.2 Executando a aplicação

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

### 3.3 Utilizando a aplicação

1. Informe o caminho do diretório local onde estão os arquivos a serem renomeados.
2. Faça upload do arquivo Excel com os códigos dos arquivos a serem renomeados.
3. Clique em "Processar arquivos".
4. Os arquivos cujos nomes começam com algum dos códigos listados na planilha serão renomeados, recebendo o prefixo `Não_Enviar_` no nome.
5. Ao final, a aplicação exibirá um resumo dos arquivos renomeados e avisará caso algum código não tenha sido encontrado no diretório.

---

## Estrutura esperada do Excel

O arquivo Excel deve conter uma coluna chamada **CODIGO** com os códigos iniciais dos arquivos a serem renomeados. Exemplo:

| CODIGO      |
|-------------|
| 12345       |
| 67890       |
| ABCD        |

---

## Observações

- O diretório informado deve existir e conter os arquivos a serem renomeados.
- **Antes de processar, mantenha uma cópia da pasta original como backup.** Assim, caso precise recuperar algum arquivo ou desfazer alterações, você terá sempre uma cópia íntegra dos seus dados originais.
- Certifique-se de que os códigos no Excel correspondem exatamente ao início do nome dos arquivos no diretório.
- A aplicação não exclui arquivos, apenas renomeia os arquivos identificados no diretório informado.
- O prefixo padrão adicionado é `Não_Enviar_`, mas você pode alterar isso no código se desejar.

---
