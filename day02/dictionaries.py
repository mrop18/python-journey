student = {'name': 'Ankit', 'age': '32', 'courses': ['Java', 'Python']}

# print(student['name'])
# print(student['age'])
# print(student['courses'])
# print(student['phone'])         #error
# print(student.get('name'))        # Ankit
# print(student.get('phone'))        # None
# print(student.get('phone', 'Not Available'))        # Not Available


# student['phone'] = '88 00 88888'
# student['name'] = 'Om'
# print(student)                  #{'name': 'Om', 'age': '32', 'courses': ['Java', 'Python'], 'phone': '88 00 88888'}


# student.update({'name': 'Wanku', 'age': '4', 'phone': '85978858'})
# print(student)          #{'name': 'Wanku', 'age': '4', 'courses': ['Java', 'Python'], 'phone': '85978858'}
# del student['age']
# print(student)          # age deleted  = {'name': 'Wanku', 'courses': ['Java', 'Python'], 'phone': '85978858'}

print(student.keys())       #dict_keys(['name', 'age', 'courses'])
print(student.values())     #dict_values(['Ankit', '32', ['Java', 'Python']])
print(student.items())      #dict_items([('name', 'Ankit'), ('age', '32'), ('courses', ['Java', 'Python'])])

for key in student:
    print(key)

    # name
    # age
    # courses

for key, value in student.items():
    print(key, value)

    # name Ankit
    # age 32
    # courses ['Java', 'Python']