# vamos ver sobre entradas e saídas

"""
Nosso problema:
Queremos calcular o volume e área de uma esfera
Como calcular?
Volume = (4.π.r³)/3
Area = (4.π.r²)


Etapas:
1. Identificação do problema
    i. Que dados o usuário precisa-rá informar? R: raio
    ii. O que o programa irá retornar?          R: volume
2. Organização da solução
3. Codificação

"""

# nosso imput, por padrão sempre nos retorna uma string!
import math

print('Calculando volume e área da esfera...')
print('Informe o valor do raio (m): ')
raio = float(input())

PI = math.pi

volume = 4/3 * PI * math.pow(raio, 3)
area = 4 * PI * math.pow(raio, 2)

print('O volume da esfera é: ' + str(volume) + 'm³')
print('A área da esfera é: ' + str(area) + 'm²')

# Implemente um programa que leia um valor n e calcule
# e escreva n² n³ e n⁴

print('Digite um valor n : ')
N = float(input())

N_2 = math.pow(N, 2)
N_3 = math.pow(N, 3)
N_4 = math.pow(N, 4)

print('n² n³ e n⁴ são respectivamente: ', N_2, N_3, N_4)
