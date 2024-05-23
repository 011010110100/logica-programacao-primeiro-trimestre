# Comandos de repetição: for, break, continue

# Python tutor para ver o passo a passo das lógicas!

""" 
Quando dizemos repetir -> iterar

temos a iteração 1.determinada ou 2.indeterminada
1. sabemos quantas vezes um bloco de código
deverá ser repetido

2. não é possível determinar antecipadamente quantas
vezes o bloco será repetido (depende de condições
dentro do bloco de código)
"""

# Trabalharemos com as condições determinadas.
#for number in range(1,11):

# podemos omitir o valor inicial (começara em 0)
# for cont in range(10):

# passo -> quanto o valor aumenta, nesse caso: 1, 3, 5, 7 ...
#for cont in range(1,12,2):

import math

for num in range(1,51):
    sqrt = math.sqrt(num)
    print(f"{num:4}: {sqrt:.2f}")

# Exemlpo para calcular o somatório de 1 a n 


n = int(input("N: "))
soma = 0

for cont in range(1,n+1):
    soma = soma + cont
    print(soma)
print(f"Somatório: {soma}")




# Algoritmo de raiz quadrada

num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))

aprox = 1.0
for cont in range(1, total+1):
    aprox = (aprox + num/aprox) / 2
    print(f"{cont:3}: {aprox:5f}")

print(f"Raiz aproximada: {aprox:.5f}")


# BREAK -> para o código em determinado momento que desejarmos


for cont in range(20):
    if cont>10:
        # irá encerrar o código aqui :D
        break
    print(cont)


for cont in range(20):
    if cont % 2 == 1:
        continue
    print(cont)
# pula todos os números ímpares! pois ele irá continuar a iteração
# sem fazer o print, quando o resto da divisão for 1