from datetime import date
nasc = int(input('Qual ano voce nasceu ?: '))

idade = (nasc - date.today().year) * -1

if idade <= 9:
    print('Mirim')
elif idade <=14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade == 20:
    print('Sênior')
else:
    print('Master')
