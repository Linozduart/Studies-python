altura = float(input('Qual sua altura ?: '))
massa = float(input('Qual sua massa ?: '))
imc = massa/(altura**2)
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <=25:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('obesidade morbida')
