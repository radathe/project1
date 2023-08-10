a = 2
b = 11
for i in range(99):
    a1 = a
    b1 = b
    while b!=0:
        a = a%b
        a, b = b, a
    a = a1 + a
    b = b1 + (a - a1)
print(a, b)
