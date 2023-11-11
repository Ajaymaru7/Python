from tkinter import N


n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
f_space = n
fpspace = int(1)
bpspace = n*2-3
print(" "*f_space + "*" + " "*3 + "*"*(n*2+1))
for i in range(n-2):
    f_space -= 1
    print(" "*f_space + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace += 2
    bpspace -= 2
print("*"*(n*2+1) + " "*3 + "*")

#While Loop
print("\nWhile Loop")
f_space = n
fpspace = int(1)
bpspace = n*2-3
i = int(0)
print(" "*f_space + "*" + " "*3 + "*"*(n*2+1))
while(i < n-1):
    f_space -= 1
    print(" "*f_space + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace += 2
    bpspace -= 2
    i += 1
print("*"*(n*2+1) + " "*3 + "*")