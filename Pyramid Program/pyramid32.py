n = int(input("Enter No:"))

#For Loop
print("\nFoe loop")
fa = n*2+1
space = int(-1)
print("*"*fa + " "*space + "*"*(fa-1))
for i in range(n):
    fa -= 2
    space += 4
    print("*"*fa + " "*space + "*"*(fa))
for i in range(n-1):
    fa += 2
    space -= 4
    print("*"*fa + " "*space + "*"*(fa))
print("*"*(fa+2) + " "*(space-4) + "*"*(fa+1))

#Whole loop
print("\nWhile loop")
fa = n*2+1
space = int(-1)
i = int(0)
print("*"*fa + " "*space + "*"*(fa-1))
while(i < n):
    fa -= 2
    space += 4
    print("*"*fa + " "*space + "*"*(fa))
    i += 1
i = int(0)
while(i < n-1):
    print("*"*fa + " "*space + "*"*(fa))
    i += 1
print("*"*(fa+2) + " "*(space-4) + "*"*(fa+1))