friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
print(friends)

friends.append("Harry") #Append means to add something at the end of the list
print(friends)

l1 = [1, 34, 63, 6, 11]
l1.sort() #To arrange int in systematically
print(l1)

l1 = [1, 34, 63, 6, 11]
l1.reverse() #List content will be reversed
print(l1)

l1 = [1, 34, 63, 6, 11]
l1.insert(3, 33333) #Insert 33333 such that it's index in the list is 3
print(l1)

l1 = [1, 34, 63, 6, 11]
l1.pop(3) #Pop method removes an element from the list
print(l1)
''' value = l1.pop(3)
print(value)'''

l1 = [1, 34, 63, 6, 11]
l1.remove(63)
print(l1)
