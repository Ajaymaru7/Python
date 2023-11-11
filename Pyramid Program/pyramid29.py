n = int(input("Enter No:"))
b = n
space = int(1)

#For Loop
print("\nFor Loop")
print(" "*b + "*")
for i in range(n-1):
    b -= 1
    print(" "*b + "*" + " "*space + "*")
    space += 2
space -= 4
for i in range(n-2):
    b += 1
    print(" "*b + "*" + " "*space + "*")
    space -= 2
print(" "*(b+1) + "*")

#While Loop
print("\nWhile Loop")
b = n
space = int(1)
print(" "*b + "*")
i = int(0)
while(i < n-1):
    b -= 1
    print(" "*b + "*" + " "*space + "*")
    space += 2
    i += 1
i = int(0)
space -= 4
while(i < n-2):
    b += 1
    print(" "*b + "*" + " "*space + "*")
    space -= 2
    i += 1
print(" "*(b + 1) + "*")