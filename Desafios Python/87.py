
primeira_linha = []
segunda_linha = []
terceira_linha = []
soma_pairs = 0
soma_terceira = 0

for controle in range(9):
    print(controle)
    if controle < 3:
        number = int(input(f'Digite um valor para a primeira linha: '))
        if number % 2 == 0:
            soma_pairs += number
        primeira_linha.append(number)
    elif controle == 3 or controle > 3 and controle < 6:
        number = int(input(f'Digite um valor para a segunda linha: '))
        if number % 2 == 0:
            soma_pairs += number
        segunda_linha.append(number)
    else:
        number = int(input(f'Digite um valor para a terceira linha: '))
        soma_terceira += number
        if number % 2 == 0:
            soma_terceira += number
        terceira_linha.append(number)

print('-='*10)
for linha in [primeira_linha, segunda_linha, terceira_linha]:
    for elemento in linha:
        print(elemento, end=' ')
    print()
print('-='*10)
print(f'A soma de todos os numero pares é: {soma_pairs}')
print(f'A soma da terceira coluna é: {soma_terceira}')
print(f'O maior valor da segunda linha {max(segunda_linha)}')
