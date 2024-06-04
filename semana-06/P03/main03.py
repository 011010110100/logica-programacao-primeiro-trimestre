# Repetição indeterminada 

""" 
1. Chico tem 1,50 m e cresce 2 cm por ano. Enquanto zé tem 1,10 m e cresce
3 cm po ano. Quantos anos serão necessários para que zé fique maior que
o chico?
"""

""" 
altura_chico = 1.50
altura_ze = 1.10
ano = 0

while (altura_ze <= altura_chico):
    altura_chico += 0.02
    altura_ze += 0.03
    ano += 1

print(f"Anos: {ano}")
print(f"Eles terão {altura_ze:.2f}m") 
"""

"""
2. Implemente um, programa que leia a idade, altura e gênero de 10 estudantes
a) Media de idades
b) Media de alturas das meninas
c) Percentual de estudantes com mais de 20 anos
d) Altura do estudante mais velho
"""

cont = 0
soma_idades = 0
soma_idades_gt_20 = 0
soma_alturas = 0.0
meninas = 0
maior_idade = 0
maior_altura = 0.0

while True:

    print("Cont: ", cont)
    print("Para encerrar a repetição, informe o valor 0 na idade.")

    idade = int(input("Informe a idade: "))
    if idade == 0:
        print("Fim de programa.")
        break

    while idade <= 0 or idade >= 120:
        print(">Idade inválida, intervalo (0,120)")
        idade = int(input("> Informe novamente a sua idade: "))

    
    altura = float(input("Informe sua altura: "))
    while altura <= 0 or altura >= 2.5:
        print("> Altura inválida. Deve estar no intervalo (0,2.5)")
        altura = float(input("Informe novamente sua altura: "))
    
    genero = int(input("[1] feminino e [2] para masculino: "))
    while genero != 1 and genero != 2:
        print(">Genero invalido. Deve ser 1 ou 2")
        genero = int(input("[1] feminino e [2] para masculino: "))

    if genero == 1: 
        soma_alturas += altura
        meninas += 1

    if idade >= 20:
        soma_idades_gt_20 += 1

    if idade > maior_idade:
        maior_idade = idade
        maior_altura = altura



    soma_idades += idade
    cont = cont + 1

    
if cont == 0: print("Dados não informados")
else:
    print("Media de idades dos estudantes: ", soma_idades/cont)

    #pode ser que não seja informado nenhum genero feminino!
    if meninas == 0: print("Não foram informados dados de meninas")
    else: print("Média das alturas das meninas: ", soma_alturas/meninas)

    print("Percentual de alunos com mais de 20 anos: ", soma_idades_gt_20*(100/cont))

    print("Altura do mais velho: ", maior_altura, maior_idade)

