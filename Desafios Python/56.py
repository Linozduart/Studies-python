qnt_pessoas = int(input('Quantas pessoas são: ?'))
soma = 0
pessoas = []
mais_velha = None
muie_vinte = 0
for x in range(qnt_pessoas):
    print(f'-----{x} Pessoa -----')
    pessoa = {
        'nome': input('Qual seu nome?: ').strip(),
        'sexo': input('Qual seu sexo [M/F]?: ').upper(),
        'idade': int(input('Qual sua idade?: '))
    }
    pessoas.append(pessoa)
    soma += pessoa['idade']


print(f'A media das idades é {soma / qnt_pessoas}')


for pessoa in pessoas:
    if mais_velha == None or pessoa['idade'] > mais_velha['idade']:
        if pessoa['sexo'] == 'M':
            mais_velha = pessoa
        else:
            pass
    else:
        pass
print(f'O homem mais velho é: {mais_velha["nome"]}')


for pessoa in pessoas:
    if pessoa['sexo'] == 'F' and pessoa['idade'] >= 20:
        muie_vinte += 1
    else:
        pass
print(f'Tem {muie_vinte} mulheres mais velhas que 20 anos')


