while True:
    nome = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {nome} jogou: '))

    jogador = {
        'nome': nome,
        'partidas': partidas,
        'gols': [],
        'total': 0,

    }
    for i in range(partidas):
        jogador["gols"].append(int(input(f'Quantos pontos {nome} marcou: ')))
        jogador["total"] += 1
    continuar = input('Deseja continuar?: ').lower()
    if continuar in ['n']:
        break
    print(f'cod      nome                          gols                          total')
for i in range(partidas):
    print(
        f'{i} {jogador["nome"]}              {jogador["gols"]}      {jogador["total"]}')
