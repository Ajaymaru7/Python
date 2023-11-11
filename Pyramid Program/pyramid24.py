n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
b = int(4)
fp = 2*n-1
sp = int(1)
for a in range(n, 0, -1):
    print(" "*a + "*"*sp + " "*b + "*"*fp)
    fp -= 2
    sp += 2

#While Loop
print("\nWhile Loop")
a = n
b = int(4)
fp = 2*n-1
sp = int(1)
while(a > 0):
    print(" "*a + "*"*sp + " "*b + "*"*fp)
    fp  -= 2
    sp += 2
    a -= 1