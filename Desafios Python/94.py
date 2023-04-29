qnt_user = int(input('Quantas pessoas deseja registrar: '))

users = []

for i in range(qnt_user):

    users.append({
        'nome': input('Qual seu nome: '),
        'sexo': input('Qual seu gênero (M/F): ').lower(),
        'idade': int(input('Qual sua idade ?: '))
    })

print(f'Foram cadastradas {qnt_user} pessoas')


def adicionais():
    soma = 0
    woman = list()
    medialist = list()
    for user in users:
        soma += user["idade"]
    print(f'A média de idades é {soma/len(users)}')
    if user["sexo"] == 'f':
        woman.append(user)
    print(f'{woman}')
    if user["idade"] > soma/len(users):
        medialist.append(user)
adicionais()