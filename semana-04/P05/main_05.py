# Exercício de anos bissextos

""" 
Um ano é bissexto se
- for divisível por 4
- mas não por 100, a menos que seja divisível por 400

Casos de teste:

ANO     divisivel por 4?  divisível por 100?   divisível por 400?     CONCLUSAO
------|-----------------|-------------------|----------------------|-----------
2021         falso              falso               falso               FALSO
2000           T                 T                    T              VERDADEIRO
2004           T                falso               falso            VERDADEIRO
1900           T                 T                  falso               FALSO

"""

ano = int(input("Ano: "))

if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto!")
else:
    print("Não é bissexto.")


# Cálcuolo de salário líquido
""" 
Entradas: salário bruto e total de dependentes
Saídas: Desconto no INSS, de IRRF e salário Líquido.

BRUTO                  Alíquota(%)      Parcela a deduzir (R$)    Contribuição (R$) 
---------------------|-----------------|-----------------------|-----------------------
1.212,00                   7,5%                 --                   90,90

1.212,01 - 2.427,35        9%                 18,18                 200,28

2.427,36 - 3.641,03       12%                91,00                 345,92

3.641,04 - 7.087,22        14%                163,82                828,39

---------------------|-----------------|-----------------------|-----------------------

Desconto do IRRF


Base de cálculo          Alíquota(%)       Parcela a deduzir     
---------------------|-----------------|-----------------------
Até 1.903,98                -                 --                  

1.903,99 - 2.826,65        7,5%              142,80          
 
2.826,66 - 3.751,05        15%               354,80           

3.751,06 - 4.664,68        22,5%             636,16

Acima de 4.664,68          27.5%             869,36

---------------------|-----------------|-----------------------


Salário líquido = bruto - INSS - IRRF

"""

bruto = float(input("Salário bruto: "))
dependentes = int(input("Total dependentes: "))

# De acordo com a faixa de salário determina a líquota do INSS e a parcela a deduzir

if bruto < 1212.01:
    al_inss = 0.075
    parcela_deduzir = 0.0
elif bruto <= 2427.35:
    al_inss = 0.09
    parcela_deduzir = 18.18
elif bruto <= 3641.03:
    al_inss = 0.12
    parcela_deduzir = 91
else:
    al_inss = 0.14
    parcela_deduzir = 163.82

inss = bruto * al_inss - parcela_deduzir

if inss > 828.39:
    inss = 828.39 #Nesse caso limita!

print ("INSS: ", inss)

# Base para cálculo do IRRF

base = bruto - inss - 189.59 * dependentes

if base <= 1903.98:
    aliq_irrf = 0.0
    parcela_irrf = 0.0
elif base <= 2826.65:
    aliq_irrf = 0.075
    parcela_irrf = 142.8
elif base <= 3751.05:
    aliq_irrf = 0.15
    parcela_irrf = 354.80
elif base <= 4664.68:
    aliq_irrf = 0.225
    parcela_irrf = 636.16
else:
    aliq_irrf = 0.275
    parcela_irrf = 869.36

irrf = base * aliq_irrf - parcela_irrf

print("Imposto retido na fonte: ", irrf)

liquido = bruto - inss - irrf

print("Salário líquido: ", liquido)