# def fatorial(numero):
#     resultado = 1
#     i = 1
#     while i <= numero:
#         resultado *= i
#         i += 1
#     return resultado
# print(fatorial(int(input('Digite um número: '))))

numero = int(input('Digite um numero: '))
c = numero
i = 1

while c > 0:
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    i *= c
    c -= 1
print(f'O fatorial de {numero} = {i}')
