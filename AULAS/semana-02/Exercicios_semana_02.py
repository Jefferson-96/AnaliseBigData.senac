# #ATIVIDADES PRATICAS

# #1 - Cálculo de Lâmpadas:

# potencia = float(input("Digite a potência da lâmpada (W): "))
# largura = float(input("Digite a largura do cômodo (m): "))
# comprimento = float(input("Digite o comprimento do cômodo (m): "))

# area = largura * comprimento
# potencia_necessaria = area * 3
# lampadas = potencia_necessaria / potencia

# match lampadas % 1:
#     case 0:
#         lampadas = int(lampadas)
#     case _:
#         lampadas = int(lampadas) + 1

# print("Número de lâmpadas necessárias:", lampadas)




# #2 - Quantidade de Caixas de Azulejos:

# comprimento = float(input("Digite o comprimento: "))
# largura = float(input("Digite a largura: "))
# altura = float(input("Digite a altura: "))

# area = 2 * (comprimento + largura) * altura
# caixas = area / 1.5

# if caixas % 1 != 0:
#     caixas = int(caixas) + 1
# else:
#     caixas = int(caixas)

# print("Quantidade de caixas:", caixas) 




# #3. Rendimento do Taxista:

# preco_combustivel = 6.15

# odometro_inicial = float(input("Informe a quilometragem inicial: "))
# odometro_final = float(input("Informe a quilometragem final: "))
# litros_gastos = float(input("Informe os litros gastos: "))
# valor_recebido = float(input("Informe o valor recebido dos passageiros: R$ "))

# km_percorridos = odometro_final - odometro_inicial
# consumo_medio = km_percorridos / litros_gastos
# gasto_combustivel = litros_gastos * preco_combustivel
# lucro_liquido = valor_recebido - gasto_combustivel

# print(f"\nQuilômetros percorridos: {km_percorridos:.2f} km")
# print(f"Consumo médio: {consumo_medio:.2f} km/L")
# print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")
# print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")





# #4 - Código de Origem do Produto:

# codigo = int(input("Código de Origem do Produto:"))
# match codigo:
#     case 1:
#         codigo="Sul"
#     case 2:
#         codigo="Norte"
#     case 3:
#         codigo="Leste"
#     case 4:
#         codigo="Oeste"
#     case 5 | 6:
#         codigo="Nordeste"
#     case 7 | 8 | 9:
#         codigo="Sudeste"
#     case 10:
#         codigo="Centro-Oeste"
#     case 11:
#         codigo="Noroeste" 
#     case _:
#         codigo="Importado"            

# print(f"região:{codigo}.")




# #5. Média do Aluno com Optativa:

# nota1 = float(input("Digite a nota da primeira avaliação: "))
# nota2 = float(input("Digite a nota da segunda avaliação: "))
# optativa = float(input("Digite a nota da avaliação optativa (-1 caso não tenha feito): "))

# if optativa != -1:

#     if nota1 < nota2:
#         nota1 = optativa
#     else:
#         nota2 = optativa

# media = (nota1 + nota2) / 2

# print(f"\nMédia do semestre: {media:.2f}")


# if media >= 6.0:
#     print("Aprovado")
# elif media >= 3.0:
#     print("Recuperação")
# else:
#     print("Reprovado")



# #6. Positivo ou Negativo:


# valor = float(input("Digite um valor: "))

# if valor >= 0:
#     print("O valor é positivo.")
# else:
#     print("O valor é negativo.")







