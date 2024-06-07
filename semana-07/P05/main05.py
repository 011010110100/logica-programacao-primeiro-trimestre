"""
Implementar o jogo da forca
- no inicio o computador escolhe uma palavra
- a cada jogada, o usuário chuta uma letra
- se a letra nao existir, ele perde a jogada
- se existir, ela é exibina na posição correta
"""
import random
import random

def sorteio():
    return random.choice([
        "amarelo", "amiga", "geleia", "janela", "peixe",
        "carro", "bicicleta", "computador", "celular", "livro",
        "caneta", "gato", "cachorro", "praia", "montanha",
        "rio", "floresta", "sol", "lua", "estrela",
        "nuvem", "chuva", "tempestade", "neve", "vento",
        "fogo", "terra", "ar", "água", "espelho",
        "vidro", "porta", "cama", "mesa", "cadeira"
    ])  

def forca(estado):
    estados = [
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =====""",
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =====""",
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =====""",   
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =====""",
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =====""",
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =====""",
        """
        +---+
        |   |
            |
            |
            |
            |
        ====="""
    ]
    print(estados[estado])

palavra = sorteio()
print(palavra)


# gera uma palavra com ____    Ex.: Peixe == _____

tam = len(palavra)
adivinhada = "_" * tam
vidas = 6
letras = "" # letras que serão escolhidas


jogoAtivo = True

while jogoAtivo:

    # Exibe estado do jogo
    print()
    forca(vidas)
    print(adivinhada)
    print(f"Letras já escolhidas {letras}")
    
    letra_valida = False
    while not letra_valida:
        letra = input("Escolha uma letra: ")
        if letra not in letras:
            letra_valida = True
        else:
            print("Esta letra já foi escolhida!")

    # Registrando a letra escolhida
    letras += letra
    
    # Verificando se a letra está na palavra
    if letra in palavra:
        # fazer a troca!
        for pos in range(tam):
            if letra == palavra[pos]:
                adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]

    else:
        print("A letra não percente a palavra :(")
        vidas -= 1
        print(f"Vidas: {vidas}")
        if vidas == 0: 
            forca(vidas)
            jogoAtivo = False
    
    if "_" not in adivinhada:
        print("Parabens! você ganhou")
        jogoAtivo = False


