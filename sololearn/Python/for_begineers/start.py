from typing import TextIO

#+========================================+
print('='*60)
print( '*'*20 + '**Basic Concepts*' + '*'*20 )
print('='*60)
#+========================================+

# TODO: Goal!
# [x]: Create a program to calculate and output the total points earned by a soccer team.
# ? You need to calculate the points earned by a soccer team.
# ! The team won 18 games and ended 7 games as a draw.
# ? A win brings 3 points, while a draw brings 1. 

team_wons = 18
team_draw = 7
points = ( team_wons * 3 ) + ( team_draw * 1 )
print(points)


# TODO: How Many Seconds?
# [x]: Write a program to calculate how many seconds there are in a month.

month_to_days = 30
days_to_hours = 24
hours_to_minutes = 60
minutes_to_seconds = 60

print(month_to_days * days_to_hours * hours_to_minutes * minutes_to_seconds)


# TODO: Do The Math
# [x]: Write a program that will multiply the sum of 5 and 6 by 57.3 and output the result.

result = ( 5 + 6) * 57.3
print(result)

# NOTE:                
print(2**3**2) # ! it mean 3**2 = 9 , 2 ** 9 = 515
# ! The following code will result in the square root of 9:
print( 9 ** (1 / 2))        # ? The result will be a float.

# TODO: Exponentiation
# [x]: Write a code to output 4 raised to the 5th power.
print(4 ** 5 )

# TODO: Growing Bacteria
# [x]: Calculate and output the number of bacteria that will be in the culture after 24 hours.
# ? A bacteria culture starts with 500 bacteria and doubles in size every hour.
# ! Which means that after 1 hour the number of bacteria is 1000, after 2 hours, 2000, and so on. 
# NOTE: The formula to calculate the bacteria after N hours will be: 500*2ᴺ
bacteria = 500
doubles_hour = bacteria *2 ** 24
print(doubles_hour)

# TODO: Number Of Hours
# [x]: Calculate the number of hours in 888 minutes.
# ? Your program needs to output the number of hours and then the 
# number of remaining minutes, on separate lines.
# ! For example, 72 minutes are equal to 1 hour and 12 minutes, so your program would output:
# 1
# 12

## 72 = 1 , 12
minutes = 72
nums_hours = minutes // 60
nums_minutes = minutes - ( nums_hours * 60 )  # don't forget change them as minutes
print(f'{nums_hours}\n{nums_minutes}')

# ! or this way , which slololearn ask about it! 
# ? بما ان القسمه لها خارج قسمه ممثل بالساعات وباقي قسمه سيكون الدقائق 
minutes = 888
nums_hours = minutes // 60
nums_minutes = minutes % 60  
print(f'{nums_hours}\n{nums_minutes}')


# NOTE: quotient of dividing //

#+========================================+
print('='*60)
print( '*'*25 + '**Strings*' + '*'*25 )
print('='*60)
#+========================================+


# TODO: Output The String
# [x]: Fix the given code to generate the expected output.
print('I\'m learning Python. It\'s easy.')

# TODO: Words Of Wisdom
# [x]: Write a program to output Steve Jobs' most famous quote in the given format.
quote = '\"Stay hungry, stay foolish\" by Steve Jobs'
print(quote)


# ? carriage
print('12\rhi there') # ! to change text after it , by after it accordin to number of characters after it.
# NOTE : Windows uses \r\n to signify the enter key was pressed, while Linux and Unix use \n.
print("\r\n\r\n\r\n")
print('How many enters from above code? ')

# TODO: New Lines
# [x]:Write a program to output the letters A B C D, each on a separate line.

print('''
A
B
C
D
''')


# TODO: Star Triangle
# [x]: Fix the code to output a triangle of stars that has 4 rows.

print("*\n**\n***\n****")

# TODO: Hey There
# [x]: Write a program that will write the word 'hi' 42 times

print('hi' * 42)



#+========================================+
print('='*60)
print( '*'*25 + '**Variables*' + '*'*25 )
print('='*60)
#+========================================+


