n = int(input())
a = str(input())
k = 1
for i in range (1,n):
    if i > 1:
        j = a[i + k]
        k = k + 1 

    print(a[0],j,end ="")




# for i in a: 
#     print(a)