data = 0
for i in range(6):
    data = data + i
print(data)


med = (23+19+31)/3

print(med)
print(403//73)
print(403%73)
print(2**10)
print(abs(54 - 57))
print(min(24, 13, 30))

a = 3
b = 4
c = a*a + b*b
print('{}, {}, {}'.format(a,b,c))

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + ' ' + s2 + ' ' + s3)
print((s1 + ' ' )*8)

## exercício 01

preco = float(input('Digite o valor do produto em reais: '))
desconto = float(input('Digite o valor do desconto (0-1000): '))

final = preco - (preco * (desconto/100))

print('O desconto foi de {} sobre o valor {}, que resultou {}.'.format(desconto, preco, final))

## exercicio 02

dias = float(input('Quantos dias foram andados com o carro? '))
quilometros = float(input('Quantos quilometros foram andados com o carro? '))

final = dias*60 + quilometros*0.60

print('O total a pagar será de: {}'.format(final))

## exercicio 03

string = input('Digite uma frase: ')
tam = len(string)

string2  = string[:int(tam/2)]

print(string2[-2:])
