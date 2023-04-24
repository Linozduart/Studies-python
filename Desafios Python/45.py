from random import choice

opcao = ['papel', 'pedra', 'tesoura']
player = str(input('Escolha pedra,papel,tesoura: '))
computador = choice(opcao)
m_msgvitoria = 'VITÓRIA'

if player != 'pedra' and player != 'tesoura' and player != 'papel':
    print('Digite sua escolha corretamente')
    exit()

print(computador)

if computador == player:
    print('EMPATE')
elif computador == 'papel' and player == 'tesoura':
    print(m_msgvitoria)
elif computador == 'pedra' and player == 'papel':
    print(m_msgvitoria)
elif computador == 'tesoura' and player == 'pedra':
    print(m_msgvitoria)
else:
    print('Derrota')
