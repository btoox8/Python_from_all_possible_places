#projects from basic python lesson

#your first program
#brain freez

""""
Today is a holiday at the children's camp, so all the children will be served ice cream.
There are 3 groups of children: 23 children in the first group, 27 in the second, and 18 in the third. 
Every child should get 2 scoops of ice cream. 
Write a program to calculate and output the total number of ice cream scoops we need.
"""
print((23*2) + (27*2) + (18*2))


#textbooks for students

"""
We need to distribute math and history textbooks to students.
There are 2 class sections: the first section has 18 pupils, and the second one has 19. 
The total number of books available for distribution is 76.
Write a program to calculate and output how many books will be left after each student receives both books.
"""
room_1 = 18
room_2 = 19
total_books = 76
# every student should take 2 mandatory books

print((total_books) - ((room_1 + room_2)* 2))

   ##or##
total_taken = ((room_1 + room_2)* 2)
print(total_books - total_taken)


##exponentiation
"""
Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days 
(the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling 
to understand which choice results in a larger amount.

Hint:
Let's see how exponentiation can be useful to perform the calculation.
For example, if we want to calculate how much money we will have on the 5th day, 
we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).
"""

#your money *(how many times duplicate * how many days that duplicate take place)
print(0.01*(2**30))
print(1*(2**30))

print(0.10*(7**4))
print(1000000*(2**5))

stuff_cost = 10000000
percent_of_duplicate = 0.5     # = % 50
number_of_time_of_duplicate = 2
total_reading = (stuff_cost*(percent_of_duplicate**number_of_time_of_duplicate))
print(total_reading)
#find the bug

print("btoo said:\"welcome every one\"to 'my new house'")

#more lines,more better

"""
The given code outputs A B C D (each letter is separated by a space).
Modify the code to output each letter on a separate line, resulting in the following output:
A
B
C
D 
"""

print("""
A
B
C
D
""")
   ##OR##
print("A\nB\nC\nD") # should not saprated \n from starting of next line


#string operations
print(input() *  3 + '!' )   ## we can use input inside print
  #every thing inside input() is string
print(input("Enter hi or hello") * 2 + "where are you from \t" + "I\"m from \t" + input("Enter your country"))  
 
#fun with expontents

base = 5
expontent = 2
result = base ** expontent 
print(result)

##calculate expontent 
print("Welcome, calculate expontent  ")
base = int(input("Enter your base number"))
expontent = int(input("Enter , raised to power *** times"))
result = base ** expontent 
print(result)

  ##power function##

# it write like this 
# pow(base, exponent)
print(pow(2,2))





#product of integers
##3.6 == 3 times repeat 6 == 6+6+6 = 18
##or 3(5) = 5+5+5 = 15
#+*+ = + and -*- = +

product_1 = 2
product_2 = 3
output = product_1 * product_2 
print(output)

##simple calculator
  #make simple adding values
first= int(input("Your first Number\t"))
second = int(input("Your second Number\t"))
adds_result = first + second
print(adds_result)

#at the boilong point!

"""
Write a program that checks if the water is boiling.
Take the inter temperature in Celsius as input and output "Boiling" if the temperature is above or equal 100.
! Do not output anything if the water is not boiling.
"""

temp = int(input("The temperature\t"))

if temp >= 100:
    print("Boiling")

#club bouncer code

"""
Getting a line 5 syntax error at name in the if statement

"""
name = input("Enter your name\t")
age = int(input("Enter your age\t"))

if age>= 18:
    print ("Welcome" + name)
else:
    print ("Sorry")
    
#my driving 

print("welcome, sudan driving licence")
print("Enter your personal,information , to know if you can take the exam...")

name = input("Enter your name\t")
age = int(input("Enter your age\t"))

if age >= 18:
    print("Yes, " + name + " you can enroll. Your age is " + str(age))
else:
    print("Sorry, become when you reach to 18")
print("See you as soon as possible")


#To pythagoras or not to pythagoras
"""
Else Statement
Pythagoras theorem says: In a right-angled triangle, the square of the hypotenuse side 
is equal to the sum of squares of the other two sides.
Write a program that takes lengths of triangle sides as inputs, and output whether our triangle is right-angled or not. 
If the triangle is right-angled, the program should output "Right-angled", and "Not right-angled" if it's not.
Sample Input
3
4
7
Sample Output
Not right-angled
[Take the 3rd input (side3 variable in sample code) as the longest side, 
which will represent the hypotenuse if the triangle is right-angled.

"""
side1 = int(input("first side\t"))
side2 = int(input("second side\t"))
side3 = int(input("third side\t"))
#your code goes here
#print(side1**2)
#print(side2**2)
#print((side1**2)+(side2**2))
#print(side3**2)
if ((side1**2) + (side2**2)) == (side3**2):
    print("Right-angled")
