chuoi = str('')
k=0
j = 0
i = 0
# print('moi nhap so luong dong')
n = int (input())
# print("so luong dong", n)
while(i<n):
    # print ('dong ', i+1)
    chuoi=input()    
    j=chuoi.count("1")
    if j>=2:
        k=k+1          
    i=i+1
print(k)
