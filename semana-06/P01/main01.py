# Programas com repetição - while

""" 
while expressao_logica:
    instrucao1
    intrucao2
    .
    .

executa tudo o que está dentro de seu bloco enquanto a expressão 
lógica for verdadeira!


Indeterminada -> quando não podemos saber quantas vezes o bloco será
repetido (depende de condições que ocorrerão dentro do bloco)
"""

# Exemlpo 1. Programa que escreva valores de 1 a 10

""" 
num = 1
while (num <= 10):
    print(num)
    num += 1 
"""


# Exemplo 2. Calcule o fatorial de um valor natural

""" 
valor = int(input("Informe um valor natural: "))

fat = 1
aux = 2

while (aux <= valor):
    fat = fat * aux
    aux += 1

    print(f"Fatorial {aux - 1}!: ", fat) 
"""


""" 
valor = int(input("Informe um valor natural: "))

d = 1

while d <= valor:
    if valor % d == 0: print(d, ' divide', valor)
    d += 1 
"""


# Algoritmo para verificar se é primo

# Minha resolução
valor = int(input("Digite um valor: "))

d = 1
controle = True

while d <= valor:
    if valor % d == 0:
        if (valor != d and d != 1):
            print("Não é primo.")
            print(f"Divisível por {d}")
            controle = False
            break
    d = d+1

if controle: print("O número é primo!")

# resolução da professora
cont = 0
while d <= valor:
    if valor % d == 0: cont += 1
    d = d + 1

if cont == 2: print(valor, "eh primo")
else: print(valor, "Não é primo")
