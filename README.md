# Renomeação e Movimentação de Arquivos por Código

## 1. Introdução

Esta aplicação web permite que você:
1. Renomeie arquivos de um diretório adicionando o prefixo `Enviar_` com base em códigos listados em uma planilha Excel
2. Opcionalmente, mova os arquivos renomeados para um diretório específico
3. Mantenha o controle de arquivos não encontrados e conflitos de renomeação

---

## 2. Guia de Uso

### Requisitos

- **Python 3.7 ou superior**  
- **Pip** (gerenciador de pacotes do Python)
- **Bibliotecas Python necessárias:**  
pip install -r requirements.txt

Principais bibliotecas:
- `streamlit` - Interface web
- `pandas` - Manipulação de dados
- `openpyxl` - Leitura de arquivos Excel
- `shutil` - Movimentação de arquivos
- Bibliotecas padrão: `os`, `sys`

- **Sistema operacional:**  
Compatível com Windows, macOS e Linux

---

## 3. Funcionamento

### Fluxo Principal:
1. **Leitura do Excel** com códigos na coluna "CODIGO"
2. **Renomeação de arquivos** que começam com os códigos listados
3. **Movimentação opcional** dos arquivos renomeados para diretório específico

### 3.1 Preparação
- Mantenha backup dos arquivos originais
- Prepare um Excel com a coluna "CODIGO"
- Defina:
  - Diretório origem: onde estão os arquivos originais
  - Diretório destino (opcional): para onde os arquivos renomeados serão movidos

### 3.2 Execução
  streamlit run renomear_arquivos.py
  
### 3.3 Interface
1. Informe:
   - Caminho do diretório origem
   - Arquivo Excel com códigos
   - (Opcional) Caminho do diretório destino
2. Clique em "Processar arquivos"

---

## 4. Estrutura do Excel

| CODIGO      |
|-------------|
| 12345       |
| 67890       |
| ABCD        |

---

## 5. Resultados Esperados

- Arquivos renomeados com prefixo `Enviar_` no diretório origem
- Se informado diretório destino:
  - Arquivos movidos mantendo o novo nome
  - Pasta criada automaticamente se não existir
- Relatório detalhado:
  - ✅ Arquivos processados com sucesso
  - ⚠️ Códigos não encontrados
  - ❌ Erros de processamento

---

## 6. Observações Importantes

1. **Prefixo Dinâmico:**  
   O prefixo `Enviar_` é adicionado apenas aos arquivos cujos códigos estão no Excel

2. **Movimentação Segura:**  
   - Arquivos não são sobrescritos no destino
   - Conflitos geram alertas detalhados

3. **Compatibilidade:**  
   - Funciona com arquivos em subdiretórios
   - Ignora arquivos ocultos e de sistema

4. **Recomendações:**  
   - Sempre verifique o diretório destino antes de processar
   - Use caminhos absolutos para evitar erros
   - Mantenha backups regulares dos arquivos originais

---

## 7. Customização

Para alterar o prefixo padrão (`Enviar_`), modifique a linha:<br>
novo_nome = f"Enviar_{arquivo}" no código fonte para o prefixo desejado.

## 8. Remoção de Prefixo dos Arquivos

Além da renomeação e movimentação, a aplicação conta com um módulo para **remover prefixos indesejados** de arquivos em lote. Esse recurso é útil para restaurar arquivos ao seu nome original, caso eles tenham sido previamente marcados com um prefixo como `Não_Enviar_`, `Enviar_` ou qualquer outro.

### Como funciona

- O usuário informa o diretório onde estão os arquivos e o prefixo a ser removido.
- O sistema faz um **backup automático** da pasta antes de qualquer alteração.
- São ignorados arquivos ocultos, de sistema ou cujo nome seja apenas o prefixo.
- Arquivos que já existam com o nome de destino não são sobrescritos.
- Um relatório detalhado é exibido ao final, com:
    - Arquivos renomeados
    - Arquivos pulados (por conflito de nome ou erro)
    - Arquivos ignorados (ocultos, inválidos, etc.)
    - Caminho do backup criado

### Exemplo de uso

1. Execute o script de remoção de prefixo:
    ```
    streamlit run reverter_arquivos.py
    ```
2. Preencha:
    - Caminho do diretório com os arquivos a serem processados
    - Prefixo a ser removido (ex: `Não_Enviar_`)
3. Clique em "Remover prefixo dos arquivos"

### Principais recursos de robustez

- **Validação do prefixo:** Não permite prefixos vazios, só espaços ou com caracteres inválidos.
- **Backup automático:** Antes de qualquer alteração, a pasta é copiada para um diretório de backup.
- **Relatórios claros:** O usuário vê exatamente o que foi alterado, pulado ou ignorado.
- **Proteção contra sobrescrita:** Nunca sobrescreve arquivos já existentes.

### Exemplo de mensagem de sucesso

✅ 5 arquivo(s) tiveram o prefixo removido com sucesso.<br>
ℹ️ 1 arquivo(s) foram ignorados (ocultos, inválidos ou só prefixo): .DS_Store<br>
⚠️ 1 arquivo(s) não puderam ser renomeados pois o nome de destino já existe ou houve erro: Enviar_relatorio.pdf<br>
Backup criado em: C:/Users/Usuario/Downloads/Arquivos_Renomeados_Não_Enviar_25-04_backup


---

**Dica:**  
Utilize este recurso sempre que precisar "liberar" arquivos para envio ou restaurar nomes originais após uma triagem.
