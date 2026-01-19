s = [1, 4, 9, 18, 25]
print(s)


print(s[0])         # indexing returns the item = 1
print(s[-1])        # indexing returns the item = 25
print(s[-3:])       # slicing returns a new list = [9, 16, 25]

print(s + [36, 49, 64])     # supports concatenation [1, 4, 9, 18, 25, 36, 49, 64]

# unlike strings which are immutable, lists are a mutable type

s[3] = 16                   # replace the value
print(s)
print(s + [3, 7, 11])     # supports concatenation [1, 4, 9, 16, 25, 36, 49, 64]

s.append(36)                # s = [1, 4, 9, 16, 25, 36]
# s.append(36, 45)                # error
# s.append([36, 45])                # [1, 4, 9, 16, 25, [36, 49]]
print(s)

a = s.copy()                # s copied to a
print(a)

# s.clear()                   # s = [], empty
# print(s)

print(a)                    # s empty but a have data [1, 4, 9, 16, 25, 36]

b = [49, 64, 81]
s.extend(b)          # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(s)

print(s.count(4))           # 4 appear 1 time in list a
print(s.index(16))          # 16 placed on index number = 3
j = s.copy()
j.insert(2, 'hello')        # [1, 4, 'hello', 9, 16, 25, 36, 49, 64, 81]
print(j)                    
print(s)                    # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(s.pop())              # print last index value & deleted last index value 81
print(s)                    # remain [1, 4, 9, 16, 25, 36, 49, 64]
s.pop(2)                    # deleted 2 index value 9
print(s)                    # remain [1, 4, 16, 25, 36, 49, 64]
# s.reverse()               # reverse list to [64, 49, 36, 25, 16, 4, 1]
# print(s)

s.remove(36)                # removed value 36
print(s)

c = [3, 10, 4, 8, 1, 15]
# c.sort()                  # sort min - max
print(c)
c.sort(reverse=True)        #sort max - min
print(c)

d = [15, 4, 11]
print(d*3)                  # [15, 4, 11, 15, 4, 11, 15, 4, 11]

print(len(s))
print(len(c))
print(len(d))

print([x*3 for x in d])     # [45, 12, 33]

print(list("abcd"))         # ['a', 'b', 'c', 'd']
e = list(range(5))
print(e)                    # [0, 1, 2, 3, 4]
print(sum(e))               # 10
print(max(e))               # 4
print(min(e))               # 0

print(list(map(str, e)))    # convert values in strings in list ['0', '1', '2', '3', '4']








