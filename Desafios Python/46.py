from time import sleep


def foguete(n_foguete):

    for n in range(10, 0, -1):
        print(n)
        sleep(0.5)
    if n_foguete % 2 == 0:
        print(f'Fim.O foguete {n_foguete} foi lançado')
    else:
        print(f'Fim.O foguete {n_foguete} falhou')


for n in range(5):
    foguete(n+1)
