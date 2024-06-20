'''
Algoritmo "Tabuada"
Descrição: Faça um programa que exibe a tabuada de um número digitado
            pelo usuário.
'''

# Solicita ao usuário que digite um número
numero = int(input('Digite o valor da tabuada: '))

# Exibe a tabuada do número digitado
print(f'Tabuada do {numero}:')
for i in range(11):
    print(f'{numero} x {i} = {numero * i}')