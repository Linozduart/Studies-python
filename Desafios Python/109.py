import os
from time import sleep
from moeda import *

p = float(input('Digite o preço: R$'))

print(f'O preço reduzido é {diminuir(p,15,True)}')
print(f'O preço aumentado é {aumentar(p,15,True)}')
print(f'O dobro do preço é {dobro(p,True)}')
print(f'A metade do preço é {metade(p,True)}')


sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')
