lista = []
for control in range(5):
    lista.append(int(input('Digite um numero: ')))
print(f'o menor valor é {min(lista)} e está na posição {lista.index(min(lista))+1}')
print(f'o maior valor é {max(lista)} e está na posição {lista.index(max(lista))+1}')
