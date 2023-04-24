listagem = ('lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.90
            )
for controle in range(len(listagem)):
    print(f'{listagem[controle]}: R${listagem[controle + 1]}')

