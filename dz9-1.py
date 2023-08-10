lst_chet = []
lst_nechet = []
for i in range(10):
    a = int(input())
    if a%2 ==0:
        lst_chet.append(a)
    else:
        lst_nechet.append(a)
print(lst_chet)
print(lst_nechet)