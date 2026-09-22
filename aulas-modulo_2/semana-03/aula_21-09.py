import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import mysql.connector


# 1 conectar ao banco de dados

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "meu_ecommerce"
)

# 2 criar um objeto cursor para executar as queris
cursor = conexao.cursor()

# 3 Executar a Query
query = "SELECT * "
 
 # 3. Definir a query
query = "SELECT * FROM produtos"

# 4. Executar a query
cursor.execute(query)

# 5. Obter os resultados
resultados = cursor.fetchall()

# 6. Exibir os resultados
for linha in resultados:
    print(linha)

# 7. Fechar a conexão
cursor.close()
conexao.close()