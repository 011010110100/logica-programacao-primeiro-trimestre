# seleção composta --> if else

"""
Escreva um valor que leia notas de [0;10] e verifique
e escreva o conceito correspondente conforme a tabela abaixo

nota           Conceito!
9 a 10          A
7 a 8,9         B
5 a 6,9         C
3 a 4,9         D
abaixo de 3     E
"""

print("Informe a nota: ")
nota = float(input())

if nota < 0 or nota > 10:
    print('Erro. Entrada inválida')
    print('A nota deve estar no intervalo [0;10]')
else:
    if nota >= 9 and nota <= 10: print('Conceito A')
    if nota >= 7 and nota < 9: print('Conceito B')
    if nota >= 5 and nota < 7: print('Conceito C')
    if nota >= 3 and nota < 5: print('Conceito D')
    if nota >= 0 and nota < 3: print('Conceito E')

"""
Faça um programa que leia o horário de inicio de um jogo,
em horas e minutos, e o horário de fim desse jogo, também
em horas e minutos. Sabendo que a duração máxima é 24 horas,
determine o tmepo de duração do jogo em horas e minutos

Exemplo de entradas:

"""

horaInicial = int(input("Informe a hora inicial do jogo: "))
minutoInicial = int(input("Informe o minuto inicial do jogo: "))
tempoInicial = horaInicial*60 + minutoInicial
print('Aqui está o horario convertido para minutos: ', tempoInicial)

horaFinal = int(input("Informe a hora final do jogo: "))
minutoFinal = int(input("Informe o minuto final do jogo: "))
tempoFinal = horaFinal*60 + minutoFinal
print('Aqui está o horario final convertido: ', tempoFinal)

# Aqui, temos que começou e terminou no mesmo dia!
if tempoInicial < tempoFinal:
    duracao = tempoFinal - tempoInicial
else: 
    #Aqui, quando ele inicia em um dia e termina no outro!
    duracao = 24*60 - tempoInicial + tempoFinal

print('Horas: ', duracao//60)
print('Minutos: ', duracao%60)


"""
Elabore um programa que leia um número inteiro de 4 digitos. 
A seguir, o programa deve detrerminar se o número lido é capicua.
Isto é, quando lido da esquerda para a direita ou da direita para 
esquerda representa o mesmo número
"""

numero = int(input('Informe o valor inteiro de 4 digitos: '))

if numero < 1000 or numero > 9999:
    print('Valor inválido! não tem 4 digitos')
else:
    milhar = numero//1000
    resto = numero%1000
    centena = resto//100
    resto = resto%100
    dezena = resto//10
    unidade = resto%10

    invertido = unidade*1000 + dezena*100 + centena*10 + milhar
    print(milhar, "MILHAR")
    print(centena, "CENTENA")
    print(dezena, "DEZENA")
    print(unidade, "UNIDADE")
  
    
    print('Valor ao contrário: ', invertido)
    if numero == invertido: print('CAPICUA')
    else: 
        print('Não é capicua :(')