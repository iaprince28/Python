#PYTHON DATATYPE

#Varriable declare

apple = "10taka"
print(apple)

#int type data

prince = 5528

print(prince)

print(type(prince))

# floating type data

banana  = 40.2

print(banana)

print(type(banana))

#Complex type data

mango = 5528j

print(mango)

print(type(mango))

#str type data

your_name = "imteaz"

my_name = "prince"

print(your_name + ' ' +my_name)

print('My name is' + ' ' + my_name)

#bool(boolean) type data

bool = True

print(bool)

print(type(bool))

bool = False

print(bool)

print(type(bool))

x = 8
y = 10

print(x > y) #false

x = 15
y = 15

print(x == y) #true

#Python string format () method

num1 = 20
num2 = 50

username = 'prince'

print( f'My name is {username}')

print( f"this is my super number {num1 + num2}") 

print( f'this is my super number',num1 + num2)

#Binary type data [Byte & Byte array, both are in a minimal range of 0-256.Byte numbers can't be changed but ByteArray numbers can be changed]

list = [1,2,3,4,5,6]

b = bytes(list)

print(type(b))

#Binary type data[ByteArray]

list1 = [2,4,6,8,10,12]

b1 = bytearray(list1)

print(type(b1))

b1[0] = 100 #Replacing the first number 2 to 100

print(b1[0])

#None type data

x = None #x = ' '

print(None)

print(type(None)) 

#list type data( Data can be changale anytime)

li = ['prince','masum','shofik','fahim']

li[1] = 'azim'

print(li)

print(type(li))

#Tuple type data( Data can't be changed)

tup = (5,10,15,20,25)

print(tup)

print(type(tup))

#range type data

ran = range(6)

print(ran)

print(type(ran))

for i in ran:
    print(i)
