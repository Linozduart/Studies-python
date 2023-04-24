number = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
user = int(input('Enter a number between 0 to 20: '))
while True:
    if user > 20:
        print('between 0 and 20,please')
        user = int(input('Enter a number between 0 to 20: '))
    else:
        break
print(f'The chosen number in words is {number[user]}')
