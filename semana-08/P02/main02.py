""" 
Como podemos contar as ocorrências de uma letra em uma lista?

ex.: lista = [a, a, a, a, b, b, b, b, c, c, c]
lista.coiunt('a')
lista.coiunt('b')


Como podemos saber a soma de uma lista?
sum()

Como sabemos o menor e o maior valor?
min()
max()

Como ordenar uma lista?
sort()    -> crescente
reverse() -> decrescente
"""

""" import random

lista = []

for i in range(1,15):
    lista.append(random.randint(1,100)/10)

print("Notas: ", lista)

media = sum(lista)/len(lista)
print("Media", media)

acima = 0
abaixo = 0

for nota in lista:
    if nota > media: acima += 1
    if nota < media: abaixo += 1

print("Quantidade de notas acima da media: ", acima)
print("Quantidade de notas abaixo da media: ", abaixo)
print("Quantidade de notas iguais a media: ", lista.count(media))
print("Maior nota: ", max(lista))
print("Menor nota: ", min(lista))
 """

""" 
Construa um programa que gera uma lista com as avaliações de 25 pessoas.
Cada pessoa avaliou a gestão do prefeito de uma cidade com notas de 5 a 1
onde 5 --> corresponde a Excelente
     4 -->               Bom
     3 -->               Regular
     2 -->               Ruim
     1 -->               Péssimo

"""
import random
lista = []

for i in range(1,300):
    lista.append(random.randint(1,6))

print("Notas: ", lista)

conceito = []
quantidade = []

conceito.append('Excelente')
quantidade.append(lista.count(5))

conceito.append('Bom')
quantidade.append(lista.count(4))

conceito.append('Regular')
quantidade.append(lista.count(3))

conceito.append('Ruim')
quantidade.append(lista.count(2))

conceito.append('Péssimo')
quantidade.append(lista.count(1))

maiorQuantidade = quantidade[0]
maiorConceito = conceito[0]

for i in range(0,5):
    print(conceito[i], " - ", quantidade[i])
    if (quantidade[i] > maiorQuantidade):
        maiorQuantidade = quantidade[i]
        maiorConceito = conceito[i]

print("Conceito mais votado: ", maiorConceito)
print("Recebeu ", maiorQuantidade, " votos")