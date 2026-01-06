# if True:
#     print('Condition true')

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater than:     >
# Less than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# language = 'Python'

# if language == 'Python':
#     print('Language is Python')
# else:
#     print('No match')

language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')


# and
# or
# not

# user = 'Admin'
# logged_in = True

# if user == 'Admin' and logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')




# user = 'Admin'
# logged_in = False

# if user == 'Admin' or logged_in:
#     print('Admin Page')
# else:
#     print('Bad Creds')




# logged_in = True              # Welcome
logged_in = False                # Please login

if not logged_in:
    print('Please login')
else:
    print('Welcome')