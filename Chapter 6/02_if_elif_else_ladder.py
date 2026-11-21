a = int(input("Enter your age: "))

#If elif else ladder

if(a>=18):
    print("You are  about the age of consent")
    print("good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

print("End of program")
