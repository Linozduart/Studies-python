
def leia(q):
    numero = input(q)
    while not numero.isnumeric():
        print(f'\033[31mDigite um número!')
        numero = input(q)
    print(f'Você acabou de digitar o número {numero}')


q = leia('Digite um número: ')
