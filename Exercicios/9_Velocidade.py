#Autor: maumau
# Data: 04/06/2024
# Versão: 1.0
# Descrição: Escreva um programa que leia a velocidade máxima permitida em uma avenida  e velocidade
#            com que o motorista estava dirigindo nela e calcule a multa que uma pessoa vai receber
# 
#           Velocidade ultrapassada              Valor da Multa 
#               Até 10 Km/h                         R$ 50,00
#              11 a 30 Km/h                         R$ 100,00
#              Mais 31 Km/h                         R$ 200,00


#======================================================================================================

# Entrada de dados

velocidade_maxima = float(input("Digite a velocidade máxima permitida (em km/h): "))
velocidade_motorista = float(input("Digite a velocidade do motorista (em km/h): "))

# Cálculo da diferença de velocidade

diferenca_velocidade = velocidade_motorista - velocidade_maxima

# Verificação e cálculo da multa

if diferenca_velocidade <= 0:
    print("Motorista dentro do limite de velocidade. Sem multa.")
elif diferenca_velocidade <= 10:
    multa = 50.00
    print(f"Multa de R${multa:.2f} por excesso de velocidade.")
elif diferenca_velocidade <= 30:
    multa = 100.00
    print(f"Multa de R${multa:.2f} por excesso de velocidade.")
else:
    multa = 200.00
    print(f"Multa de R${multa:.2f} por excesso de velocidade.")

# Observação: Os valores das multas podem variar conforme a legislação local.
