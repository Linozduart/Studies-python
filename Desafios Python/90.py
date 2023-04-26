
nome = input('Qual seu nome?: ')
media = float(input(f'Média do {nome}: '))
aluno = {
    'Nome': nome,
    'Média': media
}
print(f'O(A) aluno(a) {aluno["Nome"]} obteve a média {aluno["Média"]}')