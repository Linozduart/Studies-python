def ficha(jogador='Desconhecido',gols=0):
    if jogador == '':
        jogador = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gols = (input('Quantidade de gols marcados: '))

ficha(nome,gols)

