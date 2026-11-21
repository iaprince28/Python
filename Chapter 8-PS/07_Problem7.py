def remove(l, word):
    for item in l:
        l.remove(word)
        return l

l = ["Prince", "Pranto", "Opu", "Joy"]

print(remove(l, "Joy"))

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
l = ["Harry", "Rohan", "Shubham", "an"]
print(remove(l, "an"))       