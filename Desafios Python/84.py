pessoas = []
pessoa_pesada = {'Nome': '', 'Peso': 0}
pessoa_leve = {'Nome': '', 'Peso': 0}
soma_idades = 0

for control in range(5):
    pessoa = {
        'Nome': input('Qual é o seu nome?: '),
        'Idade': int(input('Qual é a sua idade?: ')),
        'Peso': float(input('Qual é o seu peso?: '))
    }
    print(f'PESSOA {control+1} FOI REGISTRADA')
    soma_idades = pessoa['Idade']
    pessoas.append(pessoa)
    if pessoa['Peso'] > pessoa_pesada['Peso']:
        pessoa_pesada = pessoa
    else:
        pessoa_leve = pessoa
print(f'Foram registradas {len(pessoas)} pessoas')
print(
    f'{pessoa_pesada["Nome"]} é a pessoa mais pesada, com {pessoa_pesada["Peso"]} kg.')
print(
    f'{pessoa_leve["Nome"]} é a pessoa mais leve, com {pessoa_leve["Peso"]} kg')
print(f'A soma das idades de todas as pessoas é {soma_idades}')
