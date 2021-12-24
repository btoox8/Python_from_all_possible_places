# TODO: 1. Flight Time

# [x]: You need to calculate the flight time of an upcoming trip. 
# ! You are flying from LA to Sydney, covering a distance of 7425 miles, 
# ? the plane flies at an average speed of 550 miles an hour.
# NOTE: Calculate and output the total flight time in hours. 
# COMMENT: The result should be a float. 

distance = 7425
average_speed = 550
total_flight_time_per_hour = distance / average_speed
print(total_flight_time_per_hour)

# TODO : 2.
# [x]: You need to make a program for a leaderboard.
# NOTE :The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
'''
1.
2.
3.
... 
'''
for x in range(1,10):
    print(f'{x}.')
    
# TODO: 3. Tip Calculator
# [x]: You always tip 20% of the bill amount.You’re making a program to calculate tips and save some time.
# [x]: Your program needs to take the bill amount as input and output the tip as a float.
# NOTE : Sample Input:  50 , Sample Output : 10.0 

bill = float(input("You're bill amount : $"))
tip = (20/100) * bill
print(tip)
## others ##
total_bill = bill + tip
print(total_bill)

# TODO: 4. BMI Calculator
'''
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²
The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more
Let’s make finding out your BMI quicker and easier, by creating a program 
that takes a person's weight and height as input and outputs the corresponding BMI category.
# NOTE: Sample Input 85, 1.9 Sample Output Normal
#! Weight is in kg, height is in meters.
#! Note, that height is a float. 
'''

#your code goes here

weight = float(input())
height = float(input())
bmi = weight / height ** 2
#print(bmi)

## 85 , 1.9  = normal

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obesity')

# TODO : 5. Sum of Consecutive Numbers
# [ ]:
'''
No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.
Let’s save some time by creating a program to do the calculation for you!
Take a number N as input and output the sum of all numbers from 1 to N (including N).
# NOTE: Sample Input 100 Sample Output 5050
#! Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
#! You can iterate over a range and calculate the sum of all numbers in the range.
#! Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.
'''

N = int(input())                #! num by user to br the last of our range
#your code goes here
sum = 0                         #? should start sum with zero out of our  loop
for num in range(1, N + 1):
    sum  += num
print(sum)

# TODO: Search Engine
# NOTE: 
'''
You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
Define the search() function, so that the given code works as expected.
'''

text = input()
word = input()


def search(text,word):
    #! if I can count word in tect == it's true == return (1)
    x = text.count(word)
    if x == 1:          #? if true , we found it
        return "Word found "
    else:
        return 'Word not found'

print(search(text, word))