while True:
    try:
        quantidade_alunos = int(input('Quantos alunos serão registrados?: '))
        break
    except ValueError:
        print('Digite um número válido')

alunos = []
for i in range(quantidade_alunos):
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    while True:
        try:
            nota1 = float(input(f'Digite a primeira nota de {nome}: '))
            nota2 = float(input(f'Digite a segunda nota de {nome}: '))
            break
        except ValueError:
            print('Digite uma nota válida')

    alunos.append({
        'Nome': nome,
        'Nota1': nota1,
        'Nota2': nota2
    })

print('-'*30)
print('LISTA DE ALUNOS')
print('-'*30)

for i, aluno in enumerate(alunos):
    media = aluno['Nota1'] / aluno['Nota2']
    print(f'{i+1} - {aluno["Nome"]}: média {media:.2f}')

print('-'*30)

while True:
    escolha = input(
        'Deseja ver as notas de algum aluno individualmente? (s/n): ').lower()[0]
    if escolha not in ['s', 'n']:
        print('Opção inválida')
    elif escolha == 's':
        nome_aluno = input('Digite o nome do aluno: ')
        for aluno in alunos:
            if aluno['Nome'] == nome_aluno:
                media = aluno['Nota1'] / aluno['Nota2']
                print(
                    f'Notas de {aluno["Nome"]}: {aluno["Nota1"]} e {aluno["Nota2"]}')
                print(f'Média: {media:.2f}')
                break
        else:
            print(f'O aluno {nome_aluno} não foi encontrado')
    else:
        break
