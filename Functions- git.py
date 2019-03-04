# 4.13.3: Greetings
# Caleb Taylor
# 2.5.19


name = input("What's your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Caleb Taylor
# 2.11.18

x = 10

def print_something():
    x = 3
    print('\n', x)

print('\n',x)
print_something()


#4.13.6: Functions and Variables, Part 3
# Caleb Taylor
# 2.18.19


def print_number(x):
    print('\n', x)

print_number(13)
print_number(23)


# 4.14.4: Name and age
# Caleb Taylor
#2.18.19

def name_and_age(name, age):
    print('\n','Hi, my name is', name, 'and I am', age, 'years old')

name_and_age('Caleb', 16)
name_and_age('Shamiel', 16)


# 4.14.5: Default Parameter Value
# Caleb Taylor
# 2.19.19

def print_two_number(x, y = 20):
    print('First number:', x)
    print('Second Number:'+ str(y))

print_two_number(34, 45)
print_two_number(78) 


# 4.16.6: print Sum
# Caleb Taylor
# 2.19.19

def print_sum(x, y):
    print(x + y)

print_sum(46,62)



# 4.16.4: Enter Name and Age using the try and execpt rule
# Caleb Taylor
# 2.20.19

name = input('Enter your name: ')

age = 1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('\n''That wasn\'t an integer for your age')

print('\n''name:', name)
print('Age:', age)