# impar_1 = 3
# impar_2 = 5
# impar_3 = 13
# impar_4 = 27

# impares = []
# print(type(impares))
# impares = [3,5,13,27]
# print(impares[-3])

# lista_01 = [
#     12,
#     "pedro",
#     12.53343,
#     "[{_{^^{}}}",
#     False,
#     0,
#     [2,4,6,8]]

# # print(lista_01[1],lista_01[2],lista_01[4],lista_01[6][2])

# #CONDICIONAIS:

# lista_02 = ["Márcia"]

# # if "Márcia" in lista_02:
# #     print(lista_02)
# # else:
# #     print("Márcia não está presente na lista.")

# #LOOPINGS:

# participantes = ["Isaque","Luana","Fernado","Bianca","Ana Paula"]

# # for participante in participantes:
# #     print(participante)

# # partic_2 = "Hugo"
# # participantes.append(partic_2)

# partic_2 = "Hugo"
# participantes.append(partic_2) #posição fixa
# participantes.insert(2,partic_2) #consigo colocar onde eu quiser
# participantes.pop(1) #remoção com critério
# participantes.remove("Hugo") #remoção expecífica
# participantes.reverse()
# participantes.count("Hugo")
# # participantes.index("Bianca")
# # participantes.clear()

# print(participantes)

#ESPECIFICAÇÕES IMPORTANTES
# [] List  *significa uma lista*
# () tuple *significa protegido*
# {} set *caracteristica de não ter ordem ou trabalhar em dados que não tenha ordem e remove os itens duplicados*
# {k:v} {key : value}


#TUPLAS
# participantes = ("Isaque","Luana","Fernado","Bianca","Ana Paula") + ("Hugo")
# print(resultado)

# print(participantes,type(participantes))


#SETS:

# numeros_pares = {
# 202,
# 203,
# 204,
# 204,
# 205,
# 219,
# 291,
# 292,
# 202
# }

# # print(numeros_pares,type(numeros_pares))

# numeros_impares = {111,111,112,291,205}
# print(numeros_pares.intersection(numeros_impares))
# numeros_impares.remove(205)
# print(numeros_pares)

#

#DICIONÁRIOS:

produtos = {"maçã":5.99,"laranja":4.79}
# print(produtos,(type(produtos)))

print(produtos.items()) # me trás os produtos e os valores juntos
print(produtos.keys()) #me trás somente os produtos
print(produtos.values()) #me trás somente os valores
print(produtos.get("laranja")) #especifico o produto e ele me tras somente o valor do produto *caso eu tenha esquecido o valor*
produtos2 = produtos.copy() #faço uma cópia dos dados originais *a partir deste comando daqui* 
print(produtos2)
# produtos2.pop("maçã")
# produtos.update()
produtos["maçã"]=7.99
print(produtos2)

###
achadinhos = {} 
print(type(achadinhos))
achadinhos["capinha celular"]=12.99
print(achadinhos)