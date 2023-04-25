
primeira_linha = []
segunda_linha = []
terceira_linha = []

for controle in range(9):
    print(controle)
    if controle < 3:
        number = int(input(f'Digite um valor para a primeira linha: '))
        primeira_linha.append(number)
    elif controle == 3 or controle > 3 and controle < 6:
        number = int(input(f'Digite um valor para a segunda linha: '))
        segunda_linha.append(number)
    else:
        number = int(input(f'Digite um valor para a terceira linha: '))
        terceira_linha.append(number)

print('-='*10)
for linha in [primeira_linha, segunda_linha, terceira_linha]:
    for elemento in linha:
        print(elemento, end=' ')
    print()
print('-='*10)
