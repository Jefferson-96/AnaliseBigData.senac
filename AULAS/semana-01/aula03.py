LÓGICAS CONDICIONAIS - 01#

x = 100 
y = 99.9
print("x e maior que y?", x > y)
print("x é igual a y?", x == y)

tem_carteira = True 
idade = 18
tem_carro = False
pode_dirigir = idade >= 18 and tem_carteira

print("pode dirigir?",pode_dirigir)

cnh = True
bebidinha = False 

posso_dirigir = cnh and not bebidinha
print(posso_dirigir)

LÓGICAS CONDICIONAIS - 02#

busaun = True
trenzinho = True

venho_pra_aula = busaum or trenzinho
print(venho_pra_aula)
print ("venho_pra_aula",venho_pra_aula)

#LÓGICAS CONDICIONAIS - 03#

locomocao = "moto"
choveu = True

if choveu and locomocao=="moto":
    resultado = "tô todo molhado :("
else: 
    resultado = "tô seco :)"


print(resultado)