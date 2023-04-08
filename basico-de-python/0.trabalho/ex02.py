# Serve para inicialmente pedir se o cliente gostaria de pedir algo
def pedirAlgo():
    print("Gostaria de pedir alguma coisa?")
    print("1 - Sim")
    print("0 - Não")

# Função do cardápio
def cardapio():
    print("-" * 18 + "Cardápio" + "-" * 18)
    print("| Código  |          Descrição     | Valor |")
    print("|   100   |   Cachorro quente      |  9,00 |")
    print("|   101   | Cachorro Quente Duplo  | 11,00 |")
    print("|   102   |         X-Egg          | 12,00 |")
    print("|   103   |        X-Salada        | 12,00 |")
    print("|   104   |        X-Bacon         | 14,00 |")
    print("|   105   |         X-Tudo         | 17,00 |")
    print("|   200   |     Refrigerante Lata  |  5,00 |")
    print("|   201   |       Chá Gelado       |  4,00 |")
    print("-" * 44)

# Pedir novamente
def pedirNovamente():
    print("Deseja pedir mais alguma coisa?")
    print("1 - Sim")
    print("0 - Não")
    option = int(input(""))

    return option
# Opcao do cardápio
def opcaoCardapio():
    total = 0
    booleanContinue = 1

    while(booleanContinue == 1):
        try:
            option = int(input("Escolha um produto com base em seu código: "))
            if option == 100:
                print("Você pediu Cachorro quente no valor de R$ 9,00")
                total += 9
            elif option == 101:
                print("Você pediu Cachorro Quente Duplo no valor de R$ 11,00")
                total += 11
            elif option == 102:
                print("Você pediu X-Egg no valor de R$ 12,00")
                total += 12
            elif option == 103:
                print("Você pediu X-Salada no valor de R$ 12,00")
                total += 12
            elif option == 104:
                print("Você pediu X-Bacon no valor de R$ 14,00")
                total += 14
            elif option == 105:
                print("Você pediu X-Tudo no valor de R$ 17,00")
                total += 17
            elif option == 200:
                print("Você pediu Refrigerante Lata no valor de R$ 5,00")
                total += 5
            elif option == 201:
                print("Você pediu Chá Gelado no valor de R$ 4,00")
                total += 4
            else:
                print("Código inválido.")
                continue  # Pula para a próxima iteração
        except ValueError:
            print("Operação inválida.")
            continue  # Pula para a próxima iteração

        booleanContinue = pedirNovamente()

        if booleanContinue == 0:
            break  # Interrompe o laço de repetição

    return total

# Estrutura
print("Bem vindo a lanchonete de Mateus Delai Takayama.")
pedirAlgo()

# Se for igual a 1 ele mostra o cardapio, igual a 0 encerra o programa com ate mais e se for algum valor diferente ele da operacao invalida
try:
    initialOperation = int(input(""))
    if initialOperation == 1:
        cardapio()
        total = opcaoCardapio()
    elif initialOperation == 0:
        print("Até mais!")
except ValueError:
    print("Operação inválida, encerrando programa...")

print("O valor do pedido foi de {}".format(total))