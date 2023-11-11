n = int(input("Enter no:"))

#for Loop
print("\nFor Loop")
a_s = n-2
print(" "*(a_s+1) + "*")
for b_s in range(n-1):
    if b_s == n-2:
        print("*"*(b_s+int(2)))
    else:
        print(" "*a_s + "*" + " "*b_s + "*")
        a_s -= 1

#While Loop....
print("\nWhile Loop")
a_s = n-2
b_s = 0
print(" "*(a_s+1) + "*")
while(b_s < n-1):
    if b_s == n-2:
        print("*"*(b_s+2))
        b_s += 1
    else:
        print(" "*a_s + "*" + " "*b_s + "*")
        a_s -= 1
        b_s += 1