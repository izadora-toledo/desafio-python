import os
import sqlite3
import csv
from datetime import datetime

# Conectar-se ao banco de dados SQLite
conn = sqlite3.connect('faturas.db')
cursor = conn.cursor()

# Definir o nome do arquivo CSV
nome_arquivo_csv = 'faturas_vencidas.csv'

# Obter o diretório de downloads padrão do Windows
diretorio_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

# Caminho completo do arquivo CSV
caminho_arquivo_csv = os.path.join(diretorio_downloads, nome_arquivo_csv)

# Abrir o arquivo CSV em modo de escrita
with open(caminho_arquivo_csv, 'w', newline='') as csvfile:
    # Criar o objeto escritor CSV
    csv_writer = csv.writer(csvfile)

    # Escrever o cabeçalho do arquivo CSV
    csv_writer.writerow(['ID', 'Due Date', 'Invoice URL'])

    # Obter a data atual
    hoje = datetime.now().strftime('%Y-%m-%d')

    # Consultar o banco de dados para obter apenas as faturas cuja data de vencimento é hoje ou passada
    cursor.execute("SELECT ID, DueDate, InvoiceURL FROM faturas WHERE DueDate <= ?", (hoje,))
    
    faturas_vencidas = cursor.fetchall()

    # Iterar sobre as faturas vencidas e escrever no arquivo CSV
    for fatura in faturas_vencidas:
        # Formatar a data para 'dd-mm-yyyy'
        fatura_com_data_formatada = (fatura[0], datetime.strptime(fatura[1], '%Y-%m-%d').strftime('%d-%m-%Y'), fatura[2])
        # Escrever os dados no arquivo CSV
        csv_writer.writerow(fatura_com_data_formatada)

# Fechar a conexão com o banco de dados
conn.close()

# Exibir o caminho completo do arquivo CSV criado
print(f'Arquivo CSV "{nome_arquivo_csv}" criado com sucesso em: {caminho_arquivo_csv}')
