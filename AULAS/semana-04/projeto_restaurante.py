def consultar_status_pedido(fila):

    numero_pedido = input("Digite o número do seu pedido: ")

    for pedido in fila:

        if pedido["pedido"] == numero_pedido:

            print("\n==============================")
            print("       STATUS DO PEDIDO")
            print("==============================")

            print("Pedido:", pedido["pedido"])
            print("Cliente:", pedido["cliente"])
            print("Mesa:", pedido["mesa"])
            print("Status:", pedido["status"])

            if pedido["status"] == "Enviado":
                print("Seu pedido foi enviado para a cozinha.")

            elif pedido["status"] == "Preparando":
                print("Seu pedido está sendo preparado.")

            elif pedido["status"] == "Pronto":
                print("Seu pedido está pronto!")

            print("==============================")

            return

    print("\nPedido não encontrado.")


# Lista de pedidos
fila = [
    {
        "pedido": "123",
        "cliente": "João",
        "mesa": 5,
        "status": "Preparando"
    },
    {
        "pedido": "456",
        "cliente": "Maria",
        "mesa": 2,
        "status": "Pronto"
    }
]

# Chamada da função
consultar_status_pedido(fila)