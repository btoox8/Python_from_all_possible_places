# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random
print(random)
print(f"Print Random Float Number {random.random()}")

# Show All Functions Inside Module
print(dir(random))

# Import One Or Two Functions From Module
from random import randint, random
print(f"Print Random Float {random()}")
print(f"Print Random Integer {randint(100, 900)}")

# -----------------------------------
# -- Modules => Create Your Module --
# -----------------------------------

import sys
sys.path.append(r"D:\Games")
print(sys.path)

import elzero
print(dir(elzero))

elzero.sayHello("Ahmed")
elzero.sayHello("Osama")
elzero.sayHello("Mohamed")

elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Osama")
elzero.sayHowAreYou("Mohamed")

# Alias

import elzero as ee

ee.sayHello("Ahmed")
ee.sayHello("Osama")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Osama")
ee.sayHowAreYou("Mohamed")

from elzero import sayHello

sayHello("Osama")

from elzero import sayHello as ss

ss("Osama")


# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("Elzero"))
print(termcolor.colored("Elzero", color="yellow"))

print(termcolor.colored(pyfiglet.figlet_format("Elzero"), color="yellow"))


# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1982, 10, 25))
print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

print("#" * 40)

myBirthDay = datetime.datetime(1982, 10, 25)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthDay} And ", end="")
print(f"Date Now Is {dateNow}")

print(f" I Lived For {dateNow - myBirthDay}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")

# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))

# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

myString = "Osama"

myList = [1, 2, 3, 4, 5]

for letter in myString:

  print(letter, end=" ")

for number in myList:

  print(number, end=" ")

myIterator = iter(myString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

for letter in iter("Elzero"):

  print(letter, end=" ")

# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():
  yield 1
  yield 2
  yield 3
  yield 4

myGen = myGenerator()

print(next(myGen), end=" ")
print("Hello From Python")
print(next(myGen), end=" ")

for number in myGen:
  print(number)


# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

def myDecorator(func):  # Decorator

  def nestedFunc():  # Any Name Its Just For Decoration

    print("Before")  # Message From Decorator

    func()  # Execute Function

    print("After")  # Message From Decorator

  return nestedFunc  # Return All Data

@myDecorator

def sayHello():

  print("Hello From Say Hello Function")

@myDecorator

def sayHowAreYou():

  print("Hello From Say How Are You Function")

afterDecoration = myDecorator(sayHello)

afterDecoration()

sayHello()

print("#" * 50)

sayHowAreYou()

# --------------------------------------------
# -- Decorators => Function With Parameters --
# --------------------------------------------

def myDecorator(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    if num1 < 0 or num2 < 0:

      print("Beware One Of The Numbers Is Less Than Zero")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

def myDecoratorTwo(func):  # Decorator

  def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

    print("Coming From Decorator Two")

    func(num1, num2)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator
@myDecoratorTwo

def calculate(n1, n2):

  print(n1 + n2)

calculate(-5, 90)


# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

def myDecorator(func):  # Decorator

  def nestedFunc(*numbers):  # Any Name Its Just For Decoration

    for number in numbers:

      if number < 0:

        print("Beware One Of The Numbers Is Less Than Zero")

    func(*numbers)  # Execute Function

  return nestedFunc  # Return All Data

@myDecorator

def calculate(n1, n2, n3, n4):

  print(n1 + n2 + n3 + n4)

calculate(-5, 90, 50, 150)

def speedTest(func):

  def wrapper():

    start = time()

    func()

    end = time()

    print(f"Function Running Time Is: {end - start}")

  return wrapper

@speedTest

def bigLoop():

  for number in range(1, 20000):

    print(number)

bigLoop()

'''

    
  
    Python Generators
    Python Decorators Use Cases
    Python Date Formatting

'''