#Autor : maumau 
#Data:24/05/2024
#Versão: 1.0
#Descrição:Faça um algoritimo que um vlor na moeda real (R$),
#        a cotação da conversão REAL para SOLAR, e apresente 
#        a quntidade desse valor em dolar ($)
#--------------------------------------------------------
#            Exemblo de execução
#            insira cotação do dia: 5
#            R$5000,00 equivalem $1000,00
#=======================================================
# inicio
taxa_cambio = 5.17

# processamento 
valor_real = float(input("Digite o valor em reais : "))

# Converte o valor para reais
valor_dolar = valor_real  * taxa_cambio

# Imprime o valor convertido
print("O valor em dolar é:", valor_dolar)
