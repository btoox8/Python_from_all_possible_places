#Pure gold
"""
You’re making a gold purity checker, that should accept only 22K or 24K gold. Only the good stuff!

22K gold has 91.7% or more gold in it, while 24K corresponds to 99.9% and above purity.

Given the % of gold purity as input, you should output "Accepted" only if it corresponds to 22 or 24K.

Sample Input:
93.4

Sample Output:
Accepted
"""
print("#Welcome in gold cheaker#")
gold_purity = float(input("Enter your purtiy % :\n"))

x = gold_purity
print(str(x) + '%')
if x < 91.7:
    print("Not Accepted ")
elif x > 91.7:
    if x >= 91.7 and x < 99.9:
        print("Accepted")
        print("22K")
    else:
        print("24K")
#Leap year
"""
True for / 4 and 400 but skip 100
"""

year = int(input("Enter the year here! \n"))

if year % 4 == 0 and year % 100 != 0:
    print("leap year")
elif year % 400 == 0:
    print("leap year")
elif year % 100 ==0 :
    print('not a leap year')
    print('skip it due to 100 years')
else:
    print("not a leap year")
    
#My example
# Arabic flags posibility

a = input('first color\t')
b = input('second color\t')
c = input('third color\t')
d = input('forth color\t')
print('_______________')
'''
a = first_color
b = second_color
c = third_color
d = forth_color
'''

if (a == ('green') or( 'red '))and b == 'white' and c == 'black' and (d ==('green') or( 'red')):
    print('Sudan or Palastain')
else:
    print('not found')
    
#24k magic
# advance gold cheaker 

print("Welcome in gold chwaker v.2")
purity = float(input("Enter your purity in % \t")) 
#notice we use one condition without and statement, because we start first if statment with largest value, then go down

if purity >= 99.99: 
   print("24K") 
elif purity >= 91.7:
   print("22K") 
elif purity >= 83.3: 
   print("20K") 
elif purity >= 75.0: 
    print("18K")
    
## we can use it with and....
print("Welcome in gold chwaker v.2")
purity = float(input("Enter your purity in % \t")) 

if purity >= 99.99: 
   print("24K") 
elif purity >= 91.7 and purity < 99.9:
   print("22K") 
elif purity >= 83.3 and purity < 91.7: 
   print("20K") 
elif purity >= 75.0 and purity < 83.3: 
    print("18K")
    

#My example
grade = int(input("Enter your score to show which grade you have... \t"))

if grade > 90:
    print("A")
elif grade > 80:
    print("B+")
elif grade > 70:
    print("B")
elif grade > 60:
    print("C+")
elif grade > 50:
    print("C")
else:
    print("F")

#Odd or even

x = 4 # start from here

while x <=20:
    x += 1 # increase by
    if x%2 == 0:
        print(str(x) + ' is even number')
    else:
        print(str(x) + ' is odd number')

#Pull the tiger

"""
You are making a game! The player tries to shoot an object and can hit or miss it. The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points. Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.
 Sample Input hit hit miss hit 
 Sample Output 110 
"""
print('Write hit or miss...')
shots = int(input('How many times you want shot it...\n')) # number of our trail
score = int(input('Start from which score...\n')) #our score start from here
print('score start ' + str(score))
while shots > 0: # our condition for loop, while go to shofs number which we write it in our variable
    result = input() # make new variable to write inside it our result to use it by our sentences
    if result == "hit": # if it happen + and -
        score +=10
        shots -=1
    elif result == "miss":
        score -=20
        shots -=1
print("You final score is " + str(
score))

#need to more explain

i = 0
x = 0
while i < 4:
    x += i  # x 0 1 2 3
    i += 1 # i 1 2 3 3
    
print(x)


i = 0
x = 0
while i < 4:
    x = x + i  # x 0 1 3 6
    i = i +1 #     i 1 2 3 4
print('i = ' +str(i))    
print('x = ' + str(x))

#Do the math

sum = 0
while True: #infinity loop
   x = input() #enter whole number you want to adds
   #your code goes here
   if x == "stop" :
          break
   sum +=int(x) #should be int
   #result not appear inspite of stopping 
print(sum)

#my minus
minus = 100
while True: # True not true
    m = input()
    
    if m == "S":
        break
    minus -= int(m)
    # press S to show finall result
print(minus)

#my *

multi = 1 # should be (1) we * in our final result

