while True:
    numero = int(input('Quer ver a tabuada de qual valor?: '))
    if numero == -numero:
        break
    print('-'*18)
    for controle in range(10):
        print(f'{numero} X {controle} = {numero*controle}')
    print('-'*18)

