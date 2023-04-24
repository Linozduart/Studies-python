sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Qual seu sexo:? ').upper()
    if sexo == 'M' or sexo == 'F':
        print('Digitaçao correta')
    else:
        print('Digitaçao incorreta')
