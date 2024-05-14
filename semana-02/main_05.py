# Dia de prática!
import math

"""
Algoritmo para converter de Graus Fahrenheit para Celsius
Fórmula: C = 5/9 (f - 32)
"""

# Vamos ler os valores em Fahrenheit!
print('Informe o valor em Farenheit: ')

Fahrenheit = float(input())

converte_para_celcius = 5/9 * (Fahrenheit - 32)

print('Celsius: ', converte_para_celcius)

"""
Construa um programa que leia dois valores inteiros e escreva na tela
a) A soma
b) A diferença
c) A média
d) a distância (ou seja, o valor absoluto da diferença)
e) o maior dos dois ( use maior = (a + b + |a - b|)/2 )
f) o menor dos dois (use menor = (a + b - |a - b|)/2 )
"""

print('Informe o primeiro valor: ')
valor1 = int(input())

print('Informe o segundo valor: ')
valor2 = int(input())

soma = valor1 + valor2
print('A) A soma é: ', soma)

diff = valor1 - valor2
print('B) A diferença é: ', diff)

media = (valor1 + valor2)/2
print('C) A média é: ', media)

distancia = math.fabs(valor1-valor2)
print('D) A distância será: ', distancia)

maior_valor = (valor1 + valor2 + math.fabs(valor1 - valor2))/2
print('E) O maios número é: ', maior_valor)

menor_valor = (valor1 + valor2 - math.fabs(valor1 - valor2))/2
print('F) O menor valor é: ', menor_valor)


"""
Um progama que lê o tempo de um evento em segundos e o escreve
em horas, minutos e segundos.
hora    ->  0 ao 23
minuto  ->  0 ao 59
segundo ->  0 ao 59
"""

print('Informe o tempo do evento em segundos: ')
tempo = int(input())

horas = tempo//3600      # usamos divisão inteira!
resto_horas = tempo % 3600

minutos = resto_horas//60
resto_minutos = resto_horas % 60

segundos = resto_minutos

print('Horas: ', horas)
print('Minutos: ', minutos)
print('Segundos:', segundos)

"""
Implemente um programa que lê um valor inteiro de 4 dígitos.
A seguir, o programa escreve um inteiro que corresponde ao lido na
ordem inversa 1234 -> 4321
"""

print('Informe um inteiro de 4 dígitos!: ')
inteiro = int(input())

# Exemplo 1234 
milhar = inteiro//1000           # 1
resto_milhar = inteiro % 1000

centena = resto_milhar//100     # 2
resto_centena = resto_milhar % 100

dezena = resto_centena//10     # 3
resto_dezena = resto_centena % 10

unidade = resto_dezena         # 4

inversa = unidade*1000 + dezena*100 + centena*10 + milhar*1

print(inteiro, '->', inversa)
