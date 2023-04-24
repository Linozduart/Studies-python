frase = str(input('Digite eu uma frase')).strip()
a = frase.count('a')
first = frase.find('a') + 1
last = frase.rfind('a')
print(f'Essa frase contem  {a} letras A,ela aparece na {first},e pela ultima vez na posiçao {last}')
