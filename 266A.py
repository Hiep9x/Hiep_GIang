doaichuoi = int(input())
chuoi = input()
i = 1
a = 0
while i < doaichuoi:
    
    if chuoi[i] == chuoi[i-1]:
     a = a + 1
    i += 1
print(a)