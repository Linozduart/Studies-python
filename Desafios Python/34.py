sal = float(input('qual salario do funcionario>: '))

if sal > 1250:
    print(f'O aumento será de 10% ficando assim {sal + (sal*0.10)}')
else:
    print(f'O aumento sera de 15% ficando assim {sal + (sal*0.15)}')
