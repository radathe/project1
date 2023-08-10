

def factor(n):
    if n == 1:
        return 1
    return factor(n-1)*n

print(factor(int(input('Argument: '))))
