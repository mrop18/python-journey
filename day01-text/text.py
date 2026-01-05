#\n means new line
# s= 'First line. \nSecond line.' 

# result :
# First line 
# Second line

# r befpre quotes, prints the same line with special characters
s= r'First line. \nSecond line.' 
print(s)

# result :
# First line. \nSecond line.

print('c:\some\name')
print(r'c:\some\name')

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium') 

print(3 * 'un' 'ium') 

# two or more string literals next to each other are automatically concatenated
print('Py' 'thon')

prefix = 'Py'
print(prefix + 'thon')

# strings can be indexed

word = 'Python'
print(word[0])          # character in position 0 = P
print(word[5])          # character in position 5 = n
print(word[-1])         # character in position -1 = n
print(word[-5])         # character in position -5 = y

# Indexing is used to obtain individual characters, Slicing allows to obtain a substring

print(word[0:2])        # from position 0(included) to position 2(excluded) = Py
print(word[2:5])        # from position 2(included) to position 5(excluded) = tho
print(word[:2])         # from position beginning to position 2(excluded) = Py
print(word[3:])         # from position 3(included) to the end = hon
print(word[-2:])        # from position -2(included) to the end = on

# Python strings cannot be changed - they are immutable. Therefore, assigning to an indexed position in the string result in an error

# word[0] = 'j'
# print(word)

# But can create a new one

word1 = 'J' + word[1:]
print(word1)            # result = Jython

# the function len() return the length of a string

print(len(word))        # result = 6







