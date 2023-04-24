casa_val = float(input('Qual o valor da casa ?: '))
salario = float(input('Qual o salario do comprador ?: '))
tempo = int(input('Quanto anos será pago ?: '))
prestações = tempo * 12 
valor_mensal= casa_val/prestações 



if valor_mensal <= salario * 0.30:
    print(f'emprestimo aprovado : Serão {prestações} prestações cada uma custando {valor_mensal:.2f}') 
else:
    print('Emprestimo negado')

























# print('\033[;30;41m olaaa')
# \033[0;30;40
# style = 0 , 1 , 4 ,7
# text = 30, 31, 32, 33, 34, 35, 36, 37
# back = 40, 41, 42, 43, 44, 45, 46, 47
