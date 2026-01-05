print("Hello, Let's start Python")

# to comment use (#)
# this is first comment line
spam = 1 # this is secont comment line
#... and now a third
text = "# this is not a comment, becuase it's inside quotes."

print(spam)
print(text)

greeting = 'Hello'
name = 'Ankit'

# message = greeting + name
# message = greeting +', '+ name
# message = greeting +', '+ name + '. Welcome!'
# message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!'


print(message)