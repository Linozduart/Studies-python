def aumentar(preco, porcentagem):
    aumentando = preco + preco/100 * porcentagem
    return aumentando


def diminuir(preco, porcentagem):
    reduzido = preco - preco/100 * porcentagem
    return reduzido


def dobro(preco):
    return preco*2


def metade(preco):
    return preco/2

def formatacao(preco):
   return f'R${preco:.2f}'.replace('.',',')

