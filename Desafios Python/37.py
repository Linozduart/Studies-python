num = int(input('Digite um número interio: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para binario é {bin(num)}')
elif opção == 2:
    print(f'{num} convertido para binario é {oct(num)}')
else:
    print(f'{num} convertido para binario é {hex(num)}')
