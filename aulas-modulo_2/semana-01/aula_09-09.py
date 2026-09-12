import pandas as pd
import numpy as np


filmes = {
    'titulo': ["lagoa Azul","Agente Secreto","Gênio Indomável","A Freira","Top Gun", "Brinquedo Assassino"],
    'categoria': ["Romance","Ação","Drama","Terror","Comédia","Aventura"],
    'ano': ["1980","2025","1997","2022","1995","1986"],
    'faturamento': [6,5,4,5,5,7]
}

indices = ['A','B','C','D','E','F']

tabela_filmes = pd.DataFrame(filmes, index=indices)

# leitura_invest = pd.read_excel("base_invest.xlsx")
# print(leitura_invest)

#LOC
#ILOC
#QUERY

print(tabela_filmes)
print(type(tabela_filmes))
print(tabela_filmes)
print(type(tabela_filmes))

print(tabela_filmes.iloc[0:4])                                                           #Esse básicamente serve para "filtrar" por intervalo
print('-'*20)                                                                            #Esse ('-'*20) serve para tracejar/separar a leitura no terminal#
# print(tabela_filmes.query['titulo' !="Agente Secreto"])                                  #
print(tabela_filmes.loc['C':'F'])                                                        #Esse eu posso básicamente filtrar por um intervalo maior
print('-'*20)
print(tabela_filmes)
print('-'*20)
# < ... > ... <= ... >= ... == ... != ... and ... or ... not ... in 
consulta1 = tabela_filmes.query("faturamento == 5.5")
print(consulta1)

