# Qual nosso problema?

# Problema: somar 2 valores informados pelo usuário

""" 
Modelagem do problema:
Precisamos armazenar os dois valores (por exemplo dois inteiros)
podemos chamar essas variáveis de valor1 e valor2

Vamos apresentar para o usuárario uma forma de inserir ambas as informações

Então, após guardarmos os dados escritos, efetuaremos a soma e retornaremos 
para o usuário
"""
valor1 = int(input('Informe o primeiro valor: '))

valor2 = int(input('Informe o segundo valor: '))

soma = valor1 + valor2

print('A soma será: ' + str(soma))

# Exercícios-----------------------------------------------------------------------

print('Informe seu nome')
nome = input()

print('Nome bonito! ' + nome)

# --------------------------------------------------------------------------------

print('Informe o primeiro valor: ')
valor1 = int(input())

print('Informe o segundo valor: ')
valor2 = int(input())

soma = valor1 + valor2
divisao = soma/2

print('Média Aritmética= ' + str(divisao))
