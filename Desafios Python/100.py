from random import randint

lista = []
lista_par = []

def sorteia():
    for i in range(5):
        lista.append(randint(1,20))
    print(f'Sorteado 5 valores: {lista}')
    
def somaPar():
    
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
    print(f'Somando os valores pares de {lista_par}: {sum(lista_par)}')

sorteia()
somaPar()
