# Code2Flow (permite visualizar fluxogramas)
# https://app.code2flow.com/

# Site para ver os gráficos -> Desmos

# Seleção aninhada -> if dentro de if 
# assim, econseguimos otimizar nosso programa!

a = int(input("Digite o número 1: "))
b = int(input("Digite o número 2: "))
c = int(input("Digite o número 3: "))

if a>b and a>c:
    print(f"O maior é {a}")
else:
    if b>a and b>c:
        print(f"O maior é {b}")
    else:
        print(f"O maior é {c}")


# Exemplo 2: Cálculo de raízes de eq. quadrática
""" 
Fiz o Fluxograma 02 para olhar isso visualmente!
"""
import math

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

delta = b*b - 4*a*C

if delta < 0:
    print("Não há raízes reais")
else:
    if delta == 0:
        x = -B/(2*A)
        print(f"Raiz é {x}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"As raízes são {x1} e {x2}")


# Exemplo 3: Queremos tereminar condiçõe climáticas
""" 
Temperatura acima de 30º e clima úmido (mais de 60%)
Temperatura acima de 30º e não úmido (menos de 60%)
Temperatura de 20º a 30º
Tenoeratura de 10ºa 20º (não incluindo)
Temperatura inferior a 10º
"""

temperatura = float(input("Informe a temperatura em ºC: "))
umidade = int(input("Informe a umidade em % :"))

if temperatura > 30:
    if umidade > 60:
        print('Quente e umido!')
    else:
        print('Quente')
else:
    if (temperatura >= 20 and temperatura <= 30):
        print('Ameno!')
    else:
        if (temperatura >= 10 and temperatura <20):
            print("FRIIIIIO")
        else:
            print("Muiito frio :D")