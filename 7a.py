x = int(input())
i=0
while(i < x) :
    g = input()
    if(len(g)>10):
        print(g[0],(len(g)-2),g[-1], sep='')
    
    else:
        print(g)
    
    
    i = i + 1 


# n = int(input())
# for i in range(0 , n):
#     x = str(input())
#     l = len(x)
#     if l>10:
#         print(x[0], end="")
#         print(l-2, end="")
#         print(x[-1])
#     else:
#         print(x)