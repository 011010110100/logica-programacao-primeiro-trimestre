# Uma maneira mais simples de fazer o exercicio de conceito

nota = int(input("Nota: "))

if nota>= 90:
    print("Conceito A")
elif nota>= 80:
    print("Conceito B")
elif  nota>= 70:
    print("Conceito C")
elif nota>= 60:
    print("Conceito D")
else:
    print("Conceito F")


# Exemplo 8: Queremos determinar quantos dias tem um mês!

""" 
Supondo que os meses podem ter 28, 30 ou 31 dias. 
Vamos ignorar os anos bissextos
"""

mes = int(input("Mês: "))

if mes == 2:
    dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30
else:
    dias = 31

print(f"Total de dias {dias}")


# Exemlpo 9: Cálculo do IMC = peso / altura²

altura = float(input("Altura (m): "))
peso = float(input("Peso (kg): "))

imc = peso/altura**2

if imc < 18.6:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
