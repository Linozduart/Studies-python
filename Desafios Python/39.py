from datetime import date
atual = date.today().year
nasc = int(input('Insira o ano de nascimento'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
    print('Voce deve se alistar')
elif idade < 18:
    print('Voce não tem idade ainda')
else:
    print(f'Voce deveria ter se alistado há {idade - 18}')