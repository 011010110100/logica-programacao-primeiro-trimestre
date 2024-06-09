# Listas aninhadas

#--------------------FUNCOES COMPARTILHADAS-------------------------------------

def print_matriz(matriz, original=True):
    if original: print("Matriz Original!")
    for linha in matriz:
        print(linha)


#-------------------------------------------------------------------------------


""" 
List comprehension - abrangência de listas é uma maneira compacta
de se criar listas.

[<expressao> for <item> in <sequencia> if <condicao>]

"""
""" 
lista = [1, 2, 3, 4, 5]

quadrados = [item**2 for item in lista]
print("---> Quadrado: ", quadrados)

cubos = [item**3 for item in lista]
print("---> Cubo: ", cubos)

 """
""" 
Listas aninhadas
ex.: matriz [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9]] 

para acessarmos
--> matriz[0] ==> [1, 2, 3]
--> matriz[0][0] ==> [1]

"""

# Ex.: Calcule a soma de todos os elementos da matriz

""" matriz = [[1,2,4],[2,3,5],[3,4,5]]
print("A MATRIZ: ", matriz)

soma = 0
for linha in matriz:
    for elemento in linha:
        soma = soma + elemento
    
print("A soma dos elementos da matriz: ", soma)
 """

# Somando apenas uma linha

""" soma = 0
for elemento in range(0,3):
    print(matriz[0][elemento])

    soma = soma + matriz[0][elemento]
print('Soma da linha 0' , soma)

 """
# Somando uma coluna

""" soma = 0
for elemento in range(3):
    print(matriz[elemento][2])
    soma = soma + matriz[elemento][2]

print("Soma da coluna2: ", soma)
 """

# Somando a diagonal principal da matriz

""" soma = 0
for elemento in range(3):
    print(matriz[elemento][elemento])
    soma = soma + matriz[elemento][elemento]

print('Soma da diagonal principal: ', soma)
 """

# Somando a diagonal secundaria
""" matriz = [[1,2,4],[2,3,5],[3,4,5]]
soma = 0
coluna = 2
for linha in range(0,3):
    
    soma = soma + matriz[linha][coluna]
    coluna = coluna - 1

print("Soma da diagonal secundaria ", soma) """

# Trocando linhas
""" 
matriz2 = [[1,2,4],[2,3,5],[3,4,5]]
print_matriz(matriz2)

aux = matriz2[0]
matriz2[0] = matriz[2]
matriz2[2] = aux

print('Matriz após a troca da linha a com a linha 2')
print_matriz(matriz2, False)
 """

# Trocando colunas

""" matriz = [[1,2,4],[2,3,5],[3,4,5]]
soma = 0

print_matriz(matriz)

for e in range(3): 
    # e = 0
    aux = matriz[e][0] # [1,2,4]
    matriz[e][0] = matriz[e][1] # [2,3,5]
    matriz[e][1] = aux # [1,2,4]

print("Matriz após troca da coluna 0 com a 1")
print_matriz(matriz, False)
 """
# Gerando matriz randomica

import random
#matriz 3x3
""" matriz = []

for linha in range(3):
    linha = []
    for coluna in range(3):
        linha.append(random.randint(0,10))
    
    matriz.append(linha)
print(matriz) """


frases = ["Um banco de dados é uma coleção organizada de infos.",
          "SQL é utilizado em bancos relacionais",
          "NoSQL permite que dados não estruturados sejam manipulados"]

for sentence in frases:
    print(sentence)

# Tokenização: segmentação em palavras

tokens = []

for sentenca in frases:
    tokens.append(sentenca.split())

for sentenca in tokens:
    print("Palavras da sentença: ", sentenca)
    for palavra in sentenca:
        print(palavra)