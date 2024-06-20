'''
autor: Maumau
data 14/06/2024
versão: 1.0
Descrição:Estudo do tipo de dado array
'''
aluno_a="joão"
aluno_b='maria'
aluno_c='francisco'
aluno_d='sofia'
aluno_e='milton'
aluno_f='joana'
#            =   0    1        2         3        4        5
turma_python =['joaõ',200,'francisco',aluno_d,'milton','joana',]

print(turma_python)
turma_python[1] = 'Maria'
print(turma_python)
print(f'posição 0 vetor turma_python é igual {turma_python[0]}')
print(f'posição 1 vetor turma_python é igual {turma_python[1]}')
print(f'posição 2 vetor turma_python é igual {turma_python[2]}')
print(f'posição 3 vetor turma_python é igual {turma_python[3]}')
print(f'posição 4 vetor turma_python é igual {turma_python[4]}')
print(f'posição 5 vetor turma_python é igual {turma_python[5]}')
#================================================================

alunos_python_noturno = [4,5,3,2,0,1]
print(alunos_python_noturno) #arry velho
alunos_python_noturno [0]='joana'
alunos_python_noturno [1]='milton'
alunos_python_noturno [2]='sofia'
alunos_python_noturno [3]='francisco'
alunos_python_noturno [4]='maria'
alunos_python_noturno [5]='joão'

print(alunos_python_noturno[3])#arry novo