#Please note down 1 point if you answered this correctly. 
#1
#Exercise for reference: 

a = 2
a = 4
a = 6
print(a + a + a)

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
The script would output 18  in the command line. Below is the explanation. 
Since Python reads and executes scripts from top to bottom, variable a  will be updated 
in every line until line 3 where a  finally gets the value of 6 .
 Then the print  function prints out 6 + 6 + 6  which is 18 .
'''

#2
a = 1
_a = 2
_a2 = 3
#2a = 4
'''
Answer: 
Line 4 throws a SyntaxError because variables cannot start with a number. 

@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
Variable names must start with a letter or an underscore. Everything else will throw a SyntaxError.
'''

#3
a = 1
b = 2
c = 2
print(a == b)
print(b == c)

#4
a = "1"
b = 2
print(int(a) + b)
'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
Values in Python can be of different types. In this exercise, 
the value assigned to a  was of string type (i.e., text) while the value of b  
was an integer (i.e., whole number), and you cannot add strings with integers. 
Therefore we needed to convert the string to an integer using the int()  
addition operation's built-in function to be possible.
'''

#5
#Exercise for reference: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
Every item of a list is referenced to an index number starting 
from zero and increasing by one. Such a hidden index system is used to access list items.
 Therefore, we accessed item b using an index of 1.
'''

#6
#Exercise for reference: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
d  has an index of 3  here, e  has an index of 4 , and f  has an index of 5, 
but since the slicing syntax is upper-bound exclusive,
 we need to pass 6  as the upper bound.
'''

#7
#Exercise for reference: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[:3])

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
[:3]  is just a shortcut [0:3] . Both would do the job,
so you can mark this exercise as solved if the output was correct.
'''

#8
#Exercise for reference: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-2])

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
Besides the left-to-right positive indexing system that starts from zero, 
equence data types such as lists also have a second indexing system that 
starts from -1 and decreases by one from right to left. 
'''

#9
#Exercise for reference: 
#Becarfull!!!  , when say go to end we mean last even when start with negative

print('Becarfull!!!  , when say go to end we mean last even when start with negative')
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[-3:])
# not true
#[-3:-1]  == h,i

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
[-3:]  means from the item with index -3  (i.e. h ) to the very last item of the list.
When you don't put any index to the colon's right, everything is included,
and upper-bound exclusivity is ignored.

'''
#10
#Exercise for reference: 

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
The complete syntax of list slicing is [start:end:step] .
 When you don't pass a step, Python assumes the step is 1. 
 [:]  itself means to get everything from start to end. So, 
 [::2]  means get everything from start to end at a step of two.
'''

#11
#Exercise for reference: 

my_range = range(1, 21)
print(list(my_range))      ## without list() == result == range(1,21)

'''
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
range()  is a Python built-in function that generates a range of integers. 
However, range()  creates a Python range object. To get a real list object, 
you need to use the list() function to convert the range object into a list object.
'''

#12
#a   ## for loop with range(), should all inside [] . to disply our result
my_range = range(1, 21)
print([10*x for x in my_range])

## from me ------------------------
print([2*b for b in my_range])
print([x/2 for x in my_range])

# make list so we write it inside [] ,
# [10 times * for this variable(x) for loop (x) in my varaible ]

#b
my_range_2 = range(10,201,10)
print(list(my_range_2))
'''
Hint: One way to solve this is to use list comprehension.
'''

# 13
## map : it function to apply certain function on iterable == map(func,range() == or its variable)
my_range = range(1, 21)
print(list(map(str,my_range)))

## from me -------------------------
print(list(map(str,range(1,21))))
print(list(map(float,my_range)))
x = list(map(str,my_range))
print(x)
print(list(map(int,x)))



'''
Question: Complete the script, so it generates the expected output using my_range  as input data.
Please note that the items of the expected list output are all strings.
Hint: Use the map  function.
'''

#14
a = ["1", 1, "1", 2]
print(list(set(a)))       ## set not allow duplicate

## need import modules
from collections import OrderedDict
b = ["1", 1, "1", 2]
b = list(OrderedDict.fromkeys(b))
print(b)

## make a new list and add items with for loop inside it if condition
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)


'''
Question: Complete the script so that it removes duplicate items from the list a .

Hint 1: Sets are datatypes where duplicates are not allowed.
Hint 2: You can use a set function to convert the list to a set and then a list function to convert the set back to a list.

@@@@@@@@@@@@ Explanation: @@@@@@@@@@@ [1]: 

We used a set  function to convert the list to a set that would intermediately produce {'1', 1, 2}
with no duplicates because set objects cannot contain duplicates.
Then using list  we converted the set back to a list.
The drawback here is that the original order of the items is lost. 
If you need to preserve the order, you may want to use the solution in Answer 2 below.

Answer 2:

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

@@@@@@@@@@@@ Explanation: @@@@@@@@@@@ [2]:

Ordered dictionaries are another data type in Python that,
unlike sets and normal dictionaries they preserve the order of the items.
Here OrderedDict.fromkeys(a)  would produce a OrderedDict  like [('1', None), (1, None), (2, None)] .
Then we would convert that OrderedDict  to a list.

@@@@@@@@@@@@ Explanation: @@@@@@@@@@@ [3]:

This is another solution that would preserve the original order. 
We go through all the original list items and append them to the new list if they have not been appended before. 
The downside of this is that the operation can take a lot of time
if the list as large as we need to access both lists and perform a conditional in each iteration.
'''

