from random import randint

def analisar(*num):
    count = maior = count_par = 0

    print('Analisando os valores passados.....')
    for valor in num:
        print(valor, end=' ')
        count += 1
        if valor > maior:
            maior = valor
        if valor % 2 == 0:
            count_par += 1
    print(f'\nForam informados {count} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print(f'{count_par} números são pares.')

analisar(2, 3, 41, 2, 4, 2, 1, 2, 2)
