# # TODO: Car Data
# # [ ]: Write a program to store the car data in a dictionary.
# '''
# Your program needs to take the key as input and output the corresponding value.
#
# Sample Input
# year
#
# Sample Output
# 2018
# '''
# car = {
#     'brand':'BMW',
#     'year': 2018,
#     'color': 'red',
#     'mileage': 15000
# }
#
#
# key = input()
#
# value = car.get(key)
# print(value)
#
#
#
#
# ########################################################
# #! To determine whether a key is in a dictionary, you can use in and not in,
# #  just as you can for a list.
#
# x = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
# }
#
# print( 1 in x)
# print( 2 not in x)
# print( 'three' in x)
# print(len(x))
# print(x.get(2))             #? give us value of key
# print(x.get(5,'not found'))
# print(x[2])                 #! indexing not index == get
#
# ########################################################
#
# # TODO: National economic freedom
# # [ ]:
# '''
# You are working on data that represents the economic freedom rank by country.
# Each country name and rank are stored in a dictionary, with the key being the country name.
#
# Complete the program to take the country name as input and output its corresponding economic freedom rank.
# In case the provided country name is not present in the data, output "Not found".
# Recall the get() method of a dictionary, that allows you to specify a default value.
#
# '''
# data = {
#     'Singapore': 1,
#     'Ireland': 6,
#     'United Kingdom': 7,
#     'Germany': 27,
#     'Armenia': 34,
#     'United States': 17,
#     'Canada': 9,
#     'Italy': 74
# }
#
# country_name = input()
# freedom_rank = data.get(country_name,"Not found")
# print(freedom_rank)

########################################################
my_tuple = '1', '2', 'True'
print(my_tuple[2])

# TODO: Contact search
'''
You are given a list of contacts, where each contact is represented by a tuple, 
with the name and age of the contact.
Complete the program to get a string as input, search for the name in the list of contacts 
and output the age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31
If the contact is not found, the program should output "Not found".
'''

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
my_name = input()

for name in contacts:           ## access to tuple, then use index according to our needs
    if name[0] == my_name:
        print(f'{name[0]} is {name[1]}')

##################
x, y = [1, 2]
x, y = y, x
print(y)

a ,b , *c, d = 1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)    # list of items == *var
print(d)

#############
# TODO: Square up
'''
Tuples can be used to output multiple values from a function.
You need to make a function called calc(), that will take the side length of a square as its argument 
and return the perimeter and area using a tuple.
The perimeter is the sum of all sides, while the area is the square of the side length.

Sample Input
3
Sample Output
Perimeter: 12
Area: 9
The given code takes a number from user input, passes it to the calc() function, 
and uses unpacking to get the returned values.

'''

def calc(x):
    #your code goes here
    p = x * 4
    a = x ** 2
    return (p ,a)



side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))

#####################
# TODO: You are Qualified!
# [ ] : Complete the program to match the available jobs and the candidates based on their skills.
'''
You are working on a recruitment platform, which should match the available jobs and the candidates based on their skills.
The skills required for the job, and the candidate's skills are stored in sets.
Complete the program to output the matched skill.
You can use the intersect operator to get the values present in both sets.

'''

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
matched = skills & job_skills

# print as set ?
#print(skills & job_skills)

# we don't need output as set? so loop on it

for _ in matched:
    print(_)

# TODO: Ignore the Vowels
# [ ]: Output a list that contains letters of the word that are not vowels.
'''

Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.

Sample Input
awesome

Sample Output
['w', 's', 'm']
Use a list comprehension to create the required list of letters and output it.
'''
#word = input()
word = 'hello'
# you need make string as list by for loop
new_word = []
for _ in word:
    new_word.append(_)

vowel = {'a','e','i','o','u'}
#print(new_word)
last = []
for letter in word:
    if letter not in vowel:
        last.append(letter)

print(last)

# set will be delete the repeated letter

