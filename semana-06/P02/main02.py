# Repetições determinadas

""" 
Implemente um prograwma que  calcula a soma dos n primeiros termos 
Ex.: 1 + 1/2 + 1/3 + 1/4 ... até 1/N

numerador sempre 1 <-> e o denominador variando.
"""

""" n_termos = int(input("Informe a quantidade de termos: "))

if n_termos <= 0:
    print("Número inválido. Informe um valor positivo")
else:
    soma = 0.0
    cont = 1.0

    while(cont <= n_termos):
        soma = soma + 1/cont
        cont += 1
    
    print("Soma: ", soma)
 """

""" 
Implemente um prograwma que  calcula a soma dos n primeiros termos 
Ex.: 2 + 4/3 + 6/5 + 8/7 + 10/9

Podemos perceber que ambos crescem de dois em dois. Tanto o nominador
quando o denominador
 
Numerador   -> pares
Denominador -> ímpares
"""

""" n_termos = int(input("Informe a quantidade de termos: "))

if n_termos <= 0:
    print("Número inválido. Informe um valor positivo")
else:
    soma = 0.0
    cont = 1.0
    
    numerador = 2
    denominador = 1

    while(cont <= n_termos):
        soma = soma + numerador/denominador
        cont += 1
        
        numerador = numerador + 2
        denomionador = denominador + 2
        print(f"A soma na iteração {cont} é {soma}")
    
    print("Soma: ", soma)
 """


""" 
3. Implemente um programa que leia dois valores a e b. O programa
deve escrever e som ar os valores ímpares! existentes entre a e b

Ex.: a = 10 e b = 16  ----> 11 13 e 15 soma => 39
"""

# Validações de entrada
""" a = int(input("Informe o limite inferior: "))
while a < 0: 
    print("O valor inicial do intervalo deve ser Natural!")
    a = int(input("Informe novamente limite inferior: "))


b = int(input("Informe o limite superior: "))
while b<0: 
    print("O valor final do intervalo deve ser Natural!")
    b = int(input("Informe novamente o limite superior: "))
    
    # Início da lógica!

if a>b:
    aux = a
    a = b
    b = aux
        
if a%2 == 0:  a = a + 1
soma = 0

while (a <= b ):
    print(f"{a}, ", end = "")
    soma = soma + a
    a = a + 2
        
print("A soma dos ímpares será: ", soma)
 """


"""
4. Implemente um programa que leia um valor e verifique se ele é 
um número perfeito, ou seja, se a soma de seus divisores iguala ao valor

ex.: 6   -> divisores 1  2 e 3 = 1 + 2 + 3 = 6
"""

num = int(input("Informe um valor inteiro e positivo: "))

while num <= 0:
    print("Erro. O valor deve ser positivo")
    num = int(input("Informe um valor inteiro e positivo: "))

soma = 0
d = 1

while (d <= num/2):
    if num % d == 0: soma = soma + d
    d += 1

if soma == num : print("O número é perfeito")
else: print("O número não é perfeito")
