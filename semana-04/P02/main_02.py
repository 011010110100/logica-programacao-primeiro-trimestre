""" 
Exercicio

Aprovação de aluno por nota e frequência, com exame

Aluno realiza 3 provas, com mesmo peso.
Grau1 -> média aritmética das provas
Frequência -> pelo menos 75%


Se G1 for igual ou superior a 7 - aprovado em G1
G1 inferior a 4 -> reprovado
G1 for inferior a 7, o aluno deverá realizar um exame G2

Se a média entre G1 e G2 for >= 5, o aluno estará aprovado em grau2
se a média for menor que 5, estará reprovado!

Fluxograma -> F01
"""

# precisamos ler a nota das provas P1, P2, P3
# precisamos também do percentual de frequência!


# Exemplo4: Aprovação por nota e frequência

p1 = float (input("P1: "))
p2 = float (input("P2: "))
p3 = float (input("P3: "))

freq = float(input("Freq: "))

g1 = (p1+p2+p3)/3

if freq < 75:
    print(f"Reprovado por frequencia {freq}!")
else:
    if g1 >= 7:
        print(f"Aprovado com média {g1}")
    else:
        if g1<4:
            print(f"Reprovado com média {g1}")
        else:
            # Em exame (G2)
            g2 = float(input("G2: "))
            final = (g1+g2)/2
            if final > 5:
                print("Aprovado!")
            else:
                print("Reprovado")


# Exemplo 5: Conceito em função da nota A B C D E F

nota = int(input("Nota: "))

if nota >= 90:
    print("Conceito A")
else:
    if nota >= 80:
        print("Conceito B")
    else:
        if nota >= 70:
            print("Conceito C")
        else:
            if nota >= 60:
                print("Conceito D")
            else:
                print("Conceito F")

# Exemplo 6: Determinar a data da páscoa em um ano específico

ano = int(input("Ano: "))

if ano < 1900 or ano > 2099:
    print("Não podemos calcular fora do interválo") 
else:
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19*a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dia = 22 + d + e

    if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
        dia = dia - 7
    if dia > 31:
        dia = dia - 31

    print(f"Dia da páscoa: {dia}")  
