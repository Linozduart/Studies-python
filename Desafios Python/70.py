preco_total = 0
qnts_mil = 0
mais_barato = float('inf')
nome_barato = ''
print('Lojaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
while True:
    nome = input('Nome do Produto: ')
    preco = int(input('Preço do Produto: '))
    if preco < mais_barato:
        mais_barato = preco
        nome_barato = nome
    if preco >= 1000:
        qnts_mil += 1
    preco_total += preco
    escolha = input('Quer continuar? [S/N]').lower()
    while escolha not in ['s','n']:
        print('Escolha sim ou nao')
        escolha = input('Quer continuar? [S/N]').lower()
    if escolha == 'n':
        print(f'O total da compra foi R${preco_total:.2f}')
        print(f'Temos {qnts_mil} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato}')
        break