# 15

c = {'a':1,"b":2}         ## by only {} , we need write our key and value
print(c)

d = dict (a =1 , b =2)    ## dict(key=value,key=value)
print(d)

'''
Question: Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
Create a dictionary that contains the keys a  and b  and their respective values 1  and 2 .
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@ [1]: 
Using curly brackets is one way to create a dictionary.
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@ [2]:
A dict  function is another way to create a dictionary. dict  is also used to convert other objects to a dictionary.
'''

#16
d = {"a": 1, "b": 2}
print(d["b"])
'''
Question: Please complete the script so that it prints out the value of key b .
Hint: Dictionaries are exactly like lists. The difference is keys are the indexes.
@@@@@@@@@@@@ Explanation: @@@@@@@@@@@
As you see, accessing dictionary values follows the same syntax as accessing list items.
 The difference is that lists have indexes, while dictionaries have keys that you create by yourself.
'''

#17
d = {"a": 1, "b": 2, "c": 3}
print(d["a"]+d["b"])
'''
Question: Calculate the sum of the values of keys a  and b .
Hint: Access the values as you did in the previous exercises.
Explanation: 

It's as easy as that. However, if you want to do the sum of all dictionary values, 
you need to take another approach instead of accessing all values one by one. 
We're going through that approach later on in another exercise.
'''
#18
d = {"Name": "John", "Surname": "Smith"}
#print(d["Smith"])
print(d["Surname"])
'''
Answer: 
There is no key Smith  in the dictionary. Smith  is a value. 
You want to use Surname  if you want to access Smith :
print(d["Surname"])

Explanation: 
A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).
'''

#19
d      = {"a": 1, "b": 2}
d['c'] = 3                    ## just make new key & value
d['d'] = 5
d['h'] = 7

print(d)

'''
Hint 1: Refer to key c  and use the assignment operator to assign a value to the key.

Hint 2: Note that dictionaries are unordered collections, so don't worry about the order. It's always random. 
Explanation: 

Adding pairs of keys and values is straightforward,
as you can see. Note, though, that you cannot fix the order of the dictionary items. 
Dictionaries are unordered collections of items.

'''
#20

d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))

'''
d.values()  returns a list-like dict_values  object 
while the sum  function calculates the sum of the dict_values  items.
'''

#21
d = {"a": 1, "b": 2, "c": 3}
print(d.items())
d = dict((key, value) for key, value in d.items() if value <= 1)   ## all syntax inside dict()
print(d)

'''
Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
Hint 1: Use dictionary comprehension.
Hint 2: Inside the dictionary comprehension access dictionary items with d.items()  
if you are on Python 3, or dict.iteritems()  if you are on Python 2.

Explanation: 

Here we're using a dictionary comprehension. The comprehension is the expression inside dict(). 
The comprehension iterates through the existing dictionary items, 
and if an item is less or equal to 1, the item is added to a new dict. 
This new dict is assigned to the existing variable d  , 
so we end up with a filtered dictionary in d.
'''

#22
a = list(range(1,11))
b = list(range(11,21))
c = list(range(21,31))
d = dict (a = a,b =b , c=c)
print(d)
## or
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
print(d)
'''
Explanation: 
We're using ranges here to construct the lists. 
We're also using the built-in Python pprint  module, 
which is used to print out well-formatted views of datatypes in Python.
'''


#23
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d['b'][2])
'''
Question: Access the third value of key b  from the dictionary.
Hint: You need square brackets after square brackets here.

'''
## pprirnt
from pprint import pprint    ## good with dict lines

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
pprint(d)
pprint(d['b'][2])

#24 
## dict with for loop

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
for key,value in d.items():
    print(key,'has value',value)
'''
Question: Please complete the script so that it prints out the expected output.

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

Expected output: 

b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Hint: Iterate through the d.items()  (Python 3) or d.iteritems()  (Python 2) with a for loop.
'''

#25
import string

for letter in string.ascii_lowercase:  # _letters , _uppercase
    print(letter)

'''
Make a script that prints out letters of the English alphabet from a to z, one letter per line in the terminal.

Explanation: 
string  is a built-in module and string.ascii_lowercase  
returns a string object containing all 26 letters of the English alphabet. 
Then we simply iterate through that string and print out the string items.
'''