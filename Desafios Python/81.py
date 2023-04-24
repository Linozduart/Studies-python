import random


print('-='*30)
vezes = random.randint(1, 4)
lista = []
for controle in range(vezes):
    valor = int(input('Digite um numero: '))
    lista.append(valor)
print(f'foram digitados {len(lista)} numeros')
lista.sort()
print(list(reversed(lista)))
if 5 in lista:
    print(f'o valor 5 está na lista na posição {lista.index(5)}')
else:
    print('o valor 5 não foi encontrado na lista')
print('-='*30)
