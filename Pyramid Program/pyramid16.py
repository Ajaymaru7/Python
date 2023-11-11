n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
space = n-3
print("*"*n)

for i in range(n-2):
    print("*" + " "*space + "*")
    space -= 1
print("*")

#While Loop
print("\nWhile Loop")
space = n-3
print("*"*n)
i = 0
while(i<n-2):
    print("*" + " "*space + "*")
    space -= 1
    i += 1
print("*")