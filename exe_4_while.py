#Autor : maumau 
#Data:06/06/2024
#Versão: 1.0
#Descrição:estudo da estrutura de repetição "while"
#============================================================

indice = 1
while indice <17:
    print(indice)
    indice = indice + 1 # indice +=1

#=============================================================

indice2 =10
while indice2 > 0:
    print(indice2,'maumau')
    indice2 = indice2 - 1

#==============================================================
indice3 = 1
while True:
    print(indice3)
    indice3 = indice3 + 1
    if indice3 == 5:
        break
#==============================================================
indice4 = 1
while True:
    opcao = input('Digite 5 para finalizar o programa:')
    print(opcao)
    print(indice4)
    indice4 = indice4 + 1
    if indice4 == 10:
        break