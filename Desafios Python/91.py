from random import randint
from time import sleep
from os import system, name


jogadores = {}

system('clear') if name == 'posix' else system('cls')

for i in range(1, 5):
    dado = randint(1, 6)
    jogadores[i] = {
        'jogador': i, 'dado': dado
    }

    print(f'O jogador {i} tirou {dado}')
    sleep(0.5)

print('-'*30)

print('Ranking dos Jogadores:')

jogadores = sorted(
    jogadores.values(),
    key=lambda jogador: jogador['dado'],
    reverse=True)
for i, jogador in enumerate(jogadores):
    print(f'{i+1}º lugar: Jogador {jogador["jogador"]} com {jogador["dado"]}')

