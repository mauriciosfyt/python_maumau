'''
faça um programa que calcule minha idade pelo mes dia e ano em que naci
'''
from datetime import datetime

dia_nascimento = int(input("Digite o dia do seu nascimento: "))
mes_nascimento = int(input("Digite o mês do seu nascimento: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
data_atual = datetime.now()

idade = data_atual.year - data_nascimento.year

if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
    idade -= 1

print("Você tem " + str(idade) + " anos.")



