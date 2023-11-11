#print triangle in python

from math import factorial


n = int(input("Enter No:"))

#For Loop
print("\nFor Loop")
for i in range(n):
    for j in range(n-i+1):
        #for left spacing
        print(end=" ")
    for k in range(i+1):
        # ncr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(k)*factorial(i-k)), end=" ")
    print()

#While Loop
print("\nWhile Loop")
i = int(0)
while(i<n):
    j = int(0)
    k = int(0)
    while(j < n-i+1):
        print(end=" ")
        j += 1
    while(k<i+1):
        print(factorial(i)//(factorial(k)*factorial(i-k)), end=" ")
        k += 1
    i += 1
    print()
