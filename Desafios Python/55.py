# def peso():

#     lista = []
#     for x in range(5):
#         lista.append(int(input('Qual sua massa?: ')))
#     lista.sort()
#     return lista[0],lista[-1]


# print(peso())


def peso_dificil():

    maior = 0
    menor = 0

    for controle in range(0, 5, 1):
        massa = int(input('Qual sua massa?: '))
        if controle == 0:
            maior = massa
            menor = massa
        else:
            if massa > maior:
                maior = massa
            else:
                if massa < menor:
                    menor = massa
                else:
                    pass
    return maior, menor


peso = peso_dificil()
print(f'A maior massa é {peso[0]} e a menor é {peso[1]}')
