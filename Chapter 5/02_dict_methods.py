marks = {
    "Prince": 100,
    "Shofik": 65,
    "Masum": 27,
    0: "Prince"

}
'''
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Prince": 99})
print(marks)

print(marks.get("Prince")) #Prints None
print(marks["Prince"]) #Returns an error
'''
