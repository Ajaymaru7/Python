n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
space = n
for i in range(1, n*4, 4):
    print(" "*space + "*"*i)
    space -= 1

#While Loop
print("\nWhile Loop")
space = n
i = 1
while(i<n*4):
    print(" "*space + "*"*i)
    space -= 1
    i += 4