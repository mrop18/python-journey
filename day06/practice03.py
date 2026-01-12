# 1.
# nums = [3, 8, 2, 6]
# i = nums[0] + nums[2]
# j = nums[i % 4]

# print(j)

# Ans: 8

# 2.
# a = 256
# b = 256
# c = 257
# d = 257
# print(a is b, c is d)
# Ans : True True

# 3.
# a = {'x': 1}
# b = a

# a.update({'x': 2})
# a = {'x': 3}

# print(b)
# print(a)

# Ans: 
# {'x': 2}
# {'x': 3}

# 4.
# x = 10
# list = [x for x in range(3)]

# print(x)

# Ans : 10

# 5.
# s = 'ab'
# t = s * 3
# print(t[4])

# Ans : a


# 6.
# a = float('nan')
# b = float('nan')

# s = {a, b}
# print(len(s))

# Ans: 2

# 7. 
# print(1 < 2 < 3 == True)

# Ans : False

# 8.
# print(1 or 0 and 0 or 2 and 3)
# Ans : 1
# print(0 or 5 and 0 or 7)
# Ans : 7
# print("" or "hello" and "" or "world")
# Ans : world
# print(None or 0 or "OK" and "")
# Ans:    # "" empty

# 9. 
# x = [1, 2]
# y = x

# x = x+ [3]

# print(y)

# Ans : [1, 2]

# 10.3
# a = [1, 2, 3]
# b = a[:]
# b[0] = 99

# print(a)

# Ans : [1, 2, 3]
