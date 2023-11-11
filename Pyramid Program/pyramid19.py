n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
i = 1
for space in range(n*3+1, 1, -3):
    print(" "*space + "*"*i)
    i += 4

#While Loop
print("\nWhile Loop")
i = 1
space = n*3+1
while(space > 1):
    print(" "*space + "*"*i)
    i += 4
    space -= 3