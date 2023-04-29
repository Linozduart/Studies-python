import datetime

def voto(nasc):
    if nasc >= 18:
        return 'Obrigatório'
    elif nasc >= 16 or nasc >=65:
        return 'opcional'
    else:
        return 'negado'
hoje = datetime.datetime.now()
reposta = input('Qual seu ano de nascimento? dd/mm/aaaa:  ')
data_nasc = datetime.datetime.strptime(reposta, '%d/%m/%Y') 
idade = abs(data_nasc.year - hoje.year)
print(idade)
print(voto(idade))
