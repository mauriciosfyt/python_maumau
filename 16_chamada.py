'''
Descricao:faça um programa que receba o numero da chamada da dos alunos do curso de pyton no periodo noturno do Senai 115 e apresentado seu nome
'''

# Lista de chamada dos alunos
lista_chamada = [
    'Luana','Gustavo', 'Danielle','Felipe','Joao','Thiago','Aldivan','Jose','Arthur','Pedro','Maumau','Davi',
'Kawan','Andrey','Lucas','Diego','joao','Ana','Vinicius','Adriel','Patrik','Bruno','Professor',
]

# Função para obter o nome do aluno a partir do número da chamada
def obter_nome_aluno(numero_chamada):
    if 1 <= numero_chamada <= len(lista_chamada):
        return lista_chamada[numero_chamada - 1]
    else:
        return "Número de chamada inválido"

# Solicita o número da chamada ao usuário
numero_chamada = int(input("Digite o número da chamada do aluno: "))

# Obtém e exibe o nome do aluno
nome_aluno = obter_nome_aluno(numero_chamada)
print(f"O nome do aluno é: {nome_aluno}")