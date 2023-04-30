from time import sleep


info = []
def cadastrar():

    info.append({

        'nome': input('Digite o nome do usuário: '),
        'idade': int(input('Digite sua idade: '))
    })


def ver(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        print('Erro ao ler o arquivo')
        print(a.readlines())
    else:
        print('Pessoas cadastradas')
        print(a.read())




def menu():
    print('-'*30)
    print('       MENU PRINCIPAL')
    print('-'*30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema')
    print('-'*30)

    while True:

        opcao = input('Sua opção: ')

        try:
            menu_opcao = int(opcao)
        except ValueError:
            print('Digite apenas números inteiros!')
            sleep(0.2)
            continue

        if menu_opcao == 1:
            print('-'*30)
            ver('dados.txt')
            
        elif menu_opcao == 2:
            print('-'*30)
            infos = cadastrar()
            print(menu())

        elif menu_opcao == 3:
            print('Fim do programa')
            exit()
        
        else:
            print('Erro')
        sleep(1)

def arquivoexistence(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')
   