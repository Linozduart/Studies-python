r1 = int(input('digite o tamanho do lado do triangulo: '))
r2 = int(input('digite o tamanho do lado do triangulo: '))
r3 = int(input('digite o tamanho do lado do triangulo: '))

if r1 + r2 > r3 and r3 + r2 > r1 and r1 + r3 > r2:
    print('é possível formar esse tringualo')
    if r1 == r2 == r3:
        print('Esse é um triangulo equilatero')
    elif r1 == r2 and r1 != r3 and r2 !=r3:
        print('Esse triangulo é isoceles')
    else:
        print('Esse traingulo é escaleno')
else:
    print('nao é possivel formar esse triangulo')
