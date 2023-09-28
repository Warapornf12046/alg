def changecoin(d,n):
    f = [0]
    for i in range(1,n+1):
        temp = 9223372036854775807
        j =0
        m = len(d)
        while j < m and i >= d[j]:
            temp = min(f[i-d[j]] , temp)
            j = j+1
        f.append(temp +1)
    return f[n]
d = [1,2,5,10]
n = 9
print(changecoin(d,n))