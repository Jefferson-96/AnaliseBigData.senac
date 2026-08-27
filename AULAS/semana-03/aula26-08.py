# Usuario = "Jefferson"
# Senha = "senac"

# contador = 0
# limite = 3

# while contador < limite:

#     login = input("Digite seu login: ")
#     Senha_Digitada = input("Digite sua senha: ")

#     if login == Usuario and Senha_Digitada == Senha:
#         print("Acesso liberado!")
#         break

#     else:
#         contador += 1
#         print("Login ou senha incorretos.")
#         print(f"Tentativas restantes: {limite - contador}")

# if contador == limite:
#     print("Senha bloqueada! Número máximo de tentativas atingido.")



    # def calculadora_v1(num1,num2,operador="1"):

def Calculadora_v1(num1,num2operador="3"):

    # num1=float(input("Digite seu primeiro número:"))
    # num2=float(input("Digite seu segundo número:"))

    # operador=input("informe a operação desejada entre: 1. adição; 2. subtração; 3. multiplicação; 4. divisão.")

    match operador:
        case "1":
                print(f"Resultado da soma: {num1+num2}.")
        case "2":
                print(f"Resultado da subtração: {num1-num2}.")
        case "3":
                print(f"Resultado da multiplicação: {num1*num2}.")
        case "4":
                if num2!=0:
                        print(f"Resultado da divisão: {num1/num2}.")
        case _:
                print(f"Dividiu por Zero. Errou feio. Errou.")

cauculinho = Calculadora_v1(333,555)

    # calculadora_v1 (333,111,"1")
