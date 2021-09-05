t = input()
x = 0
y = 0
for i in range(0, len(t)):
    if  t[i].islower():
        x = x + 1
    else:
        y = y + 1
if x >= y:
    print(t.lower())
else:
    print(t.upper())

    