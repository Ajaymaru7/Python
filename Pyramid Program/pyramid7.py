n = int(input("Enter No:"))

n = int(input("Enter No:"))
print("\nFor Loop")
#For Loop
for i in range(1, int(n+1)):
    print("*"*i)
for i in range(int(n - 1),0,-1):
    print("*"*i)


print("\nWhile Loop")
#While Loop
i = 1
while(i < n):
    print("*"*i)
    i += 1
while(i > 0):
    print("*"*i)