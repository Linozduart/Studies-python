x = input('Digite algo')
print('O tipo primitivo desse valor e',type(x))
print(f'E um numero ? {x.isnumeric()}')
print(f'E esta em letra maiuscula ? {x.isupper()}')
print(f'E esta em letra minuscula ? {x.lower()}')
print(f'E um decimal ? {x.isdecimal()}')
print(f'E tem letras ? {x.isalpha()}')
print(f'E tem espaços ? {x.isspace()}')


