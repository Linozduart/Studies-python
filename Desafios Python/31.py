dist = float(input('Qual a distancia da viagem ?: '))

if dist < 200:
    print(f'preço R${dist * 0.50}')
else:
    print(f'preço R${dist * 0.45}')