# NOTE: del                 
test_delete_variable = 55
print(test_delete_variable)

del test_delete_variable        # ?     it cause error , if we try call it again
# print(test_delete_variable)   # !     it deleted
                                # todo: Deleted variables can be reassigned. 

# TODO: Value Of The Variable
# [x]: Change the code to output the value of the variable raised to the power of 3.
num = 7
print(num ** 3)

# TODO: Contact Management System
# [x]: Complete the code for a contact management system, where name and age are the declared variable values.
name = "James"
age = "42"
message = f'{name} is {age} years old'
print(message)

# TODO: Desired Output
# [x]: Fix the code so that it produces the desired output.
# ? Somebody wrote code to take a string input and output it, repeated 10 times. 
x = input()
print(x*10)

# TODO: Get Notified!
# [x]: Write a program to add 3 stars at the beginning and the end of the notification text.
# ? You’re working on a notification system and need to make the notification text eye-catching.
# COMMENT: Sample Input : this is awesome , Sample Output : *** this is awesome *** 

text = input()
stars = '***' 
print(stars,text,stars)

# TODO: Convert The Input
# [ ]: Write a program to take x and y as input and output the string x, repeated y times.
'''
Write a program to take x and y as input and output the string x, repeated y times.
Sample Input
hi
3
Sample Output
hihihi
'''
x = input()
y = int(input())
repeated_string = x * y
print(repeated_string)

# TODO: Identity Cards
# [x]: Change the code in contact card program to take the name and age from user input and use them in the output.

name = input()
age = input()
print(name + " is "+age+" years old")

# NOTE : compare between strings
# ? compare strings lexicographically (the alphabetical order of words is based on 
# the alphabetical order of their component letters). For example:
print('a' > 'b')
print('btoo' >= 'mohammed')

# NOTE: that we used the int() function to convert the Boolean to an integer.
x = 7 > 5       # True
print(int(x))   # ! 1

#+========================================+
print('='*60)
print( '*'*25 + '**Flow chart*' + '*'*25 )
print('='*60)
#+========================================+

# TODO: At The Boiling Point!
# [x]: Write a program that checks if the water is boiling.
# [x]: Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.
# NOTE : Sample Input 105, Sample Output Boiling , Do not output anything if the water is not boiling.

temp = int(input())

if temp >= 100:
    print('Boiling ')

# NOTE: use nested lists to represent 2D grids, such as matrices. 
# COMMENT: This is useful because a matrix-like structure can allow you to store data in row-column format, 
#! like in ticketing programs, that need to store the seat numbers in a matrix, with their corresponding rows and numbers. 


# TODO: Pure Gold
# [x]: Given the % of gold purity as input, Sample Input: 93.4 , Sample Output: Accepted
# [x]: 22K gold has 91.7% or more gold in it, while 24K corresponds to 99.9% and above purity.
# [x]: For your gold purity checker, output 'Accepted' only if it corresponds to 22K or 24K.

purity = float(input())
# 22K = ( 91.7 - 99.8)
# 24K = ( >=99.9)
if purity >= 91.7 :
    print("Accepted")
elif purity >= 99.9:
    print("Accepted")


# TODO: Face Control
# [ ]: Write a program to control the entrance to a club so that only guests aged 18 or older are allowed to enter.
'''
Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, 
and outputs "Allowed" if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.
'''
age = int(input())

if age >= 18:
    print('Allowed')
else:
    print('Sorry')

# TODO: Leap Year
# [x]: Make a program to check whether a year is a leap year or not.
'''
COMMENT: To check whether a year is a leap year or not, you need to check the following:
[x]: If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
[x]: If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
[x]: If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a leap year.
NOTE: Sample Input 2000, Sample Output Leap year
'''
year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year')
        else:
            print('Not a leap year')
    else:
        print('Leap year')
else:
    print('Not a leap year')
    
            

# TODO: Age Groups
# [ ]: Given the age of a person as an input, output their age group.
'''
Given the age of a person as input, you need to output their age group.
Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64
Senior: 65+

Sample Input
42
Sample Output
Adult
'''
age = int(input())

