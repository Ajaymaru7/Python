n = int(input("Enter No:"))
space = n

#For Loop
print("\nFor Loop")
for i in range(int(1),n+1):
    print("*"*i+" "*space+"*"*i)
    space -= 1

#While Loop
print("\nWhile Loop")
i = int(1)
space = n
while(i<=n):
    print("*"*i+" "*space+"*"*i)
    space -= 1
    i += 1