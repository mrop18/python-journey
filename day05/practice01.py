# List

# 1.
# a = [1, 2, 3]
# a.append(4)
# print(a)

# [1, 2, 3, 4] correct
# append() adds ONE element to the same list object, at the end.

# 2.
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# [1, 2, 3] wrong
# [1, 2, 3, 4] correct
# b = a does NOT copy the list — both names point to the SAME memory. like two remote controls for one TV

# 3.
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a, b)

# [1, 2, 3, 1, 2, 3, 4] wrong (if print(a + b), than it's correct answer)
# [1, 2, 3] [1, 2, 3, 4] correct
# copy() creates a NEW list, so changes in b do not affect a. Like photocopy, not mirror

# 4. 
# a = [10, 20, 30]
# a.insert(1, 99)
# print(a)

# [10, 99, 20, 30] correct
# insert(index, value) pushes elements to the right and keeps the list intact.

# 5.
# a = [1, 2, 3, 4]
# print(a[-1])

# 4 correct
# -1 always means “last element”, no matter the list size.

# 6.
# a = []
# a.append([1, 2])
# a.append([3, 4])
# print(a)

# [[1, 2], [3, 4]] correct
# A list can store ANY object — including another list — without flattening.

# 7.
# a = [1, 2, 3]
# a.remove(2)
# print(a)

# [1, 3] correct
# remove(value) deletes the FIRST matching value, not by index.

# 8.
# a = [1, 2, 3]
# print(len(a))

# 3 correct
# len() counts top-level elements only, not nested ones.

# 9.
# a = [1, 2, 3]
# print(2 in a)

# True correct
# in operator checks for existence (True or False), not position.

# 10.
# a = [1, 2, 3]
# a.clear()
# print(a)

# [] correct
# clear() empties the list but keeps the same list object alive.

# Tuple

# 1.
# a = (1, 2, 3)
# print(a[1])

# 2         correct
# Tuples are ordered, so index 1 always means the second element.

# 2.
# a = (1, 2, 3)
# a[0] = 10

# Error     correct
# Tuples are immutable, so you cannot change what index points to.

# 3.
# a = (1,)
# print(type(a))

# <class 'tuple'>   correct
# The comma creates the tuple, not the parentheses.

# 4.
# a = (1, 2, 3)
# print(len(a))

# 3         correct
# len() counts how many elements the tuple holds.

# 5.
# a = (1, 2, 3)
# b = a + (4, 5)
# print(b)

# (1, 2, 3, 4, 5)   correct
# Tuples can’t change, so Python creates a new tuple when adding.

# 6.
# a = (1, 2, 3)
# print(3 in a)

# True      correct
# in checks values, not positions.

# 7.
# a = (1, 2, 3)
# b = a
# print(a is b)

# False    # Wrong
# True      correct
# b is not a copy; it points to the same tuple in memory.
# = never copies objects — it copies references.

# 8.
# a = ()
# print(bool(a))

# False     correct
# Empty containers are always False in Python.

# 9.
# a = ([], [])
# a[0].append(1)
# print(a)

# (1, [], [])   # Wrong
# ([1], [])     correct
# The tuple is immutable, but the list inside it is mutable.
# Tuple immutability protects the container, not the objects inside it.

# 10.
# a = (1, 2)
# print(type(a) == tuple)

# True          correct
# type() compares exact object type.