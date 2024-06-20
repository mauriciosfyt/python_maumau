#Autor: maumau
# Data: 11/06/2024
# Versão: 1.0
# Descrição: Faça um programa que receba duas notas de seis alunos.
#            Calcule e mostre:
#            - A média aritmética das duas notas de cada aluno; e
#            - A mensagem que está na tabela a seguir:
#                Média Aritmética  Mensagem
#                Até 3             Reprovado 
#                Entre 3 e 7       Exame
#                De 7 para cima    Aprovado
#
#            - O total de alunos aprovados;
#            - O total de alunos de exame;
#            - O total de alunos reprovados;
#            - A média da classe.

'''
total_alunos = 6
aprovados = 0
exame = 0
reprovados = 0
soma_medias = 0

for i in range(total_alunos):
    print(f"Aluno {i+1}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    soma_medias += media
    
    if media < 3:
        print("Reprovado")
        reprovados += 1
    elif 3 <= media < 7:
        print("Exame")
        exame += 1
    else:
        print("Aprovado")
        aprovados += 1

media_classe = soma_medias / total_alunos

print("\nResultados:")
print("Total de alunos aprovados:",aprovados)
print("Total de alunos de exame:",exame)
print("Total de alunos reprovados:",reprovados)
print("Média da classe:" ,media_classe )

'''
#Usando while
# Inicializando as variáveis
total_alunos = 6
aprovados = 0
exame = 0
reprovados = 0
soma_notas = 0
i = 0

while i < total_alunos:
    # Recebendo as notas
    nota1 = float(input("Digite a primeira nota do aluno " + str(i+1) + ": "))
    nota2 = float(input("Digite a segunda nota do aluno " + str(i+1) + ": "))
    
    # Calculando a média
    media = (nota1 + nota2) / 2
    soma_notas += media
    
    # Verificando a situação do aluno
    if media >= 8:
        print("Aprovado")
        aprovados += 1
    elif 4 <= media < 8:
        print("Exame")
        exame += 1
    else:
        print("Reprovado")
        reprovados += 1

    i += 1

# Calculando a média da classe
media_classe = soma_notas / total_alunos

# Mostrando os resultados
print("Total de alunos aprovados: " , aprovados)
print("Total de alunos de exame: " , exame)
print("Total de alunos reprovados: " , reprovados)
print("Média da classe: " , media_classe)