if age >= 0 and age < 12:
    print('Child')
elif age >= 12 and age < 18:
    print('Teen')
elif age >= 18 and age < 65:
    print('Adult')
elif age >= 65:
    print('Senior')


# TODO: 24K Magic
# [x]: Improve your gold purity checker program and output the corresponding purity level in Karats.
'''
Here is the purity chart we’ll be using:
24K – 99.9%
22K – 91.7%
20K – 83.3%
18K – 75.0%

[x]: If the percentage is between 75 and 83.3, the gold is considered to be 18K.
[x]: If it's between 83.3 and 91.7 - then it’s 20K, and so on.
[x]: Given the percentage as input, output the corresponding Karat value, including the letter K.
[x]: Do not output anything, if the percentage is lower than 75%.
NOTE: Sample Input: 92.4, Sample Output: 22K
'''

purity = int(input())                 # BUG:  ! strings can't chanhe to float , use int()
#your code goes here 
if purity >= 75.0 and purity < 83.3:
    print('18K')
elif purity >= 83.3 and purity < 91.7:
    print("20K")
elif purity >= 91.7 and purity < 99.9:
    print("22K")
elif purity >= 99.9:
    print("24K")
else:
    print('Not good')

##############################################################################
# NOTE: how we make loop to make sum function for numbers
sum = 0
x = 10

while x > 0:
    sum += x            ## to sum
    x -= 1              ## to decrase our 
print(sum)

##############################################################################

# TODO: Call It Even
# [ ]: Change the code to make it output only even numbers from a given range.
'''
The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers that are multiples of both 3 and 5, output "SoloLearn".
You need to change the code to skip the even numbers so that the logic only applies to odd numbers in the range
'''
n = int(input())
for x in range(1 , n + 1, 2):           #! to avoid even we start from one and move by 2 steps , also add 1 to user input due to index start from zero
    #print(x)                           #? also add 1 to user input due to index start from zero
    if x % 3 == 0 and x % 5 == 0:       # BUG: you should start by compination of both 3 and 5 first
        print('sololearn')
    elif x % 5 ==0:
        print("learn")
    elif x % 3 == 0 :
        print('solo')
    else:
        print(x)

# TODO: Hit Or Miss
# [x]: Create a program that will take 4 action results as input by calculating 
# [x]: and outputting the remaining points of the player based on their shots.
# [x]: Use a while loop to take input during each iteration and calculate the points.
'''
#? You are making a game! The player tries to shoot an object and can hit or miss it.
# [x]: The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.
# NOTE: Sample Input (hit hit miss hit ), Sample Output 110
'''

# ! We should ask him ever time hit or miss in while loop
points = 100
x = 4        ## nums of tries
while x > 0:
    actions = input()
    if actions == 'hit':
        points += 10     # ? deal with points , don't make hit and miss variables
            
    elif actions == 'miss':
        points -= 20
    x -= 1

print(points)


# NOTE : try do this 
'''
An example use case of continue:
An airline ticketing system needs to calculate the total cost for all tickets purchased. Tickets for children under the age of 3 are free. We can use a while loop to iterate through the list of passengers and calculate the total cost of their tickets. Here, the continue statement can be used to skip the children.
'''
# TODO: Ticket Prices
# [x]: Create a ticketing system that will output the total price for 5 passengers based on their age.

# [x]: The price of a single ticket is $100.
# [x]: For children under 3 years old, the ticket is free.
# [x]: Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
# NOTE: Sample Input ( 18, 24, 2, 5, 42)  Sample Output 400

total = 0
#your code goes here
# ! first take all 5 ages as inputs , int() type
x = int(input(''))
x1 = int(input(''))
x2 = int(input(''))
x3 = int(input(''))
x4 = int(input(''))

# ? make empty list , then add ages to it
ages2 = []
ages2.append(x)
ages2.append(x1)
ages2.append(x2)
ages2.append(x3)
ages2.append(x4)

# ! make your comparison in for loop on list
for age in ages2:
    #print(age)
    if age > 3:
        total += 100
    elif age <= 3:         # ? this == free $
        continue
