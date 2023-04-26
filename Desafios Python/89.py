try:
    quantidade_alunos = int(input('Quantos alunos serão registrados?: '))
except:
    print('Digite um número')
    quantidade_alunos = int(input('Quantos alunos serão registrados?: '))

alunos = []
for i in range(quantidade_alunos):
    aluno = {
        'Nome': input('Digite o nome do aluno: '),
        'Nota1': int(input('Digite a nota do aluno: ')),
        'Nota2': int(input('Digite a nota do aluno: '))
    }
    alunos.append(aluno)
    conti = input('Deseja registrar mais? (s/n): ')
    if conti == 'n':
        break
print('-'*15)
print()