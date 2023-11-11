n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
i = 3*n+1
for space in range(n):
    print(" "*space + "*"*i)
    i -= 4

#While Loop
print("\nWhile Loop")
i = 3*n+1
space = int(0)
while(space < n):
    print(" "*space + "*"*i)
    i -= 4
    space += 1