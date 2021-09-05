# n = int(input()) 
# m = int(input())
# i=0
# k = 0
# # a = int(input[])
# # for x in range(0, len(a)+1):
# #     if x > m:
# #         i = i + 1
# # print(i)
# while(i<n):
#     a = int(input())
#     if a > m :
#         k= k + 1
#     i=i+1
# print(k)


x = 0
lst = []
n, a=  map(int, input().split())
# a = int(input())
# for i in range(0,n):
ele = map(int, input().split())
lst.append(ele)
g= lst[a-1]
for m in lst:
        if m>=g:
            x= x + 1
print(x)

# n, Vitridiemsan = map(int, input().split())
# scores =  map(int,input().split())