n = int(input("Enter No:"))
start = n
en = int(0)

#For Loop
print("\nFor Loop")
for i in range(start,en, -1):
    print("*"*i)

#While Loop
i = n
print("\nWhile Loop")
while(i>0):
    print("*"*i)
    i-=1
