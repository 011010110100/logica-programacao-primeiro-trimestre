# Estrutura de dados -> estruturas que mantém em memórias os dados
  
""" 
Listas ---| estrutura de dados linear |--> []
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c", 5, 6]

podemos acessar através dos índices
lista1[0] = 1

lista = ["o", "Menino", "jogou", "a", "Bola"]

for item in lista:
    print(item) 

print("Quantidade de elementos: ", len(lista))
indice = 0
while indice<len(lista):
    print(lista[indice])
    indice += 1

# Concatenando listas

lista = lista + ["1"] # |--> ['o', 'Menino', 'jogou', 'a', 'Bola', "1"]

lista3 = [1, 5, 10, 20, 30, 50]
valor = int(input("Informe um valor: "))

if valor in lista3: print(valor, " percence a ", lista3)
else: print("Ele não pertence a lista!")

lista3.append(90) # [1, 5, 10, 20, 30, 50, 90] insere no final

Se quisermos inserir em uma posição específica usamos o -> insert!

lista3.pop(90) # Para excluir um elemento da lista!

"""

""" 
Exemplo) Crie uma lista com 30 valores inteiros. Gere a lista com valores
aleatórios entre 1 e 500. A seguir implemente um programa que varre a lista
e calcule
a) o maior valor
b) o menor valor
 """
import random

lista = []
for i in range(0,30):
    lista.append(random.randint(1,500))

print(lista)

maior = lista[0]
pares = 0

for num in lista:
    if num > maior: maior = num
    if num%2==0 : pares += 1

impares = len(lista) - pares

print("Maior: ", maior)
print("Quantidade de pares: ", pares)
print("Quantidade de ímpares: ", impares)