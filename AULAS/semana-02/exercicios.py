#ATIVIDADES PRATICAS

#1 - Cálculo de Lâmpadas:

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




#2 - Quantidade de Caixas de Azulejos:

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





#3. Rendimento do Taxista:











#4 - Código de Origem do Produto:

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



