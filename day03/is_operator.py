# is operator

a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)           # True
# print(a is b)           # False = because id of b is not equal to a

# now if
b = a
print(id(a))
print(id(b))
print(a is b)           # True
