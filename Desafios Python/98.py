from time import sleep

def contador(i, f, p):
    print(f'contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    for j in range(i, f, p):
        sleep(0.3)
        print(j, end=', ', flush=True)
    print('\n')  # adiciona uma nova linha após a contagem

contador(0, 21, 2)
contador(20, 1, -2)
