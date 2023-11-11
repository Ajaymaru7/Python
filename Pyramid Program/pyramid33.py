n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
bs = n-1
ins = int(0)
print(" "*bs + "*")
for i in range(n-2):
    bs -= 1
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    ins += 1
print("*"*(n*2-1))

#While loop
print("\nWhile Loop")
bs = n-1
ins = int(0)
i = int(0)
print(" "*bs + "*")
while(i < n-2):
    bs -= 1
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    ins += 1
    i += 1
print("*"*(n*2-1))