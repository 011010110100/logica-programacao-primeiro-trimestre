# Exercício com manipulação de strings

# Programa para verificar o palíndromo (reviver <-> reviver)

""" palavra = input("Palíndromo? : ")

dif = False

comprimento = len(palavra)

for pos in range(comprimento//2):
    if palavra[pos] != palavra[-1-pos]:
        dif = True
        break

if dif:
    print("Não é um palíndrimo!")
else:
    print("É um palíndromo :D") """

# Outro jeito mais simples para isso!

""" texto = input("Palindromo?: ")

if texto != texto[::-1]:
    print("A frase não é um palíndromo...")
else:
    print("A frase é um palíndromo!")
 """

# Exemplo 22: conte a quantidade de vogais presentes em uma string
# a, e, i, o, u

""" 
precisaremos percorrer todas as letras, e se ele encontrar
qualquer uma dessas vogais, aumentará a contagem.
"""

texto = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
totalVogais = 0

for letra in texto:
    if letra in vogais:
        totalVogais += 1


# Programa para verificar se uma senha é Forte!

""" 
Minimo de 8 caracteres
Pelo menos uma letra maiúscula
Pelo menos um dígito entre 0-9
Pelo menos um caractere de pontuação
"""

import string

senha = input("Senha: ")

maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8:
    print("Erro: senha muito curta")
else:
    for letra in senha:

        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito = True
        if letra in string.punctuation:
            pontuacao = True

if maiuscula == False or digito == False or pontuacao == False:
    if maiuscula == False:
        print("Erro: senha não tem maiúsculas")
    if digito == False:
        print("Erro: senha não tem dígitos")
    if pontuacao == False:
        print("Erro: senha não tem caractere de pontuação")
else:
    print("Senha Forte!")
        


# Fazer um programa para mostrar as letras iniciais de um nome!
# exemlpo: Marcos Brito Paceka -> M. B. P.

nome = input("Digite um nome completo: ")

inicio = True

for letra in nome:
    if inicio:
        print(f"{letra}.", end="")
        inicio = False
    elif letra == " ":
        inicio = True