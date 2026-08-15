li = [1, 2, 3]

print(type(li))
print(li)

li[1] = 10

print(li)

li = ["prince", "imteaz", "alam"]

print(type(li))
print(li)

li = [True, False, True, False]

print(type(li))
print(li)

#Access list iteem

Access = ['WSPN', 'RAW', 'WWE', 'ME']


print(Access[3])

# Chnage list iteem

Access[3] = 'EEE'

print(Access)

# Append(adding int number)

Access.append(10)

print(Access)

#nsert(adding something)

Access.insert(0, 'CSE')
Access.insert(2, 'IIT')

print(Access)

# Remove method (remove some specify iteem)

list = ['imteaz', 'alam', 'prince', 28]
list.remove('alam')
print(list)

# Pop method(remove some specify iteem)

list.pop(1)
list.pop() #If we doesn't write something,it will remove the last iteem
print(list)