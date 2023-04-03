print("Bem-vindo(a) a calculadora de energia!")
faixa = input("Digite I para Industrial, R para Residencial ou C para Comercial.")

if faixa == 'i' or faixa == 'I' or faixa == 'r' or faixa == 'R' or faixa == 'C' or faixa == 'c':
    consumo = int(input("Digite quanto foi consumido no mês em kWh: "))

    if faixa == 'i' or faixa == 'I':
        if consumo <= 5000:
            preco = consumo * 0.55
        else:
            preco = consumo * 0.60

    elif faixa == 'r' or faixa == 'R':
        if consumo <= 500:
            preco = consumo * 0.40
        else:
            preco = consumo * 0.65

    else:
        if consumo <= 1000:
            preco = consumo * 0.55
        else:
            preco = consumo * 0.60

    print("Preço final será de {}".format(preco))
else:
    print("Entrada inválida.")