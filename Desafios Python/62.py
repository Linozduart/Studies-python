from time import sleep


def aritimetica(termo, razao):
    print(termo)
    for controle in range(10):
        termo += razao
        sleep(0.2)
        print(termo)
    desejo = input('Deseja que mostre mais alguns números?: ').lower()[0]
    while desejo not in ['s', 'n']:
        desejo = input('Deseja que mostre mais alguns números?: ').lower()[0]
        print('Digite sim ou nao')

    if desejo == 's':
        for controle in range(10):
            termo += razao
            sleep(0.2)
            print(termo)
    else:
        exit()


aritimetica(4, 3)

# if desejo == 'sim':
#                 for controle in range(10):
#                     termo += razao
#                     sleep(0.4)
#                     print(termo)
#             elif desejo == 'nao':
#                    exit()
#             else:
#                 print('Digite sim ou nao')
#         else:
#             pass