print(total)



# TODO: Let's Count
# [ ]: Make a calculator that adds multiple numbers taken from input and outputs the result.
'''
You’re making a calculator that should add multiple numbers taken from input and output the result.
The number of inputs is variable and should stop when the user enters "stop".
Sample Input
4
32
6
stop
Sample Output 
42
Use an infinite loop to take user input and break it, if the input equals to "stop".
'''
sum = 0
while True:
    x = input()         # NOTE: we should put input in our loop
    if x == "stop":     #! ask ourself stop when?
       break
    else:               #? what we do if not stop
       sum += int(x)    #! some take the result of add and save it every time
print(sum)

# TODO: Do the math
# [x]: You’re making a calculator that should add multiple numbers taken from input and output the result.
# [x]: The number of inputs is variable and should stop when the user enters "stop".
# [x]: Use an infinite loop to take user input and break it, if the input equals to "stop".
# NOTE: Sample Input (4, 32, 6, stop) Sample Output (42)

sum = 0
while True:
   x = input()
    #! first ask about string , to stop or not
   if x == 'stop':
      break
    #? the VIP , we need change type of data when we decide to continue
   else:
      x_as_int = int(x)
      sum += x_as_int       ## to sum all numbers on loop
print(sum)


# TODO: Where is my seat?
# COMMENT: The seats in your ticketing program are stored in a 2D list. Each seat is assigned a letter code.
# [x]:Complete the program to take the seat row and column as input 
# [x]: and output the corresponding code from the list (row and column indices start from 0).
# NOTE: Sample Input (3, 2) Sample Output k


seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]

#your code goes here

row = int(input())
column = int(input())

seats_class = seats[row][column]
print(seats_class)

# TODO: Strings
# [ ]: Write a program that takes an input string and outputs the 3rd character of the string.

text = input()
print(text[2])



# TODO: Name, Please?
# [x]: Create a program that takes the first and last name of a person and output the initials.
# COMMENT: (first letters of the first and last name).
# NOTE: Sample Input (James, Smith) Sample Output (J.S.)

fname = input()
lname = input()
#your code goes here

print(f'{fname[0]}.{lname[0]}.')


# TODO: Take Your Seat
# [x]: Create your theater DataFrame and output the corresponding row.
# NOTE: Lists and strings share a lot of similarities - you can basically think of strings as lists of characters that can't be changed. 
num = [1,2,3]
num2 = [4, 5, 6]
print(num *3)
print(num + num2)

# TODO: Bingo
# [ ]: Given a list of numbers, output 'bingo' if it contains the input number.

items = [42, 88, 721, 12, 43, 22, 908]
user = int(input())             #! outside , enter only once
for x in range(len(items) + 1): #? make our loop for certain items on list
    #user = int(input())        # BUG: it cause asking every time
    if user in items :          #? is what user write in our list
        print('bingo')
        break                   #! without it infinty loop



# TODO: Just Say It
# COMMENT: Complete the program to make a voice recognition system.
# [x]:Complete the program to take a command as input.
# [x]:Check if it’s supported and output "OK", if it is, and "Not supported", if not.
# NOTE: Sample Input (Lights Off) Sample (Output OK)

commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]
#your code goes here

cmd = input()
if cmd == commands[0] or cmd == commands[1] or cmd == commands[2] or cmd == commands[3] or cmd == commands[4]:
    print('OK') 
else:
    print('Not supported')

##############################################################################
# NOTE:                      
#? use for loop as len()
text = 'btoo is good boy'
count_len = 0
for x in text:
    count_len += 1
print(count_len)
print(len(text))
##############################################################################
#? use for loop as index( ,to know how many time letters repeated)
text = 'btoo is good boy'
num_repeated = 0

for x in text:
    if (x == 'o'):          #! we use if condition on list then start our cala
        num_repeated += 1
print(num_repeated)
##############################################################################
# TODO: List Of Numbers
# [ ]: Given a list of numbers, calculate their sum using a for loop.
x = input()
z = x.split(' ')    #! convert string to list

