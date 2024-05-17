""" 
Faça um programa que leia três valores e escreva
em forma crescente!
"""

v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
v3 = int(input('Informe o terceiro valor: '))

# Descobrindo primeiro o maior

maior = v1
if v2>maior : maior = v2
if v3>maior : maior = v3

menor = v1
if v2 < menor : menor = v2
if v3 < menor : menor = v3

meio = v1+v2+v3 - maior - menor
print("A ordem será: ", menor, "->", meio, "->", maior)
print("Decrescente: ", maior, "->", meio, "->", menor)


""" 
Agora, queremos estender a lógica para 4 valores
"""

v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
v3 = int(input('Informe o terceiro valor: '))
v4 = int(input('Informe o quarto valor: '))

if v2<v1:
    aux = v1
    v1 = v2
    v2 = aux

if v3<v1:
    aux = v1
    v1 = v3
    v3 = aux

if v4<v1:
    aux = v1
    v1 = v4
    v4 = aux
# logo v1 já está pronto, e com ctz tem o menor valor

if v3<v2:
    aux = v3
    v2 = v3
    v3 = aux

if v4<v2:
    aux = v4
    v2 = v4
    v4 = aux

if v4<v3:
    aux = v3
    v3 = v4
    v4 = aux

print("Crescente: ", v1, v2, v3, v4)
print("Decrescente: ", v4, v3, v2, v1)  


"""
Calcule o preco do produto!
Implemente um programa que determina o preço das vendas dos produtos
de uma loja conforme o preço de custo desses produtos.
O programa deve ler o preço de custo e calcular o valor de venda
conforme a tabela:

preço unitário de custo           preço de venda
valor abaixo de R$ 10,00           lucro de 70%
de R$ 10,00 a menos de R$ 30,00    lucro de 50%
de R$ 30,00 a menos de R$ 50,00    lucro de 40%
valor acima ou igual a R$ 50,00    lucro de 30%
"""

preco = float(input("Informe o preço de custo: "))

if preco <= 0:
    print("Valor inválido")
else:
    # aqui vamos calcular o preço de venda
    if preco<10: venda = preco*(1.7)
    if preco>=10 and preco<30: venda = preco*(1.5)
    if preco>=30 and preco<50: venda = preco*(1.4)
    if preco>=50: venda = preco*(1.3)

print("Preco de venda: ", venda)
