n = int(input("Enyer No:"))

#For Loop
print("\nFor Loop")
b_space = int(0)
fpspace = n*2-3
bpspace = int(1)
print("*"*(n*2+1) + " "*3 + "*")
for i in range(n-1):
    b_space += 1
    print(" "*b_space  + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace -= 2
    bpspace += 2
print(" "*(b_space+1) + "*" + " "*3 + "*"*(n*2+1))

#While loop
print("\nWhile Loop")
b_space = int(0)
fpspace = n*2-3
bpspace = int(1)
i = int(0)
print("*"*(n*2+1) + " "*3 + "*")
while(i<n-1):
    b_space += 1
    print(" "*b_space + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace -= 2
    bpspace += 2
print(" "*(b_space+1) + "*" + " "*3 + "*"*(n*2+1))