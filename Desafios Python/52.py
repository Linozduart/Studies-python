n = int(input('Digite um número: '))

if n > 1:

    if n == 2:
        print('é primo')
    elif n % 2 == 0:
        print('não é primo')
    else:
        print('é primo')
        
else:
    print('não é primo')
