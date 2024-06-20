#================================================================================================

# Autor: Maumau
# Data: 24/05/2024
# Versão: 1.0
# Descrição: Faça um algoritmo que um valor na moeda real (R$),
#            a cotação da conversão REAL para DÓLAR, e apresente
#            a quantidade desse valor em dólar ($)
#            ----------------------------------------------------
#            Exemplo de execução
#            Insira o valor em real: 5000
#            Insira cotação do dia: 5.00
#            R$ 5000.00 equivalem $ 1000.00
#            ----------------------------------------------------

#================================================================================================

# Entrada

real = int(input('Digite o valor em reais(R$): '))
cotacao = float(input('Digite o valor da cotação: '))

# Processamento 

dolar = real / cotacao

# Saída 

print('O valor em dolar é: ', dolar, '$')