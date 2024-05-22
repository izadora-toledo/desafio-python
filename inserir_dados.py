import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('faturas.db')

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Dados fictícios para serem inseridos
faturas_dados = [
    ('eyinr1f4ek7v6ggdd6x90d', '2024-04-26', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/10.jpg'),
    ('pjbpkw7sb2e5ydrgddy59', '2024-07-18', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/2.jpg'),
    ('b7vmzeu68egqmmljtau90i', '2024-04-12', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/11.jpg'),
    ('m9gf85a4qve9vc7ks1i41t', '2024-06-04', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/6.jpg'),
    ('pxrc2nmcgzr0ji9uzr7kv7', '2024-05-27', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/5.jpg'),
    ('gbh1nyjhk9jprejg45un4', '2024-07-20', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/3.jpg'),
    ('phe5wzq3xa76r36gv6m0e', '2024-05-15', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/8.jpg'),
    ('5ofji3nmpe2e1mg0to1tku', '2024-05-24', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/4.jpg'),
    ('na7hefmqqbscl1hkvyt4k4', '2024-04-08', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/7.jpg'),
    ('7i7lqvqrcbhstwegmazmh', '2024-05-05', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/12.jpg'),
    ('bxt0ej8kmk726dmo6xck1i', '2024-04-26', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/9.jpg'),
    ('bl8f16jd1pnaeyqxrbyzd', '2024-07-18', 10021, '13-02-2019', 'Sit Amet Corp.', 1234.40, 'rpachallengeocr.azurewebsites.net/invoices/1.jpg')   
]

# Instrução SQL para inserir dados na tabela
sql = '''INSERT INTO faturas (ID, DueDate, InvoiceNo, InvoiceDate, CompanyName, TotalDue, InvoiceURL)
         VALUES (?, ?, ?, ?, ?, ?, ?)'''

# Insere cada registro na tabela faturas
for fatura in faturas_dados:
    try:
        cursor.execute(sql, fatura)
    except sqlite3.IntegrityError:
        # Se a chave primária (ID) já existir, ignora o erro e não insere o registro duplicado
        print(f"Registro com ID {fatura[0]} já existe.")

# Salva as alterações
conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
