try:
    quantidade_alunos = int(input('Quantos alunos serão registrados?: '))
except:
    print('Digite um número')
    quantidade_alunos = int(input('Quantos alunos serão registrados?: '))

alunos = []
while True:
    aluno = {
        'Nome': input('Digite o nome do aluno: '),
        'Nota1': float(input('Digite a nota do aluno: ')),
        'Nota2': float(input('Digite a nota do aluno: '))
    }
    alunos.append(aluno)
    conti = input('Deseja registrar mais? (s/n): ')
    if conti == 'n':
        break
print('-'*15)
for aluno in alunos:
    print(f'0 {aluno["Nome"]} sua média foi {aluno["Nota1"]/aluno["Nota2"]:.2f}')
