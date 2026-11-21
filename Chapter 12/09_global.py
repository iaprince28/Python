def fun():
    global a
    a = 3
    print(a)


a = 89
fun()
print(a)