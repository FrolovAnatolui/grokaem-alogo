def fact(x):
    if (x == 1):
        return 1 # base
    else:
        return x * fact(x-1)


print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))
print(fact(7))
print(fact(8))