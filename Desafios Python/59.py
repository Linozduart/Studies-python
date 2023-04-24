while True:
    n1 = float(input('Digite um número?: '))
    n2 = float(input('Digite um número?: '))
    print("""
    [1] somar
    [2] mutiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    """)
    menu = {
        '1': f'A soma é {n1 + n2}',
        '2': f'A mutiplicação é {n1 * n2}',
        '3': f'O maior é {n1 if n1 > n2 else n2}',
        '4': ''
    }
    opcao = input('Digite sua opção: ')
    if opcao == '5':
        exit()
    else:
        print(menu[opcao])
    

   