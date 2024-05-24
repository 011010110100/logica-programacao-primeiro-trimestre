# Coleção -> qualquer tipo de dado capaz de armazenar outros dados dentro!

# Coleção de caracteres == string

texto = "Esse é um belo texto"
print(texto[0]) # primeiro elemento

texto = "Esta"
print(texto + " é uma string") # Podemos fazer operações com eles!

print("==" * 15)


# fatiamento texto[inicial:final:passo]

texto = "Este é meu texto!"
print(texto[0:2]) #"Es"


#  operador de pertencimento "in"

texto1 = input("Digite uma frase: ")
texto2 = input("Digite uma palavra: ")

if texto2 in texto1:
    print(f"{texto2} está na frase!")
else:
    print(f"{texto2} não está na frase...")


# comprimento de caracteres -> função len

texto = "quantos caracteres eu tenho?"
print(f"{len(texto)} caracteres")


# vamos processar cada caractere individualmente na string!

texto = input("Digite uma frase: ")

for caractere in texto:
    print(caractere)


for pos in range(len(texto)):
    print(texto[pos])