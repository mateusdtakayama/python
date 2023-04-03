valor = int(input("Digite o valor a ser convertido: "))
um = 0
cinco = 0
dez = 0
vinte = 0
cinquenta = 0
cem = 0

while(valor != 0):
    if valor >= 100:
        cem += 1
        valor = valor - 100
    elif valor >= 50:
        cinquenta += 1
        valor = valor - 50
    elif valor >= 20:
        vinte += 1
        valor = valor - 20
    elif valor >= 10:
        dez += 1
        valor = valor - 10
    elif valor >= 5:
        cinco += 1
        valor = valor - 5
    else:
        um += 1
        valor = valor -1
print('{} notas de cem.'.format(cem))
print('{} notas de cinquenta.'.format(cinquenta))
print('{} notas de vinte.'.format(vinte))
print('{} notas de dez.'.format(dez))
print('{} notas de cinco.'.format(cinco))
print('{} notas de um.'.format(um))
