def shiftTable(p):
    m = len(p)
    table1 ={} 
    for j in range(m-1):
        table1[p[j]] = m-1-j

    return table1
p ='barber' #ไม่นับตัวท้าย ไม่มีshift=pattern
print(shiftTable(p))

def horspool(p, t):
    tablex = shiftTable(p) 
    m = len(p)
    n=len(t)
    i = m-1
    
    while i<= n-1:
        k=0
        while k <=m-1 and p[m-1-k]==t[i-k]:
            k = k+1
        if k == m:
            return i-m+1
        else:
            if t[i] in tablex.keys():
                i = i+ tablex[t[i]] #ถ้าไม่อยู่ใน dic= s
                # print(tablex[t[i]])
            else:
                i = i+m
                print('shift',m)
    return -1


p ='barber'
t = 'barbbwarbejjjrerbarbarbbwarbejjjrerba' #bwarbejjjr
print(horspool(p,t))




