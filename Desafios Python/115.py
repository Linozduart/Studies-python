from modulos115 import *

arq = 'dados.txt'
if arquivoexistence(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)


menu()


