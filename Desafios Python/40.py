
nota1 = float(input('Digite a nota do aluno'))
nota2 = float(input('Digite a nota do aluno'))

if (nota1+nota2) / 2 <= 5.0:
    print('REPROVADO')
elif (nota1+nota2) / 2 >= 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')