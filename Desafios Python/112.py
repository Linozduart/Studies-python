import os
from time import sleep
from moeda import *


p = verificar()
print('-' * 30)
print('            Tabela')
print('-' * 30)
resumo(p, 10, 5)
print('-' * 30)

sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')
