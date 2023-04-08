## Exercício 01

print("Bem vindo a loja de Mateus Delai Takayama") ## Apresentacao


## abs para nao poder inserir valores negativos e int para passar de string para int
print("-" * 35)
valor = abs(int(input("Entre com o valor do produto: ")))
print("-" * 35)
quantidade = abs(int(input("Entre com a quantidade: ")))
preco = valor * quantidade

## descontos
if quantidade <= 9:
    desconto = 0
    aux = "0%"
elif quantidade > 9 and quantidade <= 99:
    desconto = valor * quantidade * 5/100
    aux = "5%"
elif quantidade >= 100 and quantidade <= 999:
   desconto = valor * quantidade * 10/100
   aux = "10%"
elif quantidade >= 1000:
    desconto = valor * quantidade * 15/100
    aux = "15%"

precoFinal = preco - desconto

print("-" * 65)
print("O preço a pagar sem desconto é: R$ {}".format(preco))
print("O preço a pagar com desconto é de: R$ {} ({} de desconto)".format(precoFinal, aux))
print("-" * 65)