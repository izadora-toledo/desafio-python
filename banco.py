import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('faturas.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela de faturas com as colunas especificadas
cursor.execute('''CREATE TABLE faturas (
                    ID TEXT PRIMARY KEY,  
                    DueDate TEXT,        
                    InvoiceNo INTEGER,   
                    InvoiceDate TEXT,    
                    CompanyName TEXT,    
                    TotalDue REAL,
                    InvoiceURL TEXT        
                    )''')

# Salva as alterações
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
