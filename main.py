n=int(input("введите кол-во цифр: "))

a=[]
for i in range(n):
    a.append(int(input()))
i=0
while i<n-1:
    if(i>=0):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            i -= 1
        else:
            i+=1
    else:
        i += 1
print(a)