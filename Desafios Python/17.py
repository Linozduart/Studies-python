import math
op = float(input('Qual comprimento do Cateto oposto ?'))
ad = float(input('Qual comprimento do Cateto adjacente ?'))
hip = op**2 + ad**2
print(f'Esse tringulo tem a hipotenusa igual à {math.sqrt(hip)}')
