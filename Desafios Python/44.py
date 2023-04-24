produto = float(input('Qual preço do produto?: '))
print('''Escolha uma das bases para conversão:
[ 1 ] À vista/cheque:10% , de desconto cartão
[ 2 ] À vista no cartão: 5% , de desconto
[ 3 ] em até 2x no cartão preço normal
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Digite o metodo de pagamento: '))
if opção == 1:
    print(f'Você pagará R${(produto / 100 * 10) + produto}')
elif opção == 2:
     print(f'Você pagará R${(produto / 100 * 5) + produto}')
elif opção == 3:
      print(f'Você pagará R${produto} ')
else:
     print(f'Você pagará R${(produto / 100 * 10) + produto}')


