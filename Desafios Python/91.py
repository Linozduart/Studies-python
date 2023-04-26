from random import randint
from time import sleep

jogadores = {}

print('-'*30)

for i in range(4):
    dado = randint(1, 6)
    jogador = i + 1
    print(f'O jogador {jogador} tirou {dado}')
    jogadores[jogador] = {
        'jogador': jogador,
        'dado': dado
    }
    sleep(0.5)
print('-'*30)

def ranking():
    print('Ranking dos Jogadores:')
    jogadores_ordenados = sorted(jogadores.values(), key=lambda jogador: jogador['dado'], reverse=True)
    for i, jogador in enumerate(jogadores_ordenados):
        posicao = i + 1
        print(f'{posicao}º lugar: Jogador {jogador["jogador"]} com {jogador["dado"]}')
