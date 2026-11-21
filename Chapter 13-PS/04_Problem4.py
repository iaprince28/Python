def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 3474, 53, 6734, 903, 754, 45, 55]
f = list(filter(divisible5, a))
print(f)