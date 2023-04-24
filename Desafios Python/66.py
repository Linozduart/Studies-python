contador = 0
soma = 0
while True:
    contador += 1
    numero = int(input('Digite um número: '))
    if numero == 999:
        print(f'Foram digitados {contador}  numeros.')
        print(f'A soma dos numeros digitados é {soma}')
        break
    soma += numero
