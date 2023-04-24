palavras = ('python','curso','video','exercicio')
for controle in palavras:
    print(f'\n{controle.upper()} tem ',end ='')
    for letra in controle:
        if letra.lower() in ['a','e','i','o','u']:
            print(letra,end=' ')
