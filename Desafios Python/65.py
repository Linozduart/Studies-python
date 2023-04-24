x = 0
soma = 0
lista = []
while x != 10:
    x += 1
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except:
            print('Digite corretamente')
    lista.append(numero)
    soma += numero
    if x == 10:
        print(f'A media dos números que voce digitou é {soma/x}')
        print(
            f'O maior numero digitado foi {min(lista)} e o menor for {max(lista)}')
        desejo = input('Deseja continuar com mais números? ').lower()[0]
        while desejo not in ['s', 'n']:
            print('Digite sim ou nao')
            desejo = input('Deseja continuar com mais números? ').lower()[0]
        if desejo == 's':
            x = 0
        else:
            exit()
    else:
        pass
