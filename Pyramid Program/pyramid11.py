n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
space = 0
for i in range(n, 0, -1):
    print("*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space += 1

#While Loop
print("\nWhile Loop")
space = 0
i = n
while(i>=0):
    print("*"*i + " "*space + "*"*i + " "*space + "*"*i + " "*space + "*"*i)
    space += 1
    i -= 1