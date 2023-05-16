frase = str(input('Digite uma frase: ')).strip()

frase_invertida = ''.join(reversed(frase))

print(frase_invertida)

if frase == frase_invertida:
    print('Essa Frase é um palíndromo')
else:
    print('Essa Frase não é um palíndromo')

























"""

lower() e upper(): convertem a string para letras minúsculas ou maiúsculas, respectivamente.
strip(), lstrip() e rstrip(): removem espaços em branco do início, do fim ou dos dois lados da string, respectivamente.
replace(old, new): substitui todas as ocorrências de old por new na string.
split(sep): divide a string em uma lista de substrings usando sep como separador. Por padrão, sep é o espaço em branco.
join(iterable): concatena uma lista de strings em uma única string, separando cada string por self.

"""
