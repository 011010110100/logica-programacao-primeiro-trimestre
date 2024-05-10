# S02-A02

# A variável guarda o dado na memória!
# Tipos possíveis: int, float, str, bool

# variavel = expressao ou CONSTANTE = expressao


# Queremos um algoritmo para trocar os valores entre 'valor' e 'num'

valor = 100
num = 200
print("Inicialmente temos que valor: " + str(valor))
print("Inicialmente temos que num: " + str(num))

auxiliar = valor

valor = num
num = auxiliar

print("******* APÓS O ALGORITMO *******")
print("Agora o valor vale: " + str(valor))  # 200
print("Agora o num vale: " + str(num))      # 100
