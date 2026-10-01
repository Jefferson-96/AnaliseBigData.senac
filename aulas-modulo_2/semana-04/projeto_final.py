import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import mysql.connector
import seaborn as sns
import os


conexao = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="meu_ecommerce"
    )

aeronave_df = pd.read_csv("aeronave.csv")
fator_df = pd.read_csv("fator_contribuinte.csv")
ocorrencia_df = pd.read_csv("ocorrencia.csv")
tipo_df = pd.read_csv("ocorrencia_tipo.csv")
recomendacao_df = pd.read_csv("recomendacao.csv")