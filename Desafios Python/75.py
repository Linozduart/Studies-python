count = 0
numeros = []
pares = []
while count <= 4:
    count += 1
    numero = int(input('Digite um numero: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        pass

print(f'quantas vezes o nove apareceu: {numeros.count(9)}')
try:
    print(
        f'o primeiro valor 3 foi digitado e está na posição {numeros.index(3)}')
except:
    print('O numero 3 não foi encontrado')
    
print(f"Os numeros pares são: {' , '.join(map(str, pares))}")

