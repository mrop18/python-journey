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

# DICTIONARY

# 1.
# a = {"name": "Om", "age": 24}
# print(a["name"])

# Om        Correct
# Dict access uses keys, not positions — "name" directly maps to "Om"

# 2.
# a = {"x": 1}
# print(a["y"])

# Error     Correct
# Accessing a missing key with [] raises a KeyError

# 3.
# a = {"x": 1}
# a["x"] = 5
# print(a)

# x: 5      Wrong
# {'x': 5}
# Assigning an existing key REPLACES its value, it does not create a new key

# 4.
# a = {"x": 1}
# a["y"] = 2
# print(a)

# {'x': 1, 'y': 2}      Correct
# Assigning a new key adds a new key-value pair to the dictionary

# 5.
# a = {"x": 1, "y": 2}
# print(len(a))

# 2         Correct
# len() on a dict counts KEYS, not values

# 6.
# a = {"x": 1}
# print("x" in a)

# 1         Wrong
# True      Correct
# in checks ONLY KEYS in a dictionary, never values

# 7.
# a = {"x": 1}
# print(a.get("y"))

# None      Correct
# get() returns None instead of crashing when key is missing

# 8.
# a = {"x": 1}
# print(a.get("y", 0))

# 0         Correct
# get(key, default) returns the default value when key doesn’t exist

# 9.
# a = {}
# a["list"] = [1, 2]
# a["list"].append(3)
# print(a)

# {'list': [1, 2, 3]}       Correct
# Dict stores references, so modifying the list updates the value inside the dict

# 10.
# a = {"x": 1}
# b = a
# b["x"] = 10
# print(a)

# {"x": 1}      Wrong
# {"x": 10}     Correct
# Both a and b point to the SAME dictionary in memory


# bool()

# 1.
# bool()
# False
# Empty call defaults to False (no value = falsey).

# 2.
# bool(0)
# False
# Zero means “nothing” in numeric truth.

# 3.
# bool(" ")
# True
# String exists and is not empty, space still counts as content.

# 4.
# bool([])
# False
# Empty container = falsey.

# 5.
# bool([0])
# True
# List is not empty, content doesn’t matter.

# 6.
# bool({})
# False
# Empty dictionary = falsey.

# 7.
# bool({"a": None})
# True
# Dictionary has a key, so it exists.

# 8.
# bool(None)
# False
# None literally means “nothing”.

# 9.
# bool(0.0)
# False
# Zero in any numeric form is falsey.

# 10.
# bool([[], []])
# True
# Outer list is not empty, inner emptiness is irrelevant.


# CONDITIONALS

# 1.
# if 1:
    # print("A")

# A
# Any non-zero number is truthy, so 1 behaves like True.

# 2.
# if 0:
#     print("A")
# else:
#     print("B")

# B
# 0 is falsy, so Python skips the if block and runs else.

# 3.
# if []:
#     print("Yes")
# else:
#     print("No")

# No
# Empty containers are falsy, so the condition fails.

# 4.
# if " ":
    # print("Run")

# Run
# A string with a space is still non-empty, so it’s truthy.

# 5.
# x = None
# if x:
    # print("True")
# else:
    # print("False")

# False
# None represents “nothing,” which Python treats as falsy.

# 6.
# if {}:
    # print("Yes")
# else:
    # print("No")

# No
# An empty dictionary has no content, so it evaluates to False.

# 7.
# x = [1, 2]
# if x:
#     print("Not Empty")

# Not Empty
# A list with elements is non-empty, therefore truthy.

# 8.
# if False == 0:
#     print("Equal")

# Equal
# In Python, False is internally equal to integer 0.

# 9.
# x = ""
# if not x:
#     print("Empty")

# Empty
# not flips falsy to truthy, and an empty string is falsy.

# 10.
# x = 10
# if x > 5 and x < 20:
#     print("In range")

# In range
# Both comparisons are true, so and allows the block to run.