sum = 0
for n in z:         #? for every item in a list
    sum += int(n)   #! adding intger to each other

print(sum)

# TODO: Let's Go Shopping!
# [x]: Create a program that will apply a discount to your shopping cart and output the total price.
# [x]: List of prices, and you need to add functionality to apply a discount and output the total price.
# [x]: Take the discount percentage as input, calculate and output the total price for the shopping cart.
# [x]: Use a for loop to iterate over the list.
# [x]: Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)

cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0

for item in cart:
    total_item = item - (item * (discount / 100) )  # NOTE: our math done on item not on cart list
    total += total_item                             # COMMENT: add all items together to get final result
    
print(total)


# TODO: Date Picker
# [ ]: You are making a date picker for a website and need to output all the years in a given period. 
'''
You are making a date picker for a website and need to output all the years in a given period. 
Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
The output sequence should start with the first input number and end with the second input number, without including it.

Sample Input
2005
2011

Sample Output 
[2005, 2006, 2007, 2008, 2009, 2010]
'''
x = int(input())            #! both valuables are intger , from first to second
y = int(input())

number = list(range(x,y))   #? make our range inside list to put every item in our new list
print(number)               #! don't forget we take our range, from user inputs

# TODO: Nearest Bathroom
# [x]: Create a program that takes the total number of floors as input and outputs the floors that have restrooms.
# [x]:A group of buildings have restrooms on every 5th floor.
# COMMENT: For example, a building with 12 floors has restrooms on the 5th and 10th floors.
# NOTE: Sample Input (23)  Sample Output (5, 10, 15, 20)


n = int(input())
#your code goes here

for floor_restroom in range(5,n + 1 ,5):  #! we start from first included , and user input should add  1 
    print(floor_restroom)                 #? because index strt with 0 

##############################################################################

#? range item to list
nums = list(range(10))  #! VIP NOTES
print(nums)

#?  create a list of decreasing numbers, using a negative number as the third argument. 
nums = list(range(10 , 2 , -1))
print(nums)

#? You can use ranges in for loops, without the need to convert them into lists. 
for i in range(10):
    print(i)
##############################################################################
#! backward slices
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
#! reverse a list.[::-1]
print(sqs[::-1])
#! delete first and last [1:-1]
print(sqs[1:-1])
##############################################################################
# TODO: The Last Character
# [ ]: Write a program that takes a string as input and outputs the last character of that string.

text = input()
print(text[-1])



# TODO: Flip The String
# [ ]: Given a string as input, output its reverse. 
# NOTE: Sample Input hello world , Sample Output dlrow olleh
#! Remember, a string is a list of characters, and you can reverse a string the same way you would reverse a list.

#? deal string as list when try do slicsing
string = input()
reverse = string[::-1]
print(reverse)

#+========================================+
print('='*60)
print( '*'*20 + '**Function*' + '*'*20 )
print('='*60)
#+========================================+

'''
# NOTE: insert, adding to certain place
insert() inserts a new item at the given position in the list:
The first argument is the position index, while the second parameter 
is the item to insert at that position.
'''
x = [1,2,2,5]
x.insert(2,6)
print(x)
##############################################################################

# NOTE: index, find first  occurrence of a list item and returns its index. 
x = ['s',8,88]
s = 'bro bro'
print(x.index(88))
print(s.index('r'))
print(x.count(8))           #! count(item) == to tell as how many times it repeat in list or string
print(s.count('o'))
##############################################################################
# NOTE : join change list to string
# join() joins a list of strings with another string as a separator. 
x = " ".join(['a','b','c'])
   #? "what is separator between strings".join(['strings'])
print(x)
print(type(x))          # str
##############################################################################

# NOTE: split change string to list
x = "some text goes here"
y = x.split(' ')
print(type(y))          # list
print(x[2])             # in str = m
print(y[2])             # in our new list = goes
z = x.replace('!','.')
print(z)
##############################################################################

