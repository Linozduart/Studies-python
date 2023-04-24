contador = 0
advinha = 0
soma = 0
while advinha != 999:

    advinha = int(input('Digite um número: '))
    soma += advinha
    contador += 1

    if advinha < 999:

        print('o numero que voce digitou é menor q o escolhido')

    else:

        print('o numero que voce digitou é maior q o escolhido')

    if advinha == 999:
        print(f'A soma das suas tentativas é {soma}')
        print(f'Foram {contador} tentativas', end=',')
        print('Voce acertou,parabéns!')

    else:
        pass
