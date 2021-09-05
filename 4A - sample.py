t = int(input())
if(t % 2 == 0):
    print("YES")
else:
    print(t[1]+ (len(t)-2) + t[-1])