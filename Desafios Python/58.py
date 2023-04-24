from random import randint
num = randint(0, 10)
print(num)
chute = None
palpites = 0
while chute != num:
    palpites += 1
    chute = int(input('Tente adivinhas o número de um a 10: '))
    if chute == num:
        print('Voce acertou')
        print(f'Foram necessarios {palpites} palpites')
        break
    else:
        pass
