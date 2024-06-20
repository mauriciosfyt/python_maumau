#Autor: maumau
# Data: 04/06/2024
# Versão: 1.0
# Descrição: faça um programa que o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que:
#               Salário < R$ 1000,00 aumento 25%
#               Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%
#               Salário >= R$ 2000,00 aumento de 10%
#======================================================================================================

# Variáveis

salario = 0

# Entrada

salario = float(input('Insira o valor do seu salário: '))

# Processamento

if salario < 1000.00:
    print(round(salario * 1.25))
elif salario >= 1000.00 and salario < 2000.00:
    print(round(salario * 1.15))
elif salario >= 2000.00:
    print(round(salario * 1.10))
else:
    print('Valor Inválido')

# Saída

#======================================================================================================