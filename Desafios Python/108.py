import os
from time import sleep
import moeda

p = float(input('Digite o preço: R$'))

print(f'O preço reduzido é {moeda.formatacao(moeda.diminuir(p,15))}')
print(f'O preço aumentado é {moeda.formatacao(moeda.aumentar(p,15))}')
print(f'O dobro do preço é {moeda.formatacao(moeda.dobro(p))}')
print(f'A metade do preço é {moeda.formatacao(moeda.metade(p))}')


sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')