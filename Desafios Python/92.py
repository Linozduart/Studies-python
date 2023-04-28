import datetime


today = datetime.datetime.now()

dados = {
    'nome': input('Qual seu nome?: '),
    'nascimento': input("Digite a data de nascimento no formato dd/mm/aaaa: "),
    'clt': input('Você é CLT? (sim ou não): '),
    'sexo': input('Qual seu gênero? (M/F): ').lower()

}
data_nascimento = datetime.datetime.strptime(dados['nascimento'], "%d/%m/%Y")
# ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
idade = today.year - data_nascimento.year
dados['idade'] = idade

if dados['clt'] == 'sim':
    data_clt = input('Qual ano de contratação(dd/mm/aaaa)?: ')
    salario = float(input('Qual seu salario: '))
    data_contratacao = datetime.datetime.strptime(data_clt, "%d/%m/%Y")
    dados['data_contratacao'] = data_contratacao.year - (today.year)
    dados['salario'] = salario

if dados['sexo'] == 'm':

    tempo_aposentar = abs(dados['idade'] - 65)
    dados['tempo_aposentar_M'] = tempo_aposentar
    print(
        f'Olá {dados["nome"]},vi que você trabalha à {dados["data_contratacao"]} anos.')
    print(
        f'Você tem {dados["idade"]} anos e faltam {dados["tempo_aposentar_M"]} anos para você se aposentar')

else:

    tempo_aposentar = abs(dados['idade'] - 62)
    dados['tempo_aposentar_F'] = tempo_aposentar
    print(
        f'Olá {dados["nome"]},vi que você trabalha à {dados["data_contratacao"]} anos.')
    print(
        f'Você tem {dados["idade"]} anos e faltam{dados["tempo_aposentar_F"]} anos para você se aposentar')
