# Estruturas de dados -> listas e tuplas
"""
Tupla: estrutura de dados usada para representar uma sequencia de itens.
--> registros
Registros mantém dados relacionados.
É imutável e é representada entre ( ) e seus itens são separados por virgula
('Lucas', 100)

Podem ser usadas dentro de listas

[('Vitor',100), ('Lucas',130), ('Luiza', 200), ('Marta', 80)]
"""


# Acessando elemtos
""" 
tupla = ('banana', 'ameixa', 'pera')

print(tupla) #('banana', 'ameixa', 'pera')
print(tupla[0]) #banana

for item in tupla:
    print(item)
"""
""" 
Exemplo: uma empresa ed estatística analisou os 5 melhores jogadores de uma
liga profissional de basquete e registrou os pontos, assistência e rebotes 
de cada um. Para isso, crie uma lista de tuplas onde cada trupla é da forma
-------------(nome do jogador, pontos, assistência, rebotes)
Ao final, deveremos percorrer a lista e informar a tupla do jogador que tem
as melhores estatísticas --> ((pontos+assistencias+rebotes)/3)
"""
""" 
jogadores = []

cont = 1
while (cont<=3):
    print("Contador: ", cont)

    nome = input("Informe o nome do jogador: ")
    pontos = int(input("Quantos pontos ele fez? "))
    assistencias = int(input("Quantas assist. ele fez? "))
    rebotes = int(input("Quantos rebotes ele pegou? "))
    jogadores.append((nome, pontos, assistencias, rebotes))

    cont += 1
print("A lista com os jogadores: ", jogadores)

estatisticas = []

for dados in jogadores:
    soma = 0
    for i in range (1,4):
        soma = soma + dados[i]
    
    media = soma/3
    estatisticas.append((dados[0], media))
print(estatisticas)

melhor = estatisticas[0] # definimos um valor inicial para poder comparar

for item in estatisticas:
    # onde item[1] é a média dos pontos feito pelo jogador.
    if (item[1] > melhor[1]): melhor = item

print("Melhor jogador: ", melhor)
"""

""" 
Exercício ----

Foram vendidas 50 peças de roupa. De cada peça pela foram coletados os seguintes atributos:
    - Tamanho (P, M ou G) e cor (branco, preto ou azul). O programa deve ler os dados
    das peças de roupa e organizá-los em uma lista de tuplas
    - Tuplas da forma (tamanho, cor)
    - deve calcular e escrever: o tamanho que mais vendeu, a qtd de peças de tamanho M
    que foram vendidas e a cor preferida pelos clientes
"""
import random

pecas_vendidas = []

for i in range(50):
    #Vamos fazer um sorteio tanto para o tamanho quanto para a cor
    #-- Tamanho
    tamanho = random.choice(["P", "M", "G"])
    #-- Cor
    cor = random.choice(["preta", "azul", "branca"])

    pecas_vendidas.append((tamanho, cor))
print(pecas_vendidas)


contP = 0
contM = 0
contG = 0
cores = []

for peca in pecas_vendidas:
    if peca[0] == "P": contP += 1
    else:
        if peca[0] == "M": contM += 1
        else: 
            contG += 1
    
    cores.append(peca[1])

totaliza_tamanho = []
totaliza_tamanho.append(("Pequeno", contP))
totaliza_tamanho.append(("Medio", contM))
totaliza_tamanho.append(("Grande", contG))


maior = 0
tamanho = ""
for item in totaliza_tamanho:
    if item[1] > maior:
        maior = item[1]
        tamanho = item[0]

print("Tamanho que mais vendeu: ", tamanho, "Vendeu", maior, " pecas")
print("Quantidade de tamanho M vendido: ", totaliza_tamanho[1])

# verificando a quantidade se baseando na cor!
print("Quantidade de pecas brancas vendidas: ", cores.count("branca"))
print("Quantidade de pecas Azuis vendidas: ", cores.count("azul"))
print("Quantidade de pecas Pretas vendidas: ", cores.count("preta"))
    