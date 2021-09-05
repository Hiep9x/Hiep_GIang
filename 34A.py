soLinh = int(input())
lsst = list(map(int, input().split()))

k = 0
z = 1
q=1
lsst2 = []
lsst3 = []
for i in range(0,soLinh -1):
    g = []
    if i < soLinh :
        n = lsst[i]
        p = lsst[i + 1]
        g.append(n)
        g.append(p)
        lsst2.append(g)
        i = i + 1

y = lsst[-1], lsst[0]
lsst2.append(y)
print(lsst2)
for x in range(0,len(lsst2)): 
   b = lsst2[x][k]
   c = lsst2[x][z]
   m = abs(b -c)
   lsst3.append(m)
   

print(lsst3)
v = min(lsst3)
for n in lsst2:
    if lsst3.index(v) == lsst2.index(n):
        # print(lsst3.index(v),lsst2.index(n))
        y = lsst.index(lsst2[lsst2.index(n)][0])
        j = lsst.index(lsst2[lsst2.index(n)][1])
    
print(y,j)
