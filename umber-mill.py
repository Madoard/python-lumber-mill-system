# Exibe a mensagem de boas-vindas e o menu de madeiras
print("Bem-vindo à Madeireira de Maria Eduarda Gonçalves!")
print("Por favor, informe o tipo de madeira desejado:")
print("PIN - Tora de Pinho")
print("PER - Tora de Peroba")
print("MOG - Tora de Mogno")
print("IPE - Tora de Ipê")
print("IMB - Tora de Imbuia")


# Função para escolher o tipo de madeira e retornar o preço unitário
def escolher_tipo_madeira():
    while True:
        tipo_madeira = input("\nInforme o tipo de madeira desejado: ").strip().upper()
        if tipo_madeira == "PIN":
            return 150.40
        elif tipo_madeira == "PER":
            return 170.20
        elif tipo_madeira == "MOG":
            return 190.90
        elif tipo_madeira == "IPE":
            return 210.10
        elif tipo_madeira == "IMB":
            return 220.70
        else:
            print("Escolha inválida, informe o tipo de madeira novamente.")
            print("PIN - Tora de Pinho")
            print("PER - Tora de Peroba")
            print("MOG - Tora de Mogno")
            print("IPE - Tora de Ipê")
            print("IMB - Tora de Imbuia")


# Função para obter a quantidade de toras e retornar a quantidade + desconto por volume
def quantidade_toras():
    while True:
        try:
            qtd = int(input("\nInforme a quantidade de toras: "))
            if qtd <= 0 or qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. Tente novamente.")
                continue
            elif qtd < 100:
                return qtd, 0.0
            elif 100 <= qtd < 500:
                return qtd, 0.04
            elif 500 <= qtd < 1000:
                return qtd, 0.09
            elif 1000 <= qtd <= 2000:
                return qtd, 0.16
        except ValueError:
            print("Pedido inválido. Informe um número inteiro para a quantidade de toras.")


# Função para escolher a opção de frete e retornar o seu custo
def opcao_frete():
    while True:
        try:
            opcao = int(input(
                "\nEscolha a opção de frete:\n"
                " 1 - Transporte Rodoviário - $ 1000.00\n"
                " 2 - Transporte Ferroviário - $ 2000.00\n"
                " 3 - Transporte Hidroviário - $ 2500.00\n"
                "Opção: "
            ))
            if opcao == 1:
                return 1000
            elif opcao == 2:
                return 2000
            elif opcao == 3:
                return 2500
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")


# Executa as funções e calcula o total final do pedido
preco_unitario = escolher_tipo_madeira()
quantidade, desconto = quantidade_toras()
custo_frete = opcao_frete()

total = ((preco_unitario * quantidade) * (1 - desconto)) + custo_frete

# Exibe o total final do pedido
print(f"\nTotal: $ {total:.2f}")
