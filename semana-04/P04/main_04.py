# Exemplo 10

""" 
Vamos fazer o jogo pedra, papel e tesoura

Regras (condições de vitória)
1. Tesoura corta papel
2. Papel embrulha a pedra
3. Pedra quebra a tesoura
4. Se ambos usarem a mesma jogada é um empate
"""

import random

jogador = input("Sua escolha [Pe]dra, [Pa]pel, [T]esoura?: " )

comp = random.choice(["Pe", "Pa", "T"])

print(f"Computador escolheu: {comp}")

if jogador == comp:
    print("Empate!")
elif jogador == "Pe":
    if comp == "T":
        print("Pedra quebra Tesoura! Você ganhou")
    else:
        print("Papel cobre Pedra! Você perdeu!")
elif jogador == "Pa":
    if comp == "Pe":
        print("Papel cobre pedra! Você ganhou!")
    else:
        print("Tesoura corta papel, voce perdeu!")
elif comp == "Pa":
    print("Tesoura corta Papel! Você ganhou!")
else:
    print("Pedra quebra tesoura! você perdeu :(")


# Exemlpo 11 

""" 
Pressão arterial é analisada através de duas medições:
Pressão sistólica (indica quanta pressao no sangue está exercendo sobre 
a parece das artérias quando o coração se contrai)

pressão diastólica: indica quanta pressão o sangue está exercendo
sobre a parede das artérias quando o coração está em repouso entre um
batimento e o seguinte


Categoria            Sistólica(mm Hg)      Diastólica(mm Hg)
Normal                   menos 120           menos de 80
Elevada                  120-129             menos de 80
Hipertensão (1)          130-139             80 a 90
Hipertensão (2)       140 ou superior        90 ou superior
Crise Hipertensiva    180 ou superior        120 ou superior
"""

sist = int(input("Sistólica: "))
diast = int(input("Diastólica: "))

if diast >= 120 or sist >= 180:
    print("Crise hipertensiva!")
elif (diast >= 90 and diast < 120) or (sist >= 140 and sist < 180):
    print("Hipertensão estágio 2")
elif (diast >= 80 or diast < 90) or (sist >= 130 and sist <= 140):
    print("Hipertensão Estágio 1")
elif diast < 80 and sist < 130 and sist >= 120:
    print("Elevada")
elif diast < 80 and sist < 120:
    print("Normal")
