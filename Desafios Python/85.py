lista = []
lista_pairs = []
lista_odd = []
for control in range(7):
    number = int(input('Enter a number: '))
    lista.append(number)
    if number % 2 == 0:
        lista_pairs.append(control)
    else:
        lista_odd.append(control)

print(f'The even numbers are at positions: {", ".join(map(str,lista_pairs))}')
print(f'The odd numbers are at positions: {", ".join(map(str,lista_odd))}')
