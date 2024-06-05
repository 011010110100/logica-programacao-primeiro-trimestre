# Escreva um programa que escreva o fatorial dos 100 primeiros inteiros

""" num = 0 

while num <= 99:
    fat = 1
    aux = 2
    while aux <= num:
        fat = fat * aux
        aux = aux + 1
    
    print("O fatorial de ", num, " é", fat)
    num += 1
 """
""" 
Foi feita uma pesquisa entre os habitantes de uma regiao. Foram coletados os dados de idade, 
sexo (1 para masculino e 2 para feminino) e salário. Faça um programa que leia os dados
necessário e informe

a) a média de salário do grupo
b) maior e menor idade do grupo
c) quantidade de mulheres com salário até 3500
"""

somaSalario = 0.0
pessoas = 0
maior_idade = 0
menor_idade = 120

maior_salario_mulher = 0
mulheres = 0

while True:
    print("Informe uma idade negativa para finalizar.")
    idade = int(input("Informe uma idade: "))

    if idade < 0:
        print("Fim de programa")
        break

    while idade <= 0 or idade >= 120:
        print("Idade inváldia. Intervalo (0;120)")
        idade = int(input("> Informe uma idade válida: "))

    genero = int(input("Informe o gênero [1 -feminino e 2 -masculino]"))
    while genero != 1 and genero != 2:
        print("Gênero inválido.")
        genero = int(input("> Informe o gênero [1 -feminino e 2 -masculino]"))
    
    salario = float(input("Informe o salário: "))
    while salario < 0:
        print("Salário inválido")
        salario = float(input("> Informe o salário: "))
    
    somaSalario = somaSalario + salario
    pessoas += 1

    if idade > maior_idade: maior_idade = idade
    if idade < menor_idade: menor_idade = idade

    if genero == 1 and salario <= 3500: mulheres = mulheres + 1


if pessoas == 0:
    print("Dados não informados.")
else:
    print("Média salarial: ", somaSalario/pessoas)
    print("Maior idade do grupo: ", maior_idade)
    print("Menor idade do grupo: ", menor_idade)
    print("Quantidades de mulheres que ganham até R$ 3500,00: ", mulheres) 
