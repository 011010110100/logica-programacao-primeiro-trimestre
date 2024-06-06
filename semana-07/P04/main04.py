

# Ex.1) Implementando a Conjectura de Goldbach

"""
Conjectura de Goldbach-- 
Qualquer número par acima de 2 pode ser gerado com a soma de dois primos
"""

def primo(numero):
    for div in range(2, numero//2 + 1):
        if numero % div == 0:
            return False
    return True

def goldbach(numero):
    for v1 in range(2, numero):
        v2 = numero - v1
        if primo(v1) and primo(v2):
            return v1, v2
        
for num in range(4, 1000, 2):
    primo1, primo2 = goldbach(num)
    print(f"{num:3}: {primo1} + {primo2}")

# Ex. 2) Cálculo da distância entre dois pontos
import math
"""
Resolução através do teorema de pitágoras
d = sqrt(Δx² + Δy²)
"""

def distancia (x1, y1, x2, y2):
    deltax = x1-x2
    deltay = y1-y2

    dist = math.sqrt(deltax**2 + deltay**2)
    return dist


# Ex. 3) Função para determinar a menor distância entre 3 pontos

def menorDist(x1,y1,x2,y2,x3,y3):
    d12 = distancia(x1,y1,x2,y2)
    d13 = distancia(x1,y1,x3,y3)
    d23 = distancia(x2,y2,x3,y3)
    return min(d12, d13, d23)


# 4) Fatorial
 
def fatorial(num):
    fat = 1
    for cont in range(1, num+1):
        fat = fat * cont
    return fat

def binomial(n,k):
    return fatorial(n)//(fatorial(k)*fatorial(n - k))


# 5) Fatorial melhorado

def binomial12(n,k):
    prod = 1
    total = k

    if n-k < k:
        total = n-k
    
    for i in range(1, total + 1 ):
        prod = prod * ((n + 1 - i)/ i)
    
    return int(prod)

# 6) Gerar o Triângulo de Pascal

def pascal(linhas):
    for linha in range (linhas):
        for coluna in range(linha + 1):
            valor = binomial12(linha, coluna)
            print(f"{valor} ", end="")
        print()
    
pascal(40)