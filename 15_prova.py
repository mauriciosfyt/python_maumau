'''
Algoritmo "Tabuada"
Descrição: Faça um programa que receba dois valores, sendo que o
           primeiro deve ser menor que dois segundo.
           o programa deve ser apresentar todos os número impares
           contiduos nesta seguencia.
           (modulo% exemblo:7%2 =1)

'''
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
for numero in range(num1, num2):
    if numero % 2 != 0:
        print(numero)