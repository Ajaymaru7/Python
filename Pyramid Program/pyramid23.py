n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
b = int(4)
fp = 2*n-1
sp = int(1)
for a in range(n):
    print(" "*a + "*"*fp + " "*b + "*"*sp)
    fp -= 2
    sp += 2

#While Loop
print("\nWhile Loop")
a = int(0)
b = int(4)
fp = 2*n-1
sp = int(1)
while(a < n):
    print(" "*a + "*"*fp + " "*b + "*"*sp)
    fp -= 2
    sp += 2
    a += 1