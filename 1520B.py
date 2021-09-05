
t = int(input())
s = 0

for i in range(0, t):
    n = int(input())
    for k in range(1, n+1):

        # j = b.append(k)
        # print("chuoi ky tu",b)

        a = "".join(str(k))
        # print(a)
        # del b[0:n]
        y = " ".join(a)
        # print(y)
        g = y.split()
        p = list(reversed(g))
        if g == p:
            s = s + 1
            print(g," -", p)
    print(s)

    s = 0
  