# TODO: Analyze to realize
# [ ]: 
'''
Complete the code to remove the smallest and largest elements from the list and output the sum of the remaining numbers.
I’m very lost. Having trouble from the lesson on how to pull the min and max and get rid of them let alone add it all up after. 
'''
data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

x = max(data)
z = min(data)
#l = len(data)
#print(l)

data.remove(z)     #! remove what we get from max and min functions
data.remove(x)

#ll =len(data)
#print(ll)

#sum(data)  #BUG: sum the remaining
#print(total)

# TODO: Shouting text
# [ ]: make function add !!! to end of text

text = input()
def shouting():
    print(text + ' !!!')

shouting()


# TODO: Queue Management
# [ ]: Write a program to take an input, add it to the end of the queue and output the resulting list for a queue management system.
'''
You are working on a queue management program.
The queue is represented by a list.
Note: The append() method can be used to add new items to the list.
'''
queue = ["John", "James", "Amy"]
txt = input()

add = queue.append(txt)
print(queue)

# TODO: Remaining Numbers
# [ ]: Complete the code to remove the smallest and largest elements from the list and output the sum of the remaining numbers.
# COMMENT: same to Analyze to realize



# TODO: Broken Keyboard
# [ ]: Replace all of the # characters with spaces and output the result.
text = 'Hello#btoo#!!'

change = text.replace('#'," ")
print(change)

# TODO: Stop Shouting!
# [ ]: Write a program to convert uppercase to lowercase. 
def convert_lower():
    print(input().lower())

convert_lower()

# TODO: Welcome, Sololearner!
# [ ]: Redesign the given function so that it will take the given input as the name of the user and output the welcome message with it.
'''
My code keeps outputting welcome, user instead of welcome , and the input 

'''
def welcome_message():
	#redesign this function
	user= input()
	print(f"Welcome, {user}")
welcome_message()

# TODO: Call The Function
# [ ]: Take user input and call the function by passing the input as its argument. 
def welcome_message2():
	#redesign this function
	user= input()
	print(f"Welcome, {user}")
welcome_message2()


# TODO: From Feet To Inches
# [ ]: Make a function that will convert a foot value to inches.
"""
You need to make a function that converts a foot value to inches. 
1 foot has 12 inches. Define a convert() function, 
that takes the foot value as argument and outputs the inches value.
 —————— Lost here again as it doesn’t explain well how to set and use the convert variable in the lesson.
"""
def convert(foot):
    inches = foot * 12
    print(inches)

convert(5)



############################################################
# NOTE: The returned value can be used later in the code
'''
Returning is useful when you don't need to print the result of the function, 
but need to use it in your code. For example, a bank account's withdraw() function 
could return the remaining balance of the account. 
'''

# NOTE: A function can only return once, thus, if you need to return multiple values, you can use a list. 
def double(a, b):
    return [a*2 , b*2]          #! to return multiple values , put them on list [ V1 , V2 ...]

x = double(6, 9)
print(x)
##############################################################################
# TODO: Area Of A Rectangle
# [ ]: Calculate the area of the rectangle through function arguments.
# # base /2 * h or (base * h) / 2
# base = 8
# h = 8
# x = (base / 2) * h 
# print(x)

# xx = (base * h) / 2
# print(xx)

def triangle_area(base,height):
    area = (base / 2) * height
    print(area)

triangle_area(8,8)

# TODO: How Many Letters?
# [ ]: Write a function that will return the count of the letter in the string.
"""
Write a function that takes a string and a letter as its arguments 
and returns the count of the letter in the string. Sample Input hello, 
how are you? o Sample Output 3 Explanation: The letter o appears 3 times in the given text.
"""
#write text then write which letter want to know it
#your final code would be text.count(by using this letter repeated)

def nums_letters():
    text = input()
    user = input()
    x = text.count(user)
    print(x)
nums_letters()


# NOTE: docstrings
'''
Unlike conventional comments, docstrings are retained throughout the runtime of the program. 
This allows the programmer to inspect these comments at run time. 
'''
def print_nums(x):
    for i in range(x):
        print(i)
        return          ## empty return == #! stop function

print_nums(10)          #? == 0