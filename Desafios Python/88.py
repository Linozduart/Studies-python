from random import randint

vezes = int(input('Digite quantas vezes deseja: '))

resultados = []  # lista vazia para armazenar os números sorteados

for i in range(vezes):
    numeros = []  # lista vazia para armazenar os números de cada sorteio
    for j in range(6):
        numeros.append(randint(1, 60))
    resultados.append(numeros)  # adiciona a lista de números sorteados na lista principal

print(f'Jogo 1:{resultados[0]}')
print(f'Jogo 2:{resultados[1]}')
print(f'Jogo 3:{resultados[2]}')
print(f'Jogo 4:{resultados[3]}')