while True:
    mu = input()
    
    if mu == 'end':
        break
    multi *= int(mu)
print(multi)
    
#BMI calculare
"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
"""
print("BMI calculater")
weight = float(input("Enter your weight in kg: \n"))

height = float(input("Enter your height in meter : \n"))

bmi = weight / (height**2)
#if want use cm inspite of meter
# bmi = weight / ((height/100)**2)

print("Your BMI ratio :\t" + str(bmi))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25 :
    print('Overweight')
elif bmi >= 18.5:
    print('Normal')
elif bmi <18.5:
    print('Underweight')
print('*_*')

#explain important things about lists
m = [
[1,2,3],
[4,5,6]
]

print(m[0][1]) # it mean go [0] first list, [1] and take element inside index (1)
print(m [1][2])

#Where is my seat
'''Try this one, works for me:
(Here r stands for row and c for columns.) '''
seats = [
['a', 'b', 'c'],
['d', 'e', 'f'],
['g', 'h', 'i'],
['j', 'k', 'l']
]
# highest value r = 3 and cols 2
r = int(input('Your row number\t'))
c = int(input('Your col number\t'))
print('Your class will be: ')
print(seats[r][c])

#some information
# list with add and multi as same as String
nums = [1, 2, 3]
print(nums + [4, 5, 6])
# add list to another make one contain all elements
print(nums * 3)
#repeat elements inside only one list

#Name , place?

first_name = input('Enter your first name...\n')
last_name = input('Entee your last name...\n')

x = list(first_name)
y = list(last_name)
print(str.upper(x[0]),'.',str.upper(y[0]))

# in and not in usage with list
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
print("onion" not in words)
print(not "onion" in words)

# Just say it
print('we have 5 orders you can check it down')
list1 = ['Lights Off', 'Lock the door', 'Open the door', 'Make Coffee', 'Shut down']

y = list1
our_order = input()
x = our_order

if x in y:
    print('OK')
else:
    print("Not supported")
   
print('Which langague I know it, try guess')

my_lang = [
'arabic','english','html','js','python','css','dart'
]

lang = input('Enter lang here\t')
print('___________')

if lang in my_lang:
    print('Correct !!')
    print('my lang is ')
    print(lang)
else:
    print('I can\'t guess it')
    

## example about for loop
list = [1,2,3,4]

for x in list : #take elements one by one
    print(x + 1)
##    
str = ('welcome')
count = 0

for s in str:#take letters one by one
    if (s=='l'):
        count+=1 #link between two variables
print(count)

#Let's go shopping
'''
You’re making a shopping cart program.

The shopping cart is declared as a list of prices, and you need to add functionality to apply a discount and output the total price.

Take the discount percentage as input, calculate and output the total price for the shopping cart.

Use a for loop to iterate over the list. 
Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)
'''

cart = [15, 42, 120, 9, 5, 380]

discount = int(input('Enter your discount%'))
total = 0

for item in cart:
    #print(item)
    #print(cart)
    total += item - (item * discount/100)
    #you should notice total about only element, for every time, it mean total for 15 , then 42.....380
    #every item pass through this process till end and go to next till final one , to make our total
    print(total)
    
#range
x = list(range(10))
y = list(range(5,10))
z = list(range(5,10,2))
v = list(range(10,5,-1))
#if write 
# n = list(range(5,10,-1))
# it []

print(x)
print(y)
print(z)
print(v)



#Nearest bathroom
""""
A group of buildings have restrooms on every 5th floor.
For example, a building with 12 floors has restrooms on the 5th and 10th floors. 

Create a program that takes the total number of floors as input and outputs the floors that have restrooms.

Sample Input
23
)
Sample Output
5
10
15
20
"""

#n == number of total floor, start with 5 due to it first restroom place, and increase by 5 , because it how much we should adding to it every time
#n+1 to make last floor inside our range
n = int(input('Enter number of floors\t')) 
n = list(range(5,n+1, 5)) 
print(n)

#another way to answer
n = int(input('Enter number of floors\t'))
for n in range(5,n+1,5): # look we use variable in range
    print(n)

#Flip the string
x =  list(input('your writing will extract as reverse list\t'))
y = input('your writing will extract as reverse string\t ')
print(x[::-1])
print(y[::-1])

# Sum of Consecutive number

"""
No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
"""

input = int(input())
output = sum(range(0,x+1)) #sum of our range
print(output)


