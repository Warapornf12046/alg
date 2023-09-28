def distcount(a,l,u):
    n= len(a)
    s=[0] *n  
    d = [0]*(u-l+1)

    for i in range(n):
        d[a[i]-l]  =  d[a[i]-l] + 1

    for j in range(1,u-l+1):
        d[j] =d[j-1] + d[j]
        
    for i in range(n-1,-1,-1):
        j =a[i]-l
        s[d[j]-1] = a[i]
        d[j] = d[j]-1
    return s

a = [12,14,15,12,16,13,14,16,15,12]
l = 12
u = 16
print(distcount(a,l ,u))

