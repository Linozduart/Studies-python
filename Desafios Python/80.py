lista = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos,valor)
                break
            pos+= 1
print(lista)













# import bisect

# lista = []

# for _ in range(5):
#     valor = int(input('Digite um valor: '))
#     bisect.insort(lista, valor)

# print(lista)