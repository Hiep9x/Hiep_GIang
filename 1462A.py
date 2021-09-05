t = int(input())
s = 1
for i in range (0, t):
    n = int(input())
    k = list(input().split())
    g = list(reversed(k))
    print(k) 
    print(g)
    for p in g: 
        
         k.insert(s,p)
         s = s + 2
         print(k)
    s = 1
    print("k sau ", k)
    x = k[0:n]
    
   
    print(" ".join(str(l) for l in x))
    
