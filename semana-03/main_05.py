# Aula para prarticar!

"""
1. Implemente um valor inteiro entre 1 a 7 e printe o dia correspondente
da semana! 

1 ------------ Domingo
2 ------------ Segunda
3 ------------ Terca
.
.
.
7 ------------ Sabado
"""

dia = int(input("Informe o dia da semana (1 , 7): "))

if dia < 1 or dia > 7:
    print("Dia inválido!")
else:
    if dia == 1: print('Domingo')
    if dia == 2: print('Segunda')
    if dia == 3: print('Terça')
    if dia == 4: print('Quarta')
    if dia == 5: print('Quinta')
    if dia == 6: print('Sexta')
    if dia == 7: print('Sábado')

""" 
Programa que leia 3 notas, calcule e escreva a média ponderada dela
considerando os pesos 5 2.5 e 2.5. A maior nota deve ter peso 5
"""

nota1 = float(input("Informe a nota1: "))
nota2 = float(input("Informe a nota2: "))
nota3 = float(input("Informe a nota3: "))

if (nota1 < 0 or nota1 > 10) or (nota2>10 or nota3<0) or (nota3<0 or nota3>10):
    print("Notas inválidas!. Devem estar no intervalo [0, 10]")
else:
    maior = nota1
    if nota2>maior: maior = nota2
    if nota3>maior: maior = nota3

    mediaPonderada = 0.5*maior + 0.25*(nota1 + nota2 + nota3 - maior)

    print("A média ponderada será: ", mediaPonderada)


""" 
Vamos fazer um programa para trabalhar com a fórmula de bhaskara
X = -b ‡ ✓(b²-4.a.c) / 2.a     -   Ax² + Bx + C = 0
"""
import math
a = float(input("Informe o valor do A "))
b = float(input("Informe o valor de B "))
c = float(input("Informe o valor de C "))

delta = math.pow(b,2)-4*a*c

if delta < 0 or a == 0:
    print("Não é possível efetuar o cálculo.")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    print("x1: ", x1)
    print("x2: ", x2)

""" 
Implemente um programa que leia o saldo médio de uma conta corrente,
calcule e escreva o limite conforme a tabela

saldo médio                    Limite
menor que R$ 500,00            não há limite
de 500 a 1000,00              8% do saldo médio
maior ou igual a 1000,0         15% do saldo médio
"""

saldo = float(input("Informe o saldo médio: "))

if saldo < 500.00: print("Sem limite! ")

if saldo > 500 and saldo < 1000: 
    limite = saldo*1.08
    print("limite: ", limite)

if saldo > 1000: print("Limite: ", saldo*0.15)