def leia(q):
    numero = input(q)
    while not numero.isnumeric() and not isinstance(numero, int):

        print(f'Digite um número!')

        numero = input(q)
        
    print(f'Você acabou de digitar o número {numero}')


q = leia('Digite um número: ')
