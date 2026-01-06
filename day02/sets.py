# courses = {'History', 'Math', 'English', 'Physics'}
# print(courses)  # in sets order can change each time we run the code

# courses2 = {'History', 'Art', 'English', 'Physics', 'Art'}
# print(courses2)     # it also removes duplicate values

courses = {'History', 'Math', 'English', 'Physics'}
courses2 = {'History', 'Art', 'Design', 'Physics'}

# print(courses.intersection(courses2))   # prints only common in both sets = {'History', 'Physics'}
# print(courses.difference(courses2))   # prints only different from second set = {'Math', 'English'}
print(courses.union(courses2))   # prints all from both sets but not duplicate = {'Math', 'Physics', 'Design', 'Art', 'History', 'English'}
