soHS, soNhom = map(int, input(). split())
sttHS = list(map(int, input().split()))
hs1 = set(sttHS)
hs2 = len(hs1)
lsst3 = []
x = 1

if hs2 >= soNhom:
    print("YES")
    for g in hs1:
        if x <= soNhom:
            i = sttHS.index(g) + 1
            lsst3.append(i)
            lsst3.sort()
        x = x + 1
    print(lsst3)
    print(" ".join(str(x) for x in lsst3))
else:
    print("NO")


# lst = [ 13, 15, 15, 15, 12]
# lst2 = [15, 13, 12]
# for i in lst2:
#         x = lst.index(i) + 1
#         lsst3.append(x)
#         lsst3.sort()
#         print(lsst3, end=" ",)
