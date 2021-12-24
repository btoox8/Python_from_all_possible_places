#//__ Unit one __// Hello Python >_<

#-- Introduction to programming --#

# a computer program is a recipe of instructions that tells your computer what to do.
# syntax is the rules for how a sentence is constructed while semantics refers to the actual meaning of the statements.
# In a programming language like Python, the syntax is the rules for how each instruction is written and the semantics is the effects the instructions have.
# In general, you can think of scripts as programs with a short development cycle that can be created and deployed rapidly.
# In other words, a script is a program that is short, simple, and can be written very quickly.


# Automation is the process of replacing a manual step with one that happens automatically.
# Instead, people can concentrate on more complex, creative, or difficult tasks like focusing on where you're driving.
# a human performing the same tasks hundreds of times will never be as consistent as a machine doing the same thing.
# For example, they may require a degree of creativity or flexibility that automatic systems can't provide or for more complicated or less frequently executed tasks creating the automation may actually be more effort or cost than it's worth.
# Automation is a powerful tool when used in the right place at the right moment.
# It can save time, reduce errors, increase consistency, and provide a way to centralized solutions and mistakes making them easier to fix.


# Tasks performed by a computer that need to be done multiple times with little variation are really well suited for automation, because when you automate a task you avoid the possibility of human errors, and  reduce the time it takes to do it.
# TODO: take emails not allow repilcate and print message to every one by them name and compan name.

#-- Introduction to python --#

# In programming, an interpreter is the program that reads and executes code.
# the Python interpreter is the program that reads what is in the recipe and translates it into instructions for your computer to follow.
# The more you see failure or broken code as an opportunity to learn, the quicker you'll master programming.
# A nice feature of learning the basics of programming in one language is that you can generally apply the same concepts you learn to other languages.


#-- Hello world --#

# Keywords are reserved words that are used to construct instructions.
# In programming, any text that isn't inside quotation marks is considered part of the code.
# We are going to make Python our calculator.

#-- Module review --#

# Margarita Manterola.


#-- Notes --#
If your syntax is correct, but the script has unexpected behavior or output, this may be due to a semantic problem.


#-- Assessment --#


What’s a computer program?
- A list of instructions that the computer has to follow to reach a goal 

What’s the syntax of a language?
- The rules of how to express things in that language 

What’s the difference between a program and a script?
- There’s not much difference, but scripts are usually simpler and shorter. 

Which of these scenarios are good candidates for automation? Select all that apply.
-  Generating a sales report, split by region and product type 
-  Helping a user who’s having network troubles 
-  Copying a file to all computers in a company 
-  Sending personalized emails to subscribers of your website 

What are semantics when applied to programming code and pseudocode?
- The effect the programming instructions have 

Python is an example of what type of programming language?
- General purpose scripting language 

What are functions in Python?
- Functions are pieces of code that perform a unit of work. 

What are keywords in Python?
- Keywords are reserved words that are used to construct instructions. 

What does the print function do in Python?
- The print function outputs messages to the screen 

What is a computer program?
- A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer. 

What’s automation?
- The process of replacing a manual step with one that happens automatically. 

Which of the following tasks are good candidates for automation? Check all that apply.
- Creating a report of how much each sales person has sold in the last month. 
- Setting the home directory and access permissions for new employees joining your company. 
- Populating your company's e-commerce site with the latest products in the catalog. 

What are some characteristics of the Python programming language? Check all that apply.
- The Python interpreter reads our code and transforms it into computer instructions. 
- Python programs are easy to write and understand. 
- We can practice Python using web interpreters or codepads as well as executing it locally. 


How does Python compare to other programming languages?
- Each programming language has its advantages and disadvantages. 
 

#//__ Unit tow __// Basic Python Syntax >_<

#-- Expressions and variables --#

# like an integer which represents whole numbers without a fraction, like one, and float, which represents real numbers or in other words, a number with a fractional part like 2.5.
# Read the errors carefully, understand what they're telling you, and then use that new knowledge to help you fix the mistake.
# If you're ever not 100 percent sure what data types a certain value is, Python gives you a handy way to find out. You can use the type function, to have the computer tell you the type.
# Variables are names that we give to certain values in our programs.
# When you create a variable in your code, your computer reserves a chunk of its own memory to store that value.
# The process of storing a value inside a variable is called assignment.
# Generally, you can name variables whatever you like but there are some restrictions.
# (int + float) , Behind the scenes the computer is busy automatically converting our integer into a float. We call this process, implicit conversion : The interpreter automatically converts one data type into another.
# combine a string and a number, is it possible? It sure is but only with an explicit conversion.
# Explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to.


#-- Functions --#

# how to define our own functions to tell the computer to do things that the language is built-in functions don't.
# But what about getting values out of a function? This is where the concept of return values comes to play.
# [return] It allows us to combine calls to functions and to more complex operations which makes your code more reusable.
# Python are even more interesting because we can use them to return more than one value.
# That double slash operator is called floor division.
# None is a very special data type in Python used to indicate that things are empty or that they return nothing [ not write return on def part ].
# The result of the function is still the same, no matter where the parameters come from.
# Imagine having to rewrite your own code because it's too messy to understand.
# First off, you want your code to be self-documenting as possible.
# In programming lingo, when we re-write code to be more self-documenting, we call this process refactoring.
# you can add a bit of explanatory texts to the code.
# Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits.  


#-- Conditionals --#

# These operators allow you to connect multiple statements together and perform more complex comparisons. 
# may say (1 == '1') but I can't (2 > '2')
# In Python the logical operators are the words and, or, and not.
# Here we're comparing strings, and the bigger and smaller operators refer to alphabetical order.
# string small > capital letter.
# The body of the if block will only execute when the condition evaluates to true; otherwise, it skipped.
# The condition must be true for the body of the elif block to be executed.
# The main difference between elif and if statements is we can only write an elif block as a companion to an if block
# That's because the condition of the elif statement will only be checked if the condition of the if statement wasn't true.
# We can use return instead of else on our function !!
# We can use the concept of branching to have our code alter its execution sequence depending on the values of variables. 
# We just covered the if statement, which executes code if an evaluation is true and skips the code if it’s false. 
#

#-- Module_review --#

# 


#-- Notes --#

# 


#-- Assessment --#

What do you call a combination of numbers, symbols, or other values that produce a result when evaluated?
-  An explicit conversion 

#//__ Unit three __// Loops >_<

#-- While loop --#
# While Loops instruct your computer to continuously execute your code based on the value of a condition. This works in a similar way to branching if statements. The difference here is that the body of the block can be executed multiple times instead of just once.

# You can use them to keep asking for a username if the one provided isn't valid, or maybe try an operation until it succeeds.
# One of the most common errors is forgetting to initialize variables with the right value.
# 1) Python might raise an error telling us that we're using a variable we haven't defined, NameError, just put value with it before loop .
# 2) if we reuse the variable without setting the correct value from the start, This can lead to some pretty unexpected behavior.
# how exclude infinte loop? by if then while, or while with and

if x != 0:
    while x % 2 == 0:
        x = x /2
or::

while x !=0 and x % 2 == 0:
    x = x /2


#-- For loop --#
# loop iterates over a sequence of values.
# I had to update a lot of files with different values depending on their contents.
# So I used a for loop in a script to iterate over all the files
#
#
#


#-- Recursion --#
# You need to create a family tree, showing several generations of your ancestors, with all of their children.
#
#
#
#
#



#-- Module --#


#-- Ass --#

 While loops let the computer execute a set of instructions while a condition is true. 