def fatorial(num, show=False):
    res = 1
    for i in range(num, 0, -1):
        
        if show:
            print(i, end=' ')
            if i > 1:
                print('x ', end='')
            else:
                print(' = ', end='')
        res *= i
    return res

print(fatorial(5,True))
