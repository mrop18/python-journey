# Tuples are similar to Lists but lists are mutable and tuples are immutable 
# We can't modify Tuples

# Mutable
list1 = ['History', 'Math', 'Physics', 'CompSci']
list2 = list1

print(list1)        # ['History', 'Math', 'Physics', 'CompSci']
print(list2)        # ['History', 'Math', 'Physics', 'CompSci']

list1[0] = 'Art'

print(list1)        # ['Art', 'Math', 'Physics', 'CompSci']
print(list2)        # ['Art', 'Math', 'Physics', 'CompSci']

# Immutable
tup1 = ('Java', 'HTML', 'CSS', 'Python')
tup2 = tup1

print(tup1)         # ('Java', 'HTML', 'CSS', 'Python')
print(tup2)         # ('Java', 'HTML', 'CSS', 'Python')

tup1[0] = 'Php'     # TypeError: 'tuple' object does not support item assignment

print(tup1)
print(tup2)

