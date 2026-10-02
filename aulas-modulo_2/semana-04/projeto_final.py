
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ============================================================
# 1. CONECTAR AO BANCO DE DADOS
# ============================================================

conexao = None
cursor = None

try:
    conexao = mysql.connector.connect(
        host="trocar",
        user="root",
        password="trocar",
        database="meu_ecommerce"
    )

    cursor = conexao.cursor()

    print("Conexao com o MySQL realizada com sucesso!")

    # ========================================================
    # 2. DEFINIR AS PERGUNTAS E AS CONSULTAS SQL
    # ========================================================

    consultas = [

        {
            "pergunta": "1. Ocorrencias por classificacao",
            "query": """
                SELECT
                    ocorrencia_classificacao,
                    COUNT(*) AS total
                FROM ocorrencia
                WHERE ocorrencia_classificacao IS NOT NULL
                GROUP BY ocorrencia_classificacao
                ORDER BY total DESC
            """,
            "coluna": "ocorrencia_classificacao",
            "titulo": "Quantidade de Ocorrencias por Classificacao",
            "eixo_x": "Classificacao",
            "eixo_y": "Quantidade de ocorrencias"
        },

        {
            "pergunta": "2. Ocorrencias por estado",
            "query": """
                SELECT
                    ocorrencia_uf,
                    COUNT(*) AS total
                FROM ocorrencia
                WHERE ocorrencia_uf IS NOT NULL
                  AND ocorrencia_uf <> ''
                GROUP BY ocorrencia_uf
                ORDER BY total DESC
            """,
            "coluna": "ocorrencia_uf",
            "titulo": "Quantidade de Ocorrencias por Estado",
            "eixo_x": "Estado",
            "eixo_y": "Quantidade de ocorrencias"
        },

        {
            "pergunta": "3. Tipos de ocorrencia mais registrados",
            "query": """
                SELECT
                    ocorrencia_tipo,
                    COUNT(*) AS total
                FROM ocorrencia_tipo
                WHERE ocorrencia_tipo IS NOT NULL
                  AND ocorrencia_tipo <> ''
                GROUP BY ocorrencia_tipo
                ORDER BY total DESC
            """,
            "coluna": "ocorrencia_tipo",
            "titulo": "Frequencia dos Tipos de Ocorrencia",
            "eixo_x": "Tipo de ocorrencia",
            "eixo_y": "Quantidade de registros"
        },

        {
            "pergunta": "4. Fatores contribuintes mais frequentes",
            "query": """
                SELECT
                    fator_nome,
                    COUNT(*) AS total
                FROM fator_contribuinte
                WHERE fator_nome IS NOT NULL
                  AND fator_nome <> ''
                GROUP BY fator_nome
                ORDER BY total DESC
            """,
            "coluna": "fator_nome",
            "titulo": "Frequencia dos Fatores Contribuintes",
            "eixo_x": "Fator contribuinte",
            "eixo_y": "Quantidade de registros"
        },

        {
            "pergunta": "5. Fabricantes de aeronaves mais frequentes",
            "query": """
                SELECT
                    aeronave_fabricante,
                    COUNT(*) AS total
                FROM aeronave
                WHERE aeronave_fabricante IS NOT NULL
                  AND aeronave_fabricante <> ''
                GROUP BY aeronave_fabricante
                ORDER BY total DESC
            """,
            "coluna": "aeronave_fabricante",
            "titulo": "Quantidade de Registros por Fabricante",
            "eixo_x": "Fabricante",
            "eixo_y": "Quantidade de aeronaves"
        },

        {
            "pergunta": "6. Recomendacoes por situacao",
            "query": """
                SELECT
                    recomendacao_status,
                    COUNT(*) AS total
                FROM recomendacao
                WHERE recomendacao_status IS NOT NULL
                  AND recomendacao_status <> ''
                GROUP BY recomendacao_status
                ORDER BY total DESC
            """,
            "coluna": "recomendacao_status",
            "titulo": "Quantidade de Recomendacoes por Situacao",
            "eixo_x": "Situacao da recomendacao",
            "eixo_y": "Quantidade de recomendacoes"
        }

    ]

    # ========================================================
    # 3. EXECUTAR AS CONSULTAS
    # ========================================================

    for analise in consultas:

        print("\n" + "=" * 80)
        print(analise["pergunta"].upper())
        print("=" * 80)

        # Executar a consulta SQL
        cursor.execute(analise["query"])

        # Obter os resultados
        resultados = cursor.fetchall()

        # Obter os nomes das colunas
        colunas = [
            coluna[0] for coluna in cursor.description
        ]

        # Criar um DataFrame com os resultados
        df = pd.DataFrame(
            resultados,
            columns=colunas
        )

        # Exibir os resultados no terminal
        if not df.empty:

            print(df.to_string(index=False))

            # ================================================
            # 4. GERAR O GRAFICO DE COLUNAS
            # ================================================

            plt.figure(figsize=(14, 6))

            sns.barplot(
                data=df,
                x=analise["coluna"],
                y="total"
            )

            plt.title(
                analise["titulo"],
                fontsize=14
            )

            plt.xlabel(
                analise["eixo_x"],
                fontsize=11
            )

            plt.ylabel(
                analise["eixo_y"],
                fontsize=11
            )

            # Girar os nomes para facilitar a leitura
            plt.xticks(
                rotation=90,
                fontsize=8
            )

            plt.grid(
                axis="y",
                linestyle="--",
                alpha=0.5
            )

            plt.tight_layout()
            plt.show()

        else:
            print("Nenhum resultado encontrado.")

except mysql.connector.Error as erro:

    print(f"Erro ao conectar ou consultar o MySQL: {erro}")

finally:

    # ========================================================
    # 5. FECHAR A CONEXAO
    # ========================================================

    if cursor is not None:
        cursor.close()

    if conexao is not None and conexao.is_connected():
        conexao.close()

    print("\nConexao com o MySQL encerrada.")