# using for loop

print("For Loop")
n = int(input("Enter No:"))
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end="")
    print()
print("--------------------------")

# using while loop

print("While Loop")
n = int(input("Enter No:"))
i = 1
while (i <= n):
    j = 1
    while(j <= i):
        print((j + 1 - 1), end="")
        j = j + 1
    i = i + 1
    print()
