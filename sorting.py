def compcount(a):
    n = len(a)
    s=[0]*n
    countx = [0]* n
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] < a[j]: # จากมากไปน้อยใช้>
                countx[j]=countx[j]+1
            else:
                countx[i]= countx[i]+1
    for i in range(n):
        s[countx[i]] =a[i]
    return s
a =[29,21,14,32,7,6]
print(compcount(a))

