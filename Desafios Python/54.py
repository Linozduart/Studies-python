pessoas = 0
for x in range(7):
    idade = int(input('Qual sua idade ?: '))
    if idade < 21:
        pessoas += 1
print(pessoas)
