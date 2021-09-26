socauthu = input()
a = socauthu.find("1111111")
b = socauthu.find("0000000")
if a >= 0:
     check = True 
elif b >= 0:
     check = True
else:
    check = False
if check == True:
    print("YES")
else:
    print("NO")


    
