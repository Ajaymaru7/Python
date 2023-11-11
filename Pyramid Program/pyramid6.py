n = int(input("Enter No:"))
i = n*2+1

#For Loop
print("\nFor Loop")
for space in range(n+1):
    print(" "*space, "*"*i)
    i -= 2

#While Loop
print("\nWhile Loop")
i = (n*2)+1
space = int(0)

while(space <= n):
    print(" "*space, "*"*i)
    i -= 2
    space += 1