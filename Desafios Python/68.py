from random import randint

vitorias = 0
while True:
    computador = randint(1, 10)
    player_escolha = input('Escolha ímpar ou par (ou digite "sair" para sair do jogo): ')

    if player_escolha == 'sair':
        break

    while player_escolha not in ['impar', 'par']:
        print('Escolha apenas impar ou par')
        player_escolha = input('Escolha ímpar ou par: ')

    if player_escolha in ['impar']:

        player = int(input('Digite um numero: '))

        if (player + computador) % 2 == 0:
            print('Computer wins')
            print(f'Voce conseguiu {vitorias} vitórias')
            break
        else:
            print('Player wins')
            vitorias += 1
            computador = randint(1, 10)
    else:
        player = int(input('Digite um numero: '))
        if (player + computador) % 2 == 0:
            print('Player wins')
            vitorias += 1
            computador = randint(1, 10)
        else:
            print('Computer wins')
            print(f'Voce conseguiu {vitorias} vitórias')
            break