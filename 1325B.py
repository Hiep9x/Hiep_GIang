t = int(input())

for i in range(0,t):
    n = int(input())
    k = list(map(int, input().split()))
    
    x = set(k)
    print(len(x))