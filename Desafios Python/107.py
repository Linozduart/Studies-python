import os
from time import sleep
import moeda

p = float(input('Digite o preço: R$'))
print(f'O preço reduzido é {moeda.diminuir(p,15)}')
print(f'O preço aumentado é {moeda.aumentar(p,15)}')
print(f'O dobro do preço é {moeda.dobro(p)}')
print(f'A metado do preço é {moeda.metade(p)}')

sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')