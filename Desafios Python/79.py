valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor já adicionado')
    continuar = input('Deseja continuar ? [s/n]').lower()[0]
    if continuar == 'n':
        break
print(valores)