## Desafio-python

O objetivo deste desafio é criar um fluxo de trabalho que fará a leitura de todas as linhas da tabela e fará o download das respectivas faturas cujas datas de vencimento são iguais ou anteriores à data atual.

1. **banco.py**: Cria o banco de dados SQLite e a tabela `faturas` para armazenar informações sobre as faturas.
2. **inserir_dados.py**: Insere dados fictícios na tabela `faturas` no banco de dados SQLite.
3. **arquivo_csv.py**: Gera um arquivo CSV contendo informações sobre as faturas cujas datas de vencimento são iguais ou anteriores à data atual.

### Pré-requisitos

Antes de executar o projeto, você precisa ter o Python instalado em seu sistema. Você pode baixar e instalar o Python no [site oficial do Python](https://www.python.org/).

### Passo a Passo para Execução do Projeto

1. **Clonar o Repositório:**
   - Clone este repositório em sua máquina local usando o seguinte comando: git clone <URL_do_repositório>

2. **Executar o Script para Criar o Banco de Dados:**
- Abra o terminal (ou prompt de comando) e navegue até o diretório do projeto.
- Execute o seguinte comando para criar o banco de dados e a tabela faturas: python banco.py

3. **Inserir Dados Fictícios no Banco de Dados:**
- Execute o script `inserir_dados.py` para inserir dados fictícios na tabela `faturas`: python inserir_dados.py

4. **Gerar Arquivo CSV de Faturas Vencidas:**
- Execute o script `arquivo_csv.py` para gerar um arquivo CSV contendo informações sobre as faturas: python arquivo_csv.py

5. **Verificar o Arquivo CSV Gerado:**
- Após a execução bem-sucedida, verifique o diretório de downloads do seu sistema para encontrar o arquivo CSV `faturas_vencidas.csv` contendo os dados das faturas vencidas.

### Nota Importante

- Os arquivos CSV são gerados no diretório de downloads padrão do seu sistema operacional.

Foi uma honra fazer esse projeto.






