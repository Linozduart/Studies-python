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
    woman = []
    medialist = []
    for user in users:
        soma += user["idade"]
        if user["sexo"] == 'f':
            woman.append(user)
        if user["idade"] > soma/len(users):
            medialist.append(user)
    print(f'A média de idades é {soma/len(users)}')
    print(f'Mulheres cadastradas: {woman}')
    print(f'Pessoas com idade acima da média: {medialist}')


adicionais()
