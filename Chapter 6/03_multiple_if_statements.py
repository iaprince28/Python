a = int(input("Enter your age: "))

#If statement no: 01

if(a%2 == 0):
    print("a is even")
#End of if statement no: 01

#If statement no: 02

if(a>=18):
    print("You are  about the age of consent")
    print("good for you")

elif(a<0):
    print("You are entering an invalid negative age")


else:
    print("You are below the age of consent")
#End of if statement no: 02

print("End of program")
