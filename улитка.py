a = []

for n in range(1, 55):
    a.append(n*(n+1))
b = a
nok = a[-1]
for i in range(len(a)):
    if nok % a[i] != 0:
        nok = nok*a[i]
#print(nok)
koef = []
s = 0
for i in range(len(a)):
    koef.append(nok/a[i])
    s = s + koef[i]/nok
print(s)