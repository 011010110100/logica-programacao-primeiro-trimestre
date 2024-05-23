# Vamos fazer um programa para decidir quando ele para de iterar
# sobre a lógica da raíz quadrada baseada no "erro" que decidirmos


"""
num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))

aprox = 1.0
anterior = 0.0

for cont in range(1, total + 1):
    aprox = (aprox + num/aprox) / 2
    print(f"{cont:3} {aprox:.5f}")
    dif = abs(aprox - anterior)
    if (dif < 0.001):
        break

    anterior = aprox

print(f"Raiz aproximada: {aprox:.5f}") 
"""


# Exemplo: ler 10 valores e ler a média deles.

""" 
soma = 0.0

for cont in range(10):
    alt = float(input("Digite uma altura: "))
    soma = soma + alt

media = soma / 10

print(f"A média: {media:.3f}") 
"""

# Retorne a maior altura entre as sorteadas

import random

soma = 0.0
maior = 0.0

for cont in range(10):
    alt = random.uniform(1.5,2.10)
    soma = soma + alt
    if alt > maior:
        maior = alt

print(f"Maior altura: {maior:.2f}")


"""
Problema: foram entrevistador 50 estudantes
de cada, foram coletados os seguintes dados: idade, semestre e curso

Devemos ler (sortear) os dados dos estudantes e calcular:
- media
- curso (do aluno mais velho)
- quantidade de alunos que estão no 5º Semestre
"""

# Entradas: sequência de idades, cursos, semestres

# Saídas: 
# média de idade, curso do aluno mais velho e a maior idade
# quantidade de alunos no 5º semestre

somaIdades = 0
cursoMaisVelho = ""
idadeMaisVelho = 0
qtdAlunos5Semestre = 0

for cont in range(50):
    #Sorteio
    idade = random.randint(18,60)
    curso = random.choice(["Eng. Civil", "Eng. Mec", "Eng. Química", "Eng. Produ.",])

    semestre = random.randint(1,10)

    print(f"{idade} {curso} {semestre}")

    # Coleta de estatísticas
    # Media de idades =e necessário somar
    somaIdades += idade

    # Curso do aluno mais velho
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        cursoMaisVelho = curso
    
    # Total de alunos no 5. Semestre
    if semestre == 5:
        qtdAlunos5Semestre += 1

mediaIdades = somaIdades // 50

print(f"media de idades {mediaIdades}")
print(f"curso do aluno mais velho {cursoMaisVelho}")
print(f"quantidade de aluno no 5º Semestre {qtdAlunos5Semestre}")