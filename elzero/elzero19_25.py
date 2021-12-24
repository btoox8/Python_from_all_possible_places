# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j                                      ## j, sign of complex
                # real + imagj
print(type(myComplexNumber))

print("Real Part Is: {}".format(myComplexNumber.real))      ## real, part of nums
print("Imaginary Part Is: {}".format(myComplexNumber.imag)) ## imag, part of nums

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)            ## no result of adding , just write as it
print(int(10+9j))       ## you can'tttttttttt

# --------------------------
# -- Arithmetic Operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition

print(10 + 30)  # 40
print(-10 + 20)  # 10
print(1 + 2.66)  # 3.66
print(1.2 + 1.2)  # 2.4

# Subtraction

print(60 - 30)  # 30
print(-30 - 20)  # -50
print(-30 - -20)  # -10
print(5.66 - 3.44)  # 2.22

# Multiplication

print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100)  # 1500

# Division

print(100 / 20)  # 5.0
print(int(100 / 20))  # 5

# Modulus

print(8 % 2)  # 0
print(9 % 2)  # 1
print(20 % 5)  # 0
print(22 % 5)  # 2

# Exponent

print(2 ** 5)  # 32
print(2 * 2 * 2 * 2 * 2)  # 32
print(5 ** 4)  # 625
print(5 * 5 * 5 * 5)  # 625

# Floor Division

print(100 // 20)  # 5
print(119 // 20)  # 5
print(120 // 20)  # 6
print(140 // 20)  # 7
print(142 // 20)  # 7

# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]       ## mutable == editable

## same index and slicing as string

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]
print(myAwesomeList)

## change element by another
myAwesomeList = ["One", "Two", "One", 1, 100.5, True]       

myAwesomeList[1] = 2
myAwesomeList[-1] = False
print(myAwesomeList)

## change group of elements by another
myAwesomeList = ["One", "Two", "One", 1, 100.5, True]       
myAwesomeList[0:3] = ["A"]      ## delete the all old and reolace them by new inside []
print(myAwesomeList)

# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["Osama", "Ahmed", "Sayed"]
myOldFriends = ["Haytham", "Samah", "Ali"]

## add to last of list any data type even another list
myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)  ## add another list to last

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])          ## access to list elements

# extend()
## add list to another

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()
## remove only one (item)
## if there repeatation , remove the last one of them

x = [1, 2, 3, 4, 5, "Osama", True, "Osama", "Osama"]
x.remove("Osama")
x.remove(5)
print(x)

# sort()
## it orgnize nums or letter inside listby two ways 
## sort()              == from small to large
## sort(reverse=True)  == from large to small 
y = [1, 2, 100, 120, -10, 17, 29]
#y = ["A", "Z", "C"]
#y.sort(reverse=True)
#y.sort()
print(y)

# reverse()
## it reverse the item by same orders from  last to start
z = [10, 1, 9, 80, 100, "Osama", 100]
z.reverse()
print(z)

# -------------------
# -- Lists Methods --
# -------------------

# clear()
## delete all elements of list

a = [1, 2, 3, 4]
a.clear()           
print(a)

# copy()
## copy list to another variable
## change on main list not change copied once
b = [1, 2, 3, 4]
c = b.copy()

print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()
## number of repeating
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()
## determain position of item
e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(e.index("Ramy"))

# insert()
## add item to certain index 
## not delete any item from our list

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")             ## add to start
f.insert(-1, "Test")            ## add before the last

print(f)

# pop()
## appear what we delete it 
## delete according index
## delete the last if empty pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3))        
print(g.pop())
print(g)

# -----------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# -----------------------------

# Tuple Syntax & Type Test

myAwesomeTupleOne = ("Osama", "Ahmed")
myAwesomeTupleTwo = "Osama", "Ahmed"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values

myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment

# Tuple Data
myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])

# -----------
# -- Tuple --
# -----------

# Tuple With One Element

myTuple1 = ("Osama",)
myTuple2 = "Osama",

print(myTuple1)
print(myTuple2)

print(type(myTuple1))
print(type(myTuple2))

print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b

print(c)
print(d)

# Tuple, List, String Repeat (*) 
## all of them repeating their items many times

myString = "Osama"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()

b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error  ## this way not work with str + nums
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct
## take items in it and assign it to different variables

a = ("A", "B", 4, "C")

x, y, _, z = a          ## all variable is part of main a 

print(x)
print(y)
print(z)
print(_)                ## we can call it

'''
Learn about:

    Python Data Types
    Python Operators

'''