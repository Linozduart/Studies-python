
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

print('=-'*10)
print(jogador)
print('=-'*10)
print(f'O campo nome tem o valor {nome}')
print(f'O campo gols tem o valor {jogador["gols"]}')
print(f'O campo total tem o valor {jogador["total"]}')
print('-='*10)
print(f'O jogador {nome} jogou {partidas}')
for i in range(partidas):
    print(f'Na partida {i+1}, fez {jogador["gols"][i]}')
print(f'Total de gols foi de {jogador["total"]}')