else:
    print("Not right-angled")

#organized robot
"""
Write a program that will be used in a robot that categorizes items by their color.
Each color corresponds to a box with a specific number.
For simplicity, our program will handle 3 colors:

red goes to box #1
green goes to box #2
black goes to box #3

Your program needs to take a color as input and output the corresponding box number.

Sample Input
green

Sample Output
2
"""
color = input("color may: red, green, black\t")

if color == "red" :
    print("goes to box #1")
elif color == "green":
    print("goes to box #2")
else:
    print("goes to box #3")




#depending on parity

"""
Write a program that takes a number as input and
- returns its double, if the number is even
- returns its triple, if the number is odd
- returns 0, if number is 0

Sample Input:
1

Sample Output:
3

An integer is even if it is divisible by two and odd if it is not even.

"""
number = int(input("Enter your number\t"))
if number %2 ==0: #even
    print(number**2) # may 2*number
elif number %2 != 0:
    print(number*3)
elif number == 0: # don't forget use == nit only =.
    print(number)
print("ollla")

#store is closed
   ## our store open inly 5 days and for 21 hours on it ##
   

hour = int(input())
 day = int(input())
if (10 < hour < 21) and day < 6:
    print("Open")
    
    

#boolean age groups
"""
Given the age of a person as input, you need to output their age group.
Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64
Senior: 65+


 Example- input = 15
Output = teen
"""
age = int(input("Enter your age \t"))

if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 12:
    print("Teen")
else:
    print("Child")


#tuition discounts
"""
plss
the problem is:
The university gives students discounts on tuition fees depending on their performance: 
90-100 => 50% 
80-89 => 30% 
70-79 => 10% 
0-69 => 0% 
Write a program that will take the scores from the first and second semesters, 
then calculate the average score, and output the result, depending on the score. 

Sample Input 
67 
83 


Sample Output 
10

"""
sem_1 = int(input("Enter your first semester result..\t"))
sem_2 = int(input("Enter your second semester result..\t"))
avarage = (sem_1 + sem_2 ) /2

if avarage >= 90:
    print("50%")
elif avarage >= 80:
    print("30%")
elif avarage >= 70:
    print("10%")
else:
    print("0%")


#fruit vending machine
"""
 Im referring to the fruit vending machine challenge in python where user inputs number and a fruit name is shown. 7 fruits.


"""

fruits = ["orange","bananna",'pinapple',"watermallon",'apple',"kiwi","tomato"]
num = int(input("Enter number between 1 to 7 to choose your fruits...\t"))

if 0 <= num <= 7: # here your entry two conditions
    print(fruits[num - 1]) # to take same place not index place
else:
    print("Wrong number")

#every third character
  ##delete every third place
  # we need convert our input to list, not string
  
word = list(input())

word = list(input())
del word [0: :3] # delete every third but start by deleting first place
''.join(word)
print(word)


#list operations


nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5 # that mean
  ## index (0) replace it by value index(1) - 5 so replace 10 by 4
if 4 in nums:
  print(nums[3])
else:
  print(nums[4])


#build a search engine

"""
You do not need to build a list. 
The program is passing a string in the line:
s = input()
In this exercise this string is ‘the list’.
Therefore it is within this string that you need to search for the character “a”. 

Something like this should work: 
"""
text = input("Enter your text\t")
if "a" in text:
 print("Match")
else:
 print("No match")
 
  ##other##.from certain words
  
text_1 = input("Enter your text\t")
words = ["Btoo","mohamed","ahmed"]
if text_1 in words : 
    print ("Match") 
else : 
    print ("No match")
  
#bingo

#queue management



#minimum and maximum


#the middle element


#call it even



#summing digits


#infinite loops

#free stuff!



#iteration

#date picker


##fizzbuzz



#welcome sololearn




#matching passwords


#area of a rectangle


#hashtag generator

#No dice? No problem


#circle dimension

##celsius to fahrenheit converter

