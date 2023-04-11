list_products = []
cod_product = 0

def create_product(codigo):
    print("Bem vindo a Cadastrar Produto: ")
    nome = input("Insira o NOME do produto: ")
    fabricante = input("Insira o FABRICANTE do produto: ")
    preco = input("Insira o PREÇO em reais do produto: ")
    dicionario_produto = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'preco': preco,
    }
    list_products.append(dicionario_produto.copy())

def read_product():
    print("Bem vindo a Ler Produto: ")
    while True:
        option = input("\n1- Consultar todos os produtos \n" +
                        "2- Consultar produto por código \n" +
                        "3- Consultar produto por FABRICANTE \n" +
                        "4- Retornar \n"
                        ">> ")

        if option == '1':
            print("Você escolheu a opção consultar TODOS os produtos.")
            for product in list_products:
                for key, value in product.items():
                    print("{}: {}".format(key, value))
        elif option == '2':
            print("Você escolheu a opção consultar por código.")
            cod = int(input("Insira o código desejado: "))
            for product in list_products:
                if product['codigo'] == cod:
                    for key, value in product.items():
                            print("{}: {}".format(key, value))
        elif option == '3':
            print("Você escolheu a opção consultar produto por FABRICANTE.")
            cod = input("Insira o código desejado: ")
            for product in list_products:
                if product['fabricante'] == cod:
                    for key, value in product.items():
                            print("{}: {}".format(key, value))
        elif option == '4':
            break
        else:
            print("Opção inválida, tente novamente...")
            continue

def remove_product():
    print("Bem vindo a Cadastrar Produto: ")
    cod = int(input("Insira o código desejado: "))
    for product in list_products:
        if product['codigo'] == cod:
            list_products.remove(product)
            print("Produto Removido!")
print("Bem vindo a Merceria de Mateus Delai Takayama.")

while True:
    option = input("\n1- Criar produto \n" +
                    "2- Ler produto (s) \n" +
                    "3- Remover produto \n" +
                    "4- Sair \n"
                    ">> ")

    if option == '1':
        cod_product += 1
        create_product(cod_product)
    elif option == '2':
        read_product()
    elif option == '3':
        remove_product()
    elif option == '4':
        break
    else:
        print("Opção inválida, tente novamente...")
        continue
