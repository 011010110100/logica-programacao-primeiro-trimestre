# Repetições aninhadas 

""" 
for numero in range (1,11):
    for valor in range(1,11):
        print(valor, ' x ', numero, ' = ', numero * valor)
    print() 
"""

# 2º modo de fazer

""" 
numero = 1
while numero <= 10:
    valor = 1
    while valor <= 10:
        print(valor, '  x ', numero, ' = ', numero*valor)
        valor += 1
    print()
    numero += 1
"""
""" 
Ex.1 Implemente um programa que escreve os divisores 
dos 100 primeiros valores inteiros 
"""
""" 
for num in range(1,101):
    print(">>Número: ", num)
    d = 1
    while d <= num:
        if num % d == 0: print(d , " divide ", num)
        d = d + 1
"""

# Ex.2 Implemente um programa que escreve os N primeiros primos
""" 
quantidade = int(input("Informe a quantidade de números primos: "))


while quantidade <= 0:
    print(">Valor inválido. Valor deve ser positivo")
    quantidade = int(input("Informe a quantidade de números primos: "))

num = 2
contador_primos = 0

while contador_primos < quantidade:
    contaDivisores = 0
    d = 1

    while d <= num:
        if num % d == 0: contaDivisores += 1
        d += 1
    
    if contaDivisores == 2:
        print(num)
        contador_primos += 1
    num += 1
"""

# Ex.3 Conjectura de goldbach
""" 
"Todo número par maior ou igual a 4 é a soma de dois primos"
Faça um programa que leia um valor n, inteiro e positivo, e escreva
os n primeiros pares acima de 4 juntamente com os primos em que cada
par pode ser decomposto
Ex.:
4 --> 2 e 2
6 --> 3 e 3
8 --> 3 e 5
"""

num = int(input("Informe um valor par maior que 4: "))

while (num <= 4 or num % 2 != 0):
    print(">Valor inválido. Digite novamente")
    num = int(input("Informe um valor par maior que 4: "))

parte1 = num//2
parte2 = parte1

while parte2 <= parte1:
    contParte1 = 0
    d = 1
    while (d <= parte1):
        if (parte1 % d == 0): contParte1 += 1
        d += 1
    
    # se a primeira for primo, continue
    if contParte1 == 2:
        d = 1
        contParte2 = 0
        while (d <= parte2):
            if (parte2 % d == 0): contParte2 += 1 
            d += 1
        
        if contParte2 == 2:
            print("Primo1: ", parte1, "Primo2: ", parte2)
            break

    parte1 += 1
    parte2 -= 1
