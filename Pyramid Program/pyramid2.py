# Using for loop

print("For Loop")
#Function to demonstrate printing pattern
n = int(input("Enter no:"))
    #number of spaces
k = 2*n - 2
#outer loop to hanhel no of rows
for i in range(0, n):
    #inner loop to handel no of spaces
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    #inner loop to handel no of colums
    for j in range(0, i+1):
        print("* ", end="")
    print()
print("------------------------")

# using while loop

print("While Loop")
n = int(input("Enter No:"))
n = 5; i = 0
while(i <= n):
    print(" " * (n - i)+ "*" * i)
    i+=1
