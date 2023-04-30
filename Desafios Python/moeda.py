def aumentar(preco, porcentagem, format=False):
    aumentado = preco + preco/100 * porcentagem
    if format == True:
        return f'R${aumentado:.2f}'
    else:
        return aumentado


def diminuir(preco, porcentagem, format=False):
    reduzido = preco - preco/100 * porcentagem
    if format == True:
        return f'R${reduzido:.2f}'
    else:
        return reduzido


def dobro(preco, format=False):
    if format == True:
        return f'R${preco*2:.2f}'
    else:
        return preco*2


def metade(preco, format=False):
    if format == True:
        return f'R${preco/2:.2f}'
    else:
        return preco/2


def formatacao(preco):
    return f'R${preco:.2f}'.replace('.', ',')


def resumo(preco,porcent_aumento,porcent_diminuicao):

    print(f'Preço analisado:        {formatacao(preco)}')
    print(f'Dobro do preço          {(dobro(preco,True))}')
    print(f'Metade do preço:        {(metade(preco,True))}')
    print(f'{porcent_aumento}% de aumento:         {(aumentar(preco,porcent_aumento,True))}')
    print(f'{porcent_diminuicao}% de reducao:          {(aumentar(preco,porcent_diminuicao,True))}')

    

