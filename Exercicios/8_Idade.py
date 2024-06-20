#Autor: maumau
# Data: 04/06/2024
# Versão: 1.0
# Descrição: Escreva um programa que leia de um individuo e escreva a faixa etária a que pertence, de acordo com a tabela abaixo:
#       Faixa etária              Classificação 
#            <12                     Criança
#          13 - 17                 Adolescente
#          18 - 59                   Adulto
#            >59                      Idoso

#======================================================================================================

# Variáveis

idade = ''

# Entrada

idade = int(input("Digite qual é a sua idade: "))
# Processamento

if idade >= 1 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
elif idade > 59 and idade <= 70:
    print('Adulto Plus')
else:
    print('Idade Inválida!')

# Saída