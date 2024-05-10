# Expressões aritméticas matemáticas


# OPERADORES
"""
+  : adição
-  : subtração
*  : multiplicação
** : potenciação       2**3 = 8
/  : divisão real       7/2 = 3.5
// : divisão interna   7//2 = 3
%  : resto da divisão  7%2  = 1
"""

# para trabalharmos com funções matemática -> import math

import math

# sqrt -> square root
print(math.sqrt(4))  # 2

B = 10
A = 1
C = 1

delta = math.sqrt(B*B - 4*A*C)
print("Nosso delta será: " + str(delta))

# sqrt(b^2-4.a.c)   -> pow - potencia
resultado = math.sqrt(math.pow(B, 2)-4*A*C)

# Módulo em matemática -> | b^3 - 10 |  valores absolutos!
# floating-point absolute == fabs
modulo1 = math.fabs(math.pow(B, 3) - 10)

# | a - 2c|
modulo2 = math.fabs(A - 2*C)

# N!/((n-p)!p!)     Fatorial -> x!:  math.factorial(x)
n = 10
p = 5
formula = math.factorial(n)/(math.factorial(n-p)*math.factorial(p))
print('Calculando a expressao: ' + str(formula))

# Maior divisor comum (mdc)
MDC = math.gcd(10, 30)

# Arredondamento -
# ceil - arredonda o inteiro mais proximo para cima
# trunc - simplesmente despreza a parte da fracao

arredonda_para_cima = math.ceil(9.1)    # 10
despreza_fracionario = math.trunc(9.7)  # 9

# Funcoes trigonometricas sin e cos
PI = math.pi
seno = math.sin(PI)
print("VALOR SERÁ: " + str(seno))


# EXERCICIO - transformas as expressoes da aula para o código!

primeiro_termo = (math.sqrt((A + 3*B)/(B+1)) + B**5)/math.fabs(B-A)

segundo_termo = (math.sqrt(math.sqrt(A) + 1))/(B + 3 * A + B*(A**5))

formula1 = primeiro_termo + segundo_termo - 1

print(formula)
