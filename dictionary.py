#Dictionary in python

print("\nPython Dictionary..\n")

dict = {'name' : 'Ajay Maru', 'cosmos' : '5657878978', 'email' : 'bhjgyugj@gmail.com', 'music' : 'rapsong'}

print("Dict. : ", dict)
print("dict[name] : ", dict['name'])

print("Change value of music... ")
dict['music'] = 'sadsong'
print("dict['music'] : ", dict['music'])

print("Delete email index form dict...")
del dict['email']
print("dict = ", dict)

print("Keys of dict : ", dict.keys())
print("Values of dict : ", dict.values())

print("Clearing the dict : ", dict.clear())