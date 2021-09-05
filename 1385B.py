t = int(input())
j = []
r = []
# a = []
# o = []
i = 0
# while i < t:
#     n = int(input())
#     x = list(map(int, input().split()))
#     # print(x)
#     k = set(x)
#     # print(k)
#     for v in k:
#         r.append(v)
#     # print(r) tạo list các ký tự ko trùng nhau
# # tìm vị trí các ký tự sau lọc trong input ban đầu và sắp sếp theo thứ tự
#     for u in r:
#         y = x.index(u)
#         a.append(y)
#         c = sorted(a)
#     # print("thu tu chua sap xep", a)

#     del a[0:n]
#     # print("thu tu các chu", c)
# # Từ vị trí các ký tự sau khi đc sắp xếp, nhặt các ký tự đấy ra
#     for z in c:
#         p = x[z]
#         o.append(p)
#     del r[0:n]

#     i = i + 1

#     print(" ".join(str(f) for f in o))
#     del o[0:n]



while i < t:
    n = int(input())
    x = list(map(int, input().split()))
    for s in x:
       y= x.index(s)
       j.append(y)
    print(j)
    for g in j:
        k = x[g]
        a = r.append(k)

    i= i + 1
    print(a)