########################
# TODO: How Much?
# [ ];Fix the code to output the percentage of the price.
'''

You are given code that should calculate the corresponding percentage of a price.
Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
Fix the code to output the given percentage of the price.

Sample Input
50
10

Sample Output
5.0
The first input is the price, while the second input is the percentage we need to calculate: 10% of 50 is 5.0.
'''
price = int(input())
perc = int(input())

res = (lambda x,y:x- (y/100 * x))(price, perc)

print(perc/100 * price)   # we search for % not total

############################
# map !!, to take list items as parameters of certain function
# you should use return in your function
# you should use list before map to put your result on list

nums = [ 1,5,10]

def try_map(x):
    return x + 5

y = list(map(try_map, nums))
print(y)

## lambda
y = list(map(lambda x : x +5 , nums))
print(y)

# The function filter filters an iterable by leaving only the items that match a condition (also called a predicate). 


nums = [ 1,5,10, 2 , 4 ]

y = list(filter(lambda x: x % 2 == 0, nums))
print(y)

def xd(x):
    return x % 2 == 0

y = list(filter(xd,nums))           # be carful with (func , list)
print(y)

# TODO: Animal Lifetimes
# [ ]: Analyze a data set of animals and output how many of the animals are older than the given numbers.
'''

You are analyzing a data set of animals. The data is a list of numbers, which represent the ages of animals.
You need to take a number as input and output how many of the animals are older than the given number.
Output the number of elements of the resulting list.
'''

ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]

number = int(input())
ages.append(number)     # add number to list to be able to compare it with other on list

y = list(filter(lambda x: x > number, ages))        # x == for every item on list
print(len(y))

# TODO: Generating...
# [ ]: Create a generator function that will take two numbers as arguments and output the prime numbers in the provided range.
'''

Finding prime numbers is a common coding interview task.
The given code defines a function isPrime(x), which returns True if x is prime.
You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the isPrime() function to output the prime numbers in the given range (between the two arguments).

Sample Input
10
20

Sample Output
[11, 13, 17, 19]
The given code takes the two arguments as input and passes them to the generator function, outputting the result as a list.
'''
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
    for x in range(a,b):    # make iritable on certain range
        if isPrime(x):      # we ask if our item true according to isPrime function
            yield x
        
    
f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))

# how spelling 
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

# NOTE : Decorators provide a way to modify functions using other functions. 
# A single function can have multiple decorators.
# def decor(func):                    # our eunc == other function
#     def wrap():
#         print("============")
#         func()                      # our second function will be excute here
#         print("============")
#     return wrap                     # our decor return with wrap() output

# def print_text():
#     print("Hello world!")

# decorated = decor(print_text)       # variable which carry all that function, we can convert them to function
# decorated()

# print_text = decor(print_text)      # we can update 2nd function, when use variable with same name of function name
# print_text()


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

# insteade say (print_text = decor(print_text) we say [@decor])
@decor                      # apply this function on under it
def print_text():
    print("Hello world!")

print_text()


# TODO:
# [ ]:
'''
You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
***
INVOICE #42
***
END OF PAGE
The given code takes the invoice number as input and passes it to the invoice() function.
'''

#your code goes here

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input())

##########
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

############
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17)) # 17 go to is_even = 17 return number == not is_even == not false == true
print(is_even(23))

# TODO: Making It Work
# [ ]: Improve the function so that it can take any number of variables.


####################################
nums = {1, 2, 3, 4, 5, 6}

nums = {0, 1, 2, 3} & nums      # &&&&

print(nums)
nums = filter(lambda x: x > 1, nums)

print(len(list(nums)))

####################################

def power(x, y):
  if y == 0:
    return 1

  else:
    return x * power(x, y-1)        # 2 * (2,2)  = 2*2  = 4*2 =8

print(power(2, 3))

####################################

def func(**kwargs):

  print(kwargs["zero"])

func(a = 0, zero = 8)