print('Bem-vindo(a) a Calculadora!')
print('Digite * para multiplicação')
print('Digite / para divisão')
print('Digite - para subtração')
print('Digite + para soma')
op = input('Sua operação será: ')

if  op == '+' or op == '-' or op == '/' or op == '*' or op == '-':
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))

    if op == '+':
        resultado = x+y
    if op == '-':
        resultado = x-y
    if op == '*':
        resultado = x*y
    if op == '/':
        resultado = x/y

    print("O resultado da operação é %d" % resultado)
else:
    print('Operação inválida.')