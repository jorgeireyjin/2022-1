def matriz(n):
    for i in range(1):
        for j in range(1,n+1):
            print(' ' * (n-j), ('-' * j))

n = int(input('Número n '))

matriz(n)