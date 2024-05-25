# Exercícios de fixação :D

""" 
Ex. 1) Jogo da adivinhação
-> objetivo é adivinhar um número sorteado pelo computador

- No início, ele irá sortear um número entre 1 e 100
- Temos 10 chances para adivinhar
- A cada chance o computador deve informar se o número
é maior ou menor ou se é igual ao sorteado
se for igual, ganhamos!
"""

""" import random

sorteado = random.randint(1,100)
# print(f"O número sorteado foi : {sorteado}")

acertou = False

for tentativa in range(1,11):
    print(f"Tentativa {tentativa}: ", end="")
    num = int(input())
   
    if num < sorteado:
        print("Tente um número maior...")
    elif num > sorteado:
        print("Tente um número menor...")
    else:
        print("Parabéns! você acertou")
        acertou = True
        break

if not acertou:
    print(f"O número sorteado foi...... {sorteado}")
 """


""" 
Ex. 2)Foram entrevistados 2.000 habitantes de uma cidade. 
Cada habitante foram coletados os seguintes dados:
idade, renda, gênero e número de filhos. O programa deve
obter os dados desses habitantes, calcular e escrever:
a) média de renda
b) media de idade de quem tem mais de 3 filhos
c) quantidade de homens com menos de 30 anos
d) media do número de filhos
e) renda do homem mais velho
f) idade da mulher com maior renda
"""

import random

soma_rendas = 0
soma_idades = 0
qtd_mais_3_filhos = 0
qtds_homens_menor_30 = 0
soma_filhos = 0
renda_homem_mais_velho = 0
idade_homem_mais_velho = 0
idade_mulher_maior_renda= 0
mulher_maior_renda = 0

total_habitantes = 2000

for cont in range(2000):
    # coleta de dados do "senso"
    idade = random.randint(18,80)
    renda = random.randint(1200, 12000)
    genero = random.choice(["M", "F"])
    filhos = random.randint(0, 5)

    # 1. média de rendas - somar
    soma_rendas += renda

    # 2. Média de idade com mais de 3 filhos
    if (filhos > 3):
        soma_idades += idade
        qtd_mais_3_filhos += 1
    
    #3. Quantidade de homens com mais de 30 anos.
    if genero == "M" and idade < 30:
        qtds_homens_menor_30 += 1

    #4. Média do número de filhos
    soma_filhos += filhos

    #5. Renda do homem mais velho
    if genero == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        renda_homem_mais_velho = renda
    
    #6. Idade da mulher com maior renda
    if genero == "F" and renda > mulher_maior_renda:
        idade_mulher_maior_renda = idade
        mulher_maior_renda = renda
    

media_renda = renda/total_habitantes
media_mais_3_filhos = soma_idades // qtd_mais_3_filhos
media_filhos = soma_filhos // total_habitantes

print("="*30)
print(f"a) Média de renda:{media_renda}")
print(f"b) Média de idade com mais de 3 filhos: {media_mais_3_filhos}")
print(f"c) Total de homens com menos de 30 anos: {qtds_homens_menor_30}")
print(f"d) Media no número de filhos: {media_filhos}")
print(f"e) Renda do homem mais velho: {renda_homem_mais_velho}")
print(f"f) Idade da mulher com maios renda: {idade_mulher_maior_renda}")
