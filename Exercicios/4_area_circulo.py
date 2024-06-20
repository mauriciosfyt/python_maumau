#Autor: Maumau
# Data: 28/05/2024
# Versão: 1.0
# Descrição: fassa o algoritimo que receba o raio de um 
#            circulo e apresente a sua área 
#            -------------------------------------------
#            exemblo de execução :
#            Insira o raio em metors : 5
#            área do circulo : 78.5m^2
#            a = área
#            pi = 3.14
#            r = raio 
#            a = pi*(r^2)
#===================================================================
#variaveis
r = 0#raio
a = 0#área
pi = 3.14 #contante pi
#entrada
r = float (input('Insira o raio do círculo em metros: '))

#processamento 
a = pi*(r**2)
#saida
print('a áreado circulo é', a, 'm^2')
#===================================================================
