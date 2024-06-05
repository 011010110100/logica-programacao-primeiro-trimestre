# Funcoes

""" 
Escopos locais versus globais

local -> só pdoe ser acessado durante o funcionamento da função
global -> existe ao longo de todo programa, podendo ser acessado
em diversos locais
"""

def calcula (base, taxa, duracao):
    final = base * (1+taxa) ** duracao
    return final

b = float(input("Valor inicial: "))
t = float(input("Taxa de juros mensal: "))
d = int(input("Duração (meses): "))

res = calcula(b,t,d)

print(f"Valor no final do periodo {res:.2f}")


# def calcula(base, taxa=0.1, duracao=12): 
"""
Valores padrões para o código! ou seja, caso não seja informado
irá utilizar esses valores para a taxa e para duracao

"""

def calcula(base, taxa=0.1, duracao=12):
    final = base * (1 + taxa) ** duracao
    return final

b = float(input("Valor inicial: "))
d = int(input("Duração (meses): "))
res = calcula(b, duracao=d) # aqui iremos usar o primeiro e terceiro arg
print(f"Valor no final do periodo {res:.2f}")