A = int(input('Insira o valor do lado A:  '))
B = int(input('Insira o valor do lado B:  '))
C = int(input('Insira o valor do lado C:  '))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and C + B > A:
        if A == B and B == C:
            print('O triângulo é Equilátero!')
        elif A != B and B != C and A != C:
            print('O triângulo é Escaleno!')
        else:
            print('O triângulo é Isósceles!')
    else:
        print('A soma de dois lados não podem ser menores que um dos lados.')
else:
    print('Encerrando programa...')
