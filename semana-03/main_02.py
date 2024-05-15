# seleção simples -> if

# sintaxe: if expressao_logica: instrucao

"""
Codifique um programa que leia um valor inteiro
e indique se o valor é positivo, negativo ou zero
"""

valor = int(input('Informe um valor: '))

if valor > 0:
    print('O valor é positivo!')
if valor < 0:
    print('O valor é negativo!')
if valor == 0:
    print('O valor é Zero.')

"""
Dado 4 entradas de valores, determine o maior entre eles!
"""

print('Informe o valor1: ')
v1 = int(input())

print('Informe o valor2: ')
v2 = int(input())

print('Informe o valor3: ')
v3 = int(input())

print('Informe o valor4: ')
v4 = int(input())

maior = v1

if v2 > maior:
    maior = v2

if v3 > maior:
    maior = v3

if v4 > maior:
    maior = v4

print('O maior valor é: ', maior)


"""
Implemente um programa que leia dois valores escreva os em ordem!
"""

print('Informe o primeiro valor: ')
valor1 = int(input())

print('Informe o segundo valor: ')
valor2 = int(input())

# (3, 4)  -> (3, 4)
# (10, 5) -> (5, 10)

if valor1 > valor2:
    aux = valor1   # algoritmo para trocar os valores!
    valor2 = valor1
    valor1 = valor2
print(valor1, valor2)

"""
Exercicio - programa que leia altura de uma pessoa (em metros) e
1 para feminino e 2 para masculino. Queremos escrever o peso ideal para
pessoa baseado no genero dela

para homens:   Peso ideal = 72.7 * altura - 58
para mulheres: Peso ideal = 62.1 * altura - 44.7

"""
print('Informe a altura (m): ')
altura = float(input())

print('Informe o gênero, 1 para feminino e 2 para masculino: ')
genero = float(input())

if genero == 1:
    peso = 62.1*altura - 44.7

if genero == 2:
    peso = 72.7*altura - 58

if genero != 1 and genero != 2:
    print("Genero inválido. Peso ideal nao calculado")
    peso = 0

print('Peso ideal: ', peso)
