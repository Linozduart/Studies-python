lista = []
pessoa_18 = mulheres_20 = homens = 0
while True:

    pessoas = {
        'idade': int(input('Qual sua idade?: ')),
        'sexo': input('Qual seu genero [M/F]').lower()[0]
    }
    lista.append(pessoas)
    descisao = input('Voce deseja registrar mais ?: ')
    if descisao == 'nao':
        for controle in lista:
            if pessoas['idade'] >= 18:
                pessoa_18 += 1
            if pessoas['idade'] < 20 and pessoas['sexo'] == 'f':
                mulheres_20 += 1
            if pessoas['sexo'] == 'm':
                homens += 1
        break
print(f'Há {pessoa_18} pessoas com mais de 18 anos')
print(f'Há {homens} homens foram cadastrados')
print(f'{mulheres_20} mulheres tem menos de 20 anos')