def coinrow(c):
    f = [0,c[0]]
    n = len(c)
    for i in range(1,len(c)):
        f.append(max(c[i] + f[i-1], f[i]))
    return f[n]
c = [5,1,2,10,6,2]
print(coinrow(c))