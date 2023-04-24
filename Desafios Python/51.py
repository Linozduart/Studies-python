# a1 = 1
# a2 = a1 + razao
# a3 = a2 + razao
# termo = 0
# razao = 3
# for x in range(10):
#     termo += razao
#     print(termo)
#  for x in range(1,10,3):
#     termo += razao
#     print(termo)


def aritimetica(termo, razao):
    print(termo)
    for x in range(10):
        termo += razao
        print(termo)


aritimetica(4, 3)
