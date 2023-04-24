numbers = []
pairs = []
odd = []
for count in range(5):
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('Please enter a valid number.')
        continue
    numbers.append(number)
    if number % 2 == 0:
        pairs.append(number)
    else:
        odd.append(number)
print(f'Chosen numbers: {", ".join(map(str,numbers))}')
print(f'Of these, the even numbers are: {", ".join(map(str,pairs))}')
print(f'Of these, the odd numbers are: {", ".join(map(str,odd))}')
