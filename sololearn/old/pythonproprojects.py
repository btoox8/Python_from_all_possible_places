#***Basic***
# 1:
print("Hello, World!")

# 2:
# Python3 program to add two numbers 
  
num1 = 15
num2 = 12
  
# Adding two nos 
sum = num1 + num2 
  
# printing values 
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))

# 3:
# Python program to find the 
# maximum of two numbers 
  
  
def maximum(a, b): 
      
    if a >= b: 
        return a 
    else: 
        return b 
      
# Driver code 
a = 2
b = 4
print(maximum(a, b))


# 4:
# Python 3 program to find   
# factorial of given number 
def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 
  
# Driver Code 
num = 5; 
print("Factorial of",num,"is", 
factorial(num)) 

# 5:

# Python3 program to find simple interest 
# for given principal amount, time and 
# rate of interest. 
  
  
def simple_interest(p,t,r): 
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r) 
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si) 
    return si 
      
# Driver code 
simple_interest(8, 6, 8) 
# 6:
# User enters the number
number = int(input("Enter number: "))

# checking the number
if number < 0: print("The entered number is negative.") 
elif number > 0:
    print("The entered number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("The input is not a number")

# 7:
# Store input numbers:  
num1 = input('Enter first number: ')  
num2 = input('Enter second number: ')  
  
# Add two numbers  
sum = float(num1) + float(num2)  
# Subtract two numbers  
min = float(num1) - float(num2)  
# Multiply two numbers  
mul = float(num1) * float(num2)  
#Divide two numbers  
div = float(num1) / float(num2)  
# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div))  

# 8:
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)  

# 9:
#import complex math module  
import cmath

a = float (input ('Enter a: '))
b = float (input ('Enter b: '))
c = float (input ('Enter c: '))
 
#calculate the discriminant
d = (b ** 2) - (4 * a * c)
 
#find two solutions
sol1 = (-b - cmath.sqrt (d)) / (2 * a)
sol2 = (-b + cmath.sqrt (d)) / (2 * a)
print ('The solution are {0} and {1}'.format (sol1, sol2))


# 10:
# Python swap program   
x = input('Enter value of x: ')  
y = input('Enter value of y: ')  
  
# create a temporary variable and swap the values  
temp = x  
x = y  
y = temp  
  
print('The value of x after swapping: {}'.format(x))  
print('The value of y after swapping: {}'.format(y))


# 11:
# Python program to find Area of a circle 
  
def findArea(r): 
    PI = 3.142
    return PI * (r*r); 
  
# Driver method 
print("Area is %.6f" % findArea(5)); 

# 12:

# taking user input
ch = input("Enter a character: ")
dict={'a','e','i','o','u','A','E','I','O','U'}

if ch in dict:
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")




