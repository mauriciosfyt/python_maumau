#Autor: maumau
# Data: 04/06/2024
# Versão: 1.0
# Descrição: Estudos do condicional IF ... ELSE
#======================================================================================================

# Variaveis

mes = 0
mes_escolhido = ''

# Entrada

print('Nr. Mês \n 1. Janeiro \n 2. Fevereiro \n 3. Março \n 4. Abril \n 5. Maio \n 6. Junho \n 7. Julho \n 8. Agosto \n 9. Setembro \n 10. Outubro \n 11. Novembro \n 12. Dezembro')
mes = int(input('Insira a opção desejada: '))

# Processamento

if mes == 1:
    mes_escolhido = 'Janeiro'
elif mes == 2:
    mes_escolhido = 'Fevereiro'
elif mes == 3:
    mes_escolhido = 'Março'
elif mes == 4:
    mes_escolhido = 'Abril'
elif mes == 5:
    mes_escolhido = 'Maio'
elif mes == 6:
    mes_escolhido = 'Junho'
elif mes == 7:
    mes_escolhido = 'Julho'
elif mes == 8:
    mes_escolhido = 'Agosto'
elif mes == 9:
    mes_escolhido = 'Setembro'
elif mes == 10:
    mes_escolhido = 'Outubro'
elif mes == 11:
    mes_escolhido = 'Novembro'
elif mes == 12:
    mes_escolhido = 'Dezembro'
else:
    mes_escolhido = 'Opção Inválida'
    
# Saída

print('O mês escolhido foi: ' + mes_escolhido)

#=====================================================================================================