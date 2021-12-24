# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

### becarful ###
## delete \ between strings
# myStringSix = """First
# Second "Test" \\\ 'Test'        
# Third"""

# print(myStringFive)
# print(myStringSix)

# ## delete \ between strings and back line
# myStringSeven = """First
# Second "Test" \\\ 'Test' \
# Third"""

# ## \ it print because it between strings and not with qutation marks, and no sugn to escape it
# myStringEight = """First
# Second "Test" \ 'Test' 
# Third"""

# print(myStringSeven)
# print(myStringEight)

# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End
print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)

## Three ways of full data
print(myString[:])  # Full Data
print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

## using steps
print(myString[::2])
print(myString[::3])

# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()
## remove (spaces) or (any writen things beside our main sentence )
## but not inside it

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()
## first letter for evey words

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()
## just on start of sentence

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill
## zreo(0) fill till reach last place will fill by your string
## it start by zero if you only have one char
## but if your chart == zfill , no zero will print , just your chart
## if your zfill > chart == zero on start (== zfill - chart) then write your chart

c, d, e, f = "1", "11", "111", "1111"

print(c.zfill(0))       ##  z = 0  = ch
print(d.zfill(2))       ##  z = ch
print(e.zfill(5))       ##  z > ch = (z - ch = n0) = n0 + ch
print(f.zfill(2))       ##  z < ch = ch

# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()
## remove certain chart inside our strings , (strip for outer side )
## it give us a list from string 
## make a list ##

a = "I Love Python and PHP and MySQL"
print(a.split())
# xx = a.split()
# print(type(xx))

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"          # according sign split first 3 chart , then but all inside one string
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"          # rsplit : start from right to take first ( 3 signs == 4 chart ) as one 
print(d.rsplit("-", 3))                        # then complete else normally

# center()
## put your string in center and surrond it with (spaces , signs ,nums .char) , (nums of the whole lenght of this string)
e = "Osama"
print(e.center(9))          # Spaces
print(e.center(9, "#"))     # Hashes
print(e.center(15, "@"))    # @

# count()
## to calc number pf repeatation of chart

f = "I Love Python and PHP Because PHP is Easy PHP "
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word 
                              # ("look at" , start , end)
                              # even when I replace 0 by 1 ,2 ... it give us only one
print(f.count("PHP", 0, 40))  

# swapcase()
## change letter from caps to small or the oppesite
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()
## we expected print will be True or False

i = "I Love Python"
print(i.startswith("I"))                ## is whole string start with "I"
print(i.startswith("S"))
print(i.startswith("P", 7 , 12))        # "char" , char to check is it on start of word , end
                                        # end is optinal

# endswith()

j = "I Love Python"                     ## is whole string end with "n"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)
## first place you found your string there
## if it writen more than one , index tell you where you can find only the first

# a = "I Love Python P "
# print(a.index("P"))         # Index Number 7  [ index whole string]
# print(a.index("P", 0, 10))  # Index Number 7  [ index to certain range]
# print(a.index("P", 0, 5))   # Through Error, SyntaxError  [ index out of range]

# find(SubString, Start, End)
## same as index but instead , when you out of range error it give us (-1)

b = "I Love Python P"
print(b.find("P"))          # Index Number 7
print(b.find("P", 0, 10))   # Index Number 7
print(b.find("P", 0, 5))    # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)
## complete every space on our new width with certain sign or sapce left or write
## resample to center but here our str not should be in centre

c = "Osama E"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()
## convert each new line in our string to list item

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()
## to change default lenght of tab in string to new value
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(10))

## istitle , isspace , islower , isupper , isidentifier , isalpha , isalnum
## all answers (True  , False)

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"       ## not valid as variable name

print(seven.isidentifier())     ## is our writing valid to be name of variable?
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())              ## is all letters
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
bb = '$'
print(u.isalnum())              ## is alpha orrrrr nums in it
print(z.isalnum())
print(bb.isalnum)               ## signs == False
# ---------------------
# -- Strings Methods --
# ---------------------

# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1"))        ## replace all old by new one
print(a.replace("One", "1", 1))     ## replace count = how many times you replace by order
print(a.replace("One", "1", 2))     ## first and second

# join(Iterable)
## to convert list to one string , may saprate it words by (spaces , , - ....)
## it opposite to split which change str to list

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
dd = "-".join(myList)
print(type(dd))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

## "    string %s %d %f string             " % our_value
## ' to label the place to change it later ' % any value or (variables )
print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)  ## %.2f   it take only first two places from float

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString) ## %.5s  it take only first five places from string 

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

## {} or {:s}, {:d}, {:f} rather than %s %d %f and .format(adds) rather than % (adds)
name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))     ## to make sure to certain type should be entry

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))     ## my nums take space every 3 nums
print("My Money in Bank Is: {:,d}".format(myMoney))     ## ## my nums take , every 3 nums

# ReArrange Items
## by calling one varible before another
## using it's index
## start with zero

a, b,  = "One", "Two"   # not need to be on same line
c = "Three"
## how they are arrange
## according to .format(p1,p2,....)

print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")      ## without f , our variables become part of our string
print(f"My Name is : {myName} and My Age is : {myAge}")     ## so we need (f) = to et value of variables

'''
Learn about:

    Python Strings Method
    Python Indexing
    Python Slicing

'''