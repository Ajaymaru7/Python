# Pattern using for loop

print("For Loop")
n = int(input("Enter No:"))
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end="")
    print()
print("------------------------")

# Pattern using while loop

print("While Loop")
n = int(input("Enter No:"))
i = 1
while (i <= n):
    j = 1
    while(j <= i):
        print("*", end="")
        j += 1
    print()
    i += 1
