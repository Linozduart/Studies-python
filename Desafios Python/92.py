import datetime


def obter_dados_pessoais():
    """
    Obtém os dados pessoais do usuário e retorna um dicionário com as informações.
    """
    nome = input('Qual é o seu nome? ')
    data_nascimento = input(
        'Digite a data de nascimento no formato dd/mm/aaaa: ')
    clt = input('Você é CLT? (sim ou não) ')
    genero = input('Qual é o seu gênero? (M/F) ').lower()

    # Validação da data de nascimento
    try:
        data_nascimento = datetime.datetime.strptime(
            data_nascimento, '%d/%m/%Y')
    except ValueError:
        print('Data de nascimento inválida')
        return None

    dados_pessoais = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'clt': clt.lower() == 'sim',
        'genero': genero
    }

    return dados_pessoais


def calcular_idade(data_nascimento):
    """
    Calcula a idade a partir da data de nascimento.
    """
    hoje = datetime.datetime.now()
    idade = hoje.year - data_nascimento.year
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade


def obter_dados_clt():
    """
    Obtém informações adicionais do usuário caso ele seja um CLT e retorna um dicionário com essas informações.
    """
    data_contratacao = input(
        'Digite a data de contratação no formato dd/mm/aaaa: ')

    # Validação da data de contratação
    try:
        data_contratacao = datetime.datetime.strptime(
            data_contratacao, '%d/%m/%Y')
    except ValueError:
        print('Data de contratação inválida')
        return None

    salario = input('Qual é o seu salário? ')

    # Conversão do salário para float
    try:
        salario = float(salario)
    except ValueError:
        print('Salário inválido')
        return None

    anos_trabalho = datetime.datetime.now().year - data_contratacao.year

    dados_clt = {
        'data_contratacao': data_contratacao,
        'salario': salario,
        'anos_trabalho': anos_trabalho
    }

    return dados_clt


def calcular_tempo_aposentar(genero, idade):
    """
    Calcula o tempo que falta para o usuário se aposentar de acordo com o gênero.
    """
    idade_minima = 65 if genero == 'm' else 62
    tempo_aposentar = idade - idade_minima
    return max(0, tempo_aposentar)

obter_dados_pessoais()
calcular_idade()
obter_dados_clt()
calcular_tempo_aposentar()
# import datetime


# today = datetime.datetime.now()

# dados = {
#     'nome': input('Qual seu nome?: '),
#     'nascimento': input("Digite a data de nascimento no formato dd/mm/aaaa: "),
#     'clt': input('Você é CLT? (sim ou não): '),
#     'sexo': input('Qual seu gênero? (M/F): ').lower()

# }
# data_nascimento = datetime.datetime.strptime(dados['nascimento'], "%d/%m/%Y")
# # ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
# idade = today.year - data_nascimento.year
# dados['idade'] = idade

# if dados['clt'] == 'sim':
#     data_clt = input('Qual ano de contratação(dd/mm/aaaa)?: ')
#     salario = float(input('Qual seu salario: '))
#     data_contratacao = datetime.datetime.strptime(data_clt, "%d/%m/%Y")
#     dados['data_contratacao'] = abs(data_contratacao.year - today.year)
#     dados['salario'] = salario

# if dados['sexo'] == 'm':

#     tempo_aposentar = abs(dados['idade'] - 65)
#     dados['tempo_aposentar_M'] = tempo_aposentar
#     print(
#         f'Olá {dados["nome"]},vi que você trabalha à {dados["data_contratacao"]} ano(s).')
#     print(
#         f'Você tem {dados["idade"]} anos e faltam {dados["tempo_aposentar_M"]} anos para você se aposentar')

# else:

#     tempo_aposentar = abs(dados['idade'] - 62)
#     dados['tempo_aposentar_F'] = tempo_aposentar
#     print(
#         f'Olá {dados["nome"]},vi que você trabalha à {dados["data_contratacao"]} ano(s).')
#     print(
#         f'Você tem {dados["idade"]} anos e faltam{dados["tempo_aposentar_F"]} anos para você se aposentar')
