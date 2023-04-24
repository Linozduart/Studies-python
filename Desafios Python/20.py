import random
a1 = str(input('Digite qual primeiro aluno ?'))
a2 = str(input('Digite qual segundo aluno?'))
a3 = str(input('Digite qual terceiro aluno?'))
a4 = str(input('Digite qual quarto aluno ?'))
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
print(alunos)
