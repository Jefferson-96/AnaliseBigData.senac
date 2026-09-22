#dados.gov.br  -  *coletar dados para trabalhar*
#portaldatransparencia.gov.br / Portal da Transparência do Governo Federal 
#kaggle / Kaggle: The World's AI Proving Ground

import pandas as pd
import numpy as np
import openpyxl





#Quais são as máximas e mínimas de operação de compra e venda das transações?

df_trasacoes = pd.read_excel('base_invest.xlsx',sheet_name='Transacoes')
df_ativos = pd.read_excel('base_invest.xlsx',sheet_name='Ativo')
# print(df_trasacoes)


# df_compra = df_trasacoes[df_trasacoes['operacao'] == 'compra']
# df_venda = df_trasacoes[df_trasacoes['operacao'] == 'venda']

# max_compra_preco = df_compra['preco'].max()
# min_compra_preco = df_compra['preco'].min()
# max_compra_preco = df_venda['preco'].max()
# min_compra_preco = df_venda['preco'].min()

# print(max_compra_preco)







 #Qual CNPJ tem o ativo de maior valor?

# df_trasacoes['valor_total'] = df_trasacoes['quantidade'] *df_trasacoes['preco']

# # print(df_trasacoes)

# valor_por_ativo = df_trasacoes .groupby('id_ativo')['valor_total'].sum()
# print(valor_por_ativo)

# id_ativo_maior_valor = valor_por_ativo.idxmax()
# print(id_ativo_maior_valor)

# cnpj_maior_valor = df_ativos[df_ativos['id_ativo'] == id_ativo_maior_valor]['cnpj'] .iloc[0]
# print("---CNPJ com o ativo de maior ---")
# print(f"O CNPJ para o ativo com o maior valor total é: {cnpj_maior_valor}")
# print("\n")






#Qual valor total em transações de cada participante?


