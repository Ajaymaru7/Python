from tracemalloc import start


n = int(input("Enter No:"))

start = n
en = int(0)
i = int(1)
#For Loop
print("\nFoer Loop")
for space in range(start, en, -1):
    print(" "*space, "*"*i)
    i += 2
for space in range(0, start+1):
    print(" "*space, "*"*i)
    i -= 2

#While Loop
print("\nWhile Loop")
i = int(1)
space = n
while(space > 0):
    print(" "*space, "*"*i)
    i += 2
    space -= 1
while(space <= n):
    print(" "*space, "*"*i)
    i -= 2
    space += 1