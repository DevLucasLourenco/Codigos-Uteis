import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost;"
    "Database=algumarquivo.db;"
)


conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

cursor.execute('''
               
               
               ''')


# somente no final que estas duas linhas ficam
cursor.close()
conexao.close()
