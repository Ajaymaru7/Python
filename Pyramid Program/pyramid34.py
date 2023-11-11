n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
bs = int(1)
ins = n-3
print("*"*(n*2-1))
for i in range(n-2):
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    bs += 1
    ins -= 1
print(" "*(n-1) + "*")

#While loop
print("\nWhile Loop")
bs = int(1)
ins = n-3
i = int(0)
print("*"*(n*2-1))
while(i < n-2):
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    bs += 1
    ins -= 1
    i += 1
print(" "*(n-1) + "*")