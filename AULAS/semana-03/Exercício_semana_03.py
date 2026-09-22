#1. Cálculo de Média Escolar para Vários Alunos

# for aluno in range(10):
#     print("aluno:", aluno + 1)

#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     optativa = float(input("Digite a nota da avaliação optativa (-1 caso não tenha feito): "))

#     if optativa != -1:

#         if nota1 < nota2:
#             nota1 = optativa
#         else:
#             nota2 = optativa

#     media = (nota1 + nota2) / 2

#     print(f"\nMédia do semestre: {media:.2f}")


#     if media >= 6.0:
#         print("Aprovado")
#     elif media >= 3.0:
#         print("Recuperação")
#     else:
#         print("Reprovado")




# 2. Cadastro de Candidatos


# for candidato in range(12):

#     print("Candidato:", candidato + 1)

#     ano_nascimento = int(input("Digite o ano de nascimento: "))

#     ano_atual = 2026
#     idade = ano_atual - ano_nascimento

#     if idade >= 18:

#         nome_completo = input("Digite seu nome completo: ")
#         endereco = input("Digite seu endereço: ")
#         telefone = input("Digite um número de telefone para contato: ")
#         email = input("Digite um E-mail para contato: ")

#         print("Cadastro concluído")

#     else:
#         print("Inapto (idade mínima de 18 anos)")





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


# FILA DE PEDIDOS DA COZINHA

fila_cozinha = [
    {
        "pedido": "0001",
        "mesa": 1,
        "cliente": "João",
        "itens": ["Sushi", "hot", "Refrigerante (refil)"],
        "prioridade": 2,
        "status": "Pendente"
    },

    {
        "pedido": "0002",
        "mesa": 3,
        "cliente": "Maria",
        "itens": ["sashimi", "Suco (copo 500ml)"],
        "prioridade": 1,
        "status": "Pendente"
    },

    {
        "pedido": "0003",
        "mesa": 5,
        "cliente": "Carlos",
        "itens": ["X-Bacon", "Batata frita"],
        "prioridade": 3,
        "status": "Pendente"
    },

    {
        "pedido": "0004",
        "mesa": 2,
        "cliente": "Ana",
        "itens": ["Hambúrguer", "Suco"],
        "prioridade": 1,
        "status": "Pendente"
    }
]


def listar_fila_cozinha(fila):

    print("\n===== FILA DA COZINHA =====")
    print("1 - Ordem de entrada")
    print("2 - Ordem de prioridade")

    opcao = input("Escolha a forma de exibição: ")

    # Mostra somente os pedidos pendentes
    pedidos_pendentes = []

    for pedido in fila:
        if pedido["status"] == "Pendente":
            pedidos_pendentes.append(pedido)

    # Organiza por prioridade
    if opcao == "2":
        pedidos_pendentes.sort(key=lambda pedido: pedido["prioridade"])

    print("\n===== PEDIDOS PENDENTES =====")

    for pedido in pedidos_pendentes:

        print("\nPedido:", pedido["pedido"])
        print("Mesa:", pedido["mesa"])
        print("Cliente:", pedido["cliente"])
        print("Prioridade:", pedido["prioridade"])
        print("Itens:")

        for item in pedido["itens"]:
            print("-", item)

    return pedidos_pendentes

listar_fila_cozinha(fila_cozinha)


