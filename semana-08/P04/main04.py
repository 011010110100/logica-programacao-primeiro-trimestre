# Aqruivos

"""
--> aprender a trabalhar em disco (utilizando arquivos)

Arquivos: mantém dados de forma permanente no disco.
Os dados serão mantidos em formato de texto.

Operçaões básicas:
    - Abrir um arquivo
    - Fechar um arquivo
    - Ler um arquivo (trazer dados do disco para memória principal)
    - Gravar em um arquivo (gravar os dados em memória principal em disco)

    
    
1º Arquivos devem ser abertos para:
    - Leitura, Escrita e Alteração

sintaxe:
variavel_arquivo = open(nome_do_arquivo, proposito)

nome_do_arquivo - pasta em que está o programa

propósito - r (leitura), w (gravação), a (append, alteração)


    
ex,: percorrendo um arquivo

arq = open("planta_iris.data", "r")
for linhna in arq:
    print(linha)
arq.close()

--> se não houver quebra de linhas no arquivo, precisamos fazer um split

lista = variavel_string.split(separador)


-------------PARA GRAVAR
variavel_arquivo.write(item)
 --> item deve ser string

"""
""" 
ref_arquivo = open("dados.txt", "a")

for i in range(3):
    nome = input("Informe o nome: ")
    ref_arquivo.write(nome + "\n")

ref_arquivo.close()

 """
""" 
Todos os dados SÃO DO TIPO STRING


-- crie arquivo alturas.txt com o nome e altura de 5 pessoas cujos dados
foram informados via teclado. A seguir abra o arquivo, leia os dados
e informe: média de altura, nome da pessoa mais alta.
"""

arquivo = open("alturas.txt", "w")

cont = 1
while cont<=5:
    nome = input("Informe o nome: ")
    altura = float(input("Informe a altura: "))
    arquivo.write(nome + ' - ' + str(altura) + "\n")
    cont += 1
arquivo.close()


lista  = []
soma = 0
nomeAlto = ""
alturaAlto = 0

arquivo = open("alturas.txt", "r")

for linha in arquivo:
    saida = linha[:-1].split('-')
    altura = float(saida[1])
    nome = saida[0]
    dados = (nome, altura)
    soma = soma + altura

    if altura > alturaAlto:
        alturaAlto = altura
        nomeAlto = nome
    
    lista.append(dados)

arquivo.close()
print(lista)

print("Media: ", soma/len(lista))
print("Nome do mais alto: ", nomeAlto)