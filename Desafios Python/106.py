import colorama
from colorama import Fore, Style
import os
from time import sleep


def ajuda(comando):
    help(comando)

while True:
    comando = input('Digite o comando ou biblioteca que deseja saber informações (ou "fim" para sair): ')
    if comando in ['fim', 'FIM']:
        break
    print(Fore.YELLOW + f'-' * 30)
    print(f'  AJUDA PARA O COMANDO "{comando.upper()}":')
    ajuda(comando)
    print(Style.RESET_ALL)

sleep(8)

os.system('cls' if os.name == 'nt' else 'clear')