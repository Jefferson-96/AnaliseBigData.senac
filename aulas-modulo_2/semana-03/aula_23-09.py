import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import mysql.connector

# lista_numeros = [10, 20, 30, 40, 50]
# meu_array = np.array(lista_numeros)

# print(meu_array)
# # Saída: [10 20 30 40 50]
# print(type(meu_array))
# # Saída: <class 'numpy.ndarray'>

# # Comparando com uma série do Pandas
# minha_serie = pd.Series(lista_numeros)
# print(minha_serie)
# print(type(minha_serie))

# ####################################################

# # Extraindo a coluna 'preco' do arquivo vendas_produtos.csv com Numpy
# precos_array = np.genfromtxt('../semana-02/vendas_produtos.csv', skip_header=1, dtype=None, encoding='utf-8', delimiter=',', usecols=3)
# print(precos_array)
# print(type(precos_array))

# # Calcule a média:
# media = np.mean(precos_array)
# print(f"Média dos preços: R$ {media:.2f}")


# # Obtenha a mediana:
# mediana = np.median(precos_array)
# print(f"Mediana dos preços: R$ {mediana:.2f}")


# # Calcule a distância entre a média e a mediana:
# distancia = (media - mediana) / mediana
# print(f"Distância entre a média e a mediana: {distancia * 100:.2f}%")

# if abs(distancia) <= 0.10:
#     print("A média tende a ser uma medida de tendência central confiável.")
# elif abs(distancia) < 0.25:
#     print("A média pode estar sofrendo uma influência moderada de valores extremos.")
# else:
#     print("A média tende a não ser uma medida de tendência central confiável.")

# # Verificando a direção da influência
# if media > mediana:
#     print("A influência é dos valores mais altos da distribuição.")
# elif media < mediana:
#     print("A influência é dos valores mais baixos da distribuição.")

# # Visualizando a distribuição dos preços
# import matplotlib.pyplot as plt  # Importando a biblioteca Matplotlib
# import seaborn as sns  # Importando a biblioteca Seaborn    

# sns.histplot(precos_array, kde=True) # kde=True adiciona a curva de densidade, traduzindo seria "Kernel Density Estimate"
# plt.title('Distribuição dos Preços dos Produtos')
# plt.show()  



###########################################################################################################################################################################################################################################
                                                                           #SEGUNDO TRATAMENTO#


# 1: LEITURA SEM PERDAS
# Se o CSV está quebrado (como a linha do Lucas Ferrão com 6 colunas em vez de 5),
# nós lemos o arquivo linha por linha e corrigimos o erro de separador decimal.

linhas_corrigidas = []
with open('treinamento_alunos.csv', 'r', encoding='latin1') as file:
    for linha in file:
        partes = linha.strip().split(',')
        
        # Se a linha tem 6 partes, é o erro do '850,00'. Vamos unir a parte 4 e 5.
        if len(partes) == 6:
            # Junta o '850' com '00' usando um ponto
            nova_linha = partes[:3] + [f"{partes[3]}.{partes[4]}"] + [partes[5]]
            linhas_corrigidas.append(nova_linha)
        else:
            linhas_corrigidas.append(partes)

# Criamos o DataFrame a partir da lista corrigida
df = pd.DataFrame(linhas_corrigidas[1:], columns=linhas_corrigidas[0])

print(f"Total de linhas carregadas: {len(df)}")
print(df.head())

# 2: RENOMEAR COLUNAS
df.columns = ['id', 'nome', 'data_nasc', 'mensalidade', 'curso']

# 3: TRATAR ENCODING
# Corrigindo os nomes e cursos que vieram como \xc3\xa9
def fix_encoding(text):
    if pd.isna(text) or text == '': return text
    try:
        # Tenta decodificar o que foi lido como string literal
        return text.encode('latin-1').decode('utf-8')
    except:
        return text

df['nome'] = df['nome'].apply(fix_encoding).str.strip()
df['curso'] = df['curso'].apply(fix_encoding).str.strip()

# 4: LIMPEZA DE CARACTERES
# Em vez de converter direto, limpamos tudo que não é número ou ponto
df['mensalidade'] = (
    df['mensalidade']
    .str.replace('R$', '', regex=False)
    .str.replace('.', '', regex=False) # Remove ponto de milhar
    .str.replace(',', '.')             # Troca vírgula decimal por ponto
    .str.strip()
)

# 5: MUDANÇA DE TIPOS
# Mudamos para numérico. Onde não for possível, ele vira NaN (vazio), mas a LINHA FICA.
df['mensalidade'] = pd.to_numeric(df['mensalidade'], errors='coerce')
df['id'] = pd.to_numeric(df['id'], errors='coerce')

df['data_nasc'] = pd.to_datetime(df['data_nasc'], dayfirst=True, errors='coerce')

# 6: TRATAR VALORES NULOS
# Em vez de dropna(), preenchemos com valores padrão para manter a linha
df['nome'] = df['nome'].replace('', 'NOME NÃO INFORMADO')
df['data_nasc'] = df['data_nasc'].fillna('DATA INVÁLIDA') # Vira string para manter o aviso

# 7: ANALISAR COM DESCRIBE
print("\n--- RESUMO ESTATÍSTICO ---")
# Agora o describe mostrará o outlier de 999.999 mas a linha continua lá
print(df.describe(include='all'))

# 8: LIDAR COM DUPLICADAS
# Em vez de apagar, vamos criar uma coluna que avisa se a linha é repetida
df['is_duplicada'] = df.duplicated(keep=False)


print(df)

