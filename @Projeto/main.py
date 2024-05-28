# Qual o nosso problema?

"""
- implementar um programa que leia, valide e analise dados informados pelo usuário.
- dados meteorológicos de 2021

- todas as entradas de dados devem ser validades. Caso venha um valor errado, informar
ao usuário o erro e permitir que ele redigite o dado.

Dados colerados:

1. mês (1 a 12)
    |_ deverá ser informado para cada mês: 
        - temperatura máxima (ºC) intevalo de [-60,50]

Então calcularemos:
1. Média das temperaturas máximas informadas  
2. Quantidades de mêses escaldantes (aqueles com Temperatura Máxima acima de 33º) 
3. Mês mais escaldante do ano (mês com a maior Temperatura Máxima registrada)
    |_ deve ser escrito na tela por extenso!
4. Mês menos quente do ano.
    |_ deve ser escrito na tela por extenso!

Exemplo de dados:

Mês     temperatura  
------|-------------
1          34,3  
2          26      
3          31      
4          31,7
5          31  
6          20  
7          17  
8          42,5  
9          37  
10         32,1 
11         33   
12         23 
"""

# para executar o código basta rodar no terminal - python main.py

soma_temperaturas = 0.0
meses_escaldantes = 0

mes_mais_escaldante = 0.0
mes_mais_escaldante_escrito = ""

mes_menos_escaldante = 50.0
mes_menos_escaldante_escrito = ""


# percorrer os mêses de 1 a 12 
for i in range(1,13):
    if i == 1:
        mes_escrito = "Janeiro"
    elif i == 2:
        mes_escrito = "Fevereiro"
    elif i == 3:
        mes_escrito = "Março"
    elif i == 4:
        mes_escrito = "Abril"
    elif i == 5:
        mes_escrito = "Maio"
    elif i == 6:
        mes_escrito = "Junho"
    elif i == 7:
        mes_escrito = "Julho"
    elif i == 8:
        mes_escrito = "Agosto"
    elif i == 9:
        mes_escrito = "Setembro"
    elif i == 10:
        mes_escrito = "Outubro"
    elif i == 11:
        mes_escrito = "Novembro"
    elif i == 12:
        mes_escrito = "Dezembro"

    temperatura = float(input(f"Informe a temperatura em ºC de {mes_escrito} : "))

    # Garantindo que irá enviar uma temperatura no intervalo desejado.
    while (temperatura < -60.0 or temperatura > 50.0):
        print("Temperatura inválida. Digite um valor entre -60º e 50º")
        temperatura = int(input(f"{mes_escrito} ºC : "))
    
    soma_temperaturas += temperatura

    # Verificando a quantidade de mêses escaldantes
    if (temperatura > 33):
        meses_escaldantes += 1

    # Verificando o mês com maior temperatura
    if temperatura > mes_mais_escaldante:
        mes_mais_escaldante = temperatura
        mes_mais_escaldante_escrito = mes_escrito
    
    # Verificando o mês com menor temperatura
    if temperatura < mes_menos_escaldante:
        mes_menos_escaldante = temperatura
        mes_menos_escaldante_escrito = mes_escrito


media_temperaturas = soma_temperaturas / 12

print("===========RESULTADOS===========")
print(f"A média da temperatura é: {media_temperaturas:.2f} ºC")
print(f"Quantidade de mêses escaldantes: {meses_escaldantes}")
print(f"O mês mais escaldante do ano foi: {mes_mais_escaldante_escrito}")
print(f"O mês menos escaldante do ano foi: {mes_menos_escaldante_escrito}")
