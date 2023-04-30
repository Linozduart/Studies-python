import os
from time import sleep

def notas(*n, sit=False):

    dados = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': sum(n)/len(n),

    }
    if sit == True:
        dados["situação"] = None
        if dados["média"] >= 8:
            dados["situação"] = 'Ótima'
        elif dados["média"] >= 6:
            dados["situação"] = 'Boa'
        else:
            dados["situação"] = 'Ruim'

    return dados


resp = notas(7.5, 9.5, 10, 6.5, sit=True)
print(resp)


sleep(3)

os.system('cls' if os.name == 'nt' else 'clear')