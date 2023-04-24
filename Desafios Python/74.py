from random import choices,randint 
# tupla = tuple(random.choices(range(1,51), k=5))
lista = []
for x in range(1,6):
    lista.append(randint(0,51))
tuplinha = tuple(lista)
print(tuplinha)
lista.sort()
tuplinha_ordenada = lista
ordem = tuple(tuplinha_ordenada)
print(f'O menor é {ordem[0]} o maior é {ordem[-1]} ')


