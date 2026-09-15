import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

# dados = np.array ([12,15,17,20,22,25,28,30,35,40])
# print(dados)

# #CALCULARQUARTIS

# q1 = np.percentile(dados,25) 
# q2 = np.percentile(dados,50)
# q3 = np.percentile(dados,75)

# print(f"primeiro quartil (Q1:(q1)")
# print(f"segundo quartil {Q2,mediana} : (Q2:(q2)")
# print(f"terceiro quartil (Q3:(q3)")

df_trasacoes = pd.read_excel('base_invest.xlsx',sheet_name='Transacoes')
print(df_trasacoes.head(10))

q1_preco = df_trasacoes['preco'].quantile(0.25)
q2_preco = df_trasacoes['preco'].quantile(0.50)
q3_preco = df_trasacoes['preco'].quantile(0.75)

print(f"Preço Q1: {q1_preco}")
print(f"Preço Mediana (Q2): {q2_preco}")
print(f"Preço Q3: {q3_preco}")

contagem_operacao = df_trasacoes ['operacao'].value_counts()

#CRIAR UM GRAFICO DE BARRAS
contagem_operacao.plot(kind='bar',title='Tipos de Operação')

#MOSTRAR O GRÁFICO
plt.show()

