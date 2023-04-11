def dimensoesObjeto():
    while True:
        try:
            altura = int(input("Qual a altura em cm do objeto? "))
            comprimento = int(input("Qual o comprimento em cm do objeto? "))
            largura = int(input("Qual a largura em cm do objeto? "))
            volume = altura * comprimento * largura

            if volume < 1000:
                valor = 10
                break
            elif volume <= 1000 and volume < 10000:
                valor = 20
                break
            elif volume <= 10000 and volume < 30000:
                valor = 30
                break
            elif volume <= 30000 and volume < 10000:
                valor = 50
                break
            elif volume >= 10000:
                print("Os valores inseridos ultrapassaram nosso máximo de volume, tente novamente...")
                continue
        except:
            print("Algum valor digitado está incorreto.")
            continue
    return valor

def pesoObjeto():
    while True:
        try:
            peso = int(input("Qual o peso do produto em kg?"))

            if peso <= 0.1:
                valor = 1
                break
            elif peso >= 0.1 and peso < 1:
                valor = 1.5
                break
            elif peso >= 1 and peso < 10:
                valor = 2
                break
            elif peso >= 10 and peso < 30:
                valor = 3
                break
            elif peso >= 30:
                print("Valor não aceito, tente novamente...")
                continue
        except:
            print("O Valor inserido foi digitado incorreto.")
            continue
    return valor

def rotaObjeto():
    while True:
        try:
            print("Digite uma rota:")
            print("RS - Rio de Janeiro para São Paulo")
            print("SP - São Paulo para Paraná")
            print("PR - Paraná para Rondônia")
            destino = input("")

            if destino == "PR" or "pr":
                multiplicador = 1
                break
            elif destino == "SP" or "sp":
                multiplicador = 1.2
                break
            elif destino == "RS" or "rs":
                multiplicador = 1.5
                break
            else:
                print("Essa cidade não esta em nosso sistema, tente novamente...")
                continue
        except:
            print("O valor inserido não é uma cidade.")
            continue
    return multiplicador

print("Bem vindo a transportadora Mateus Delai Takayama")
peso = pesoObjeto()
dimensoes = dimensoesObjeto()
rota = rotaObjeto()

valorTotal = peso * dimensoes * rota
print("O valor total foi de R$ {}".format(valorTotal))