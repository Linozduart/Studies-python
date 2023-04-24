vel = int(input('Velocidade do carro'))

if vel < 80:
    print(f'Voce está entre os limites de velocidade,{vel}km/h')
else:
    muta = (vel - 80) * 7
    print(f'Voce está acima do limite')
    print(f'Voce foi multado em R${muta}')
