#explain some list attributes
nums = [1,2,3]
nums.append(4)
print(nums)
print(max(nums)) # maximum max(list)
print(min(nums)) # we don't use (.)
print('_________')

print(max(66,80)) # we do it immediatly

index = 1
nums.insert(index, 'is') #may use number insted of index, to place where you want to add
print(nums)

letters = ["m","o",'h',"a",'m','e','d']
print(letters.index('o'))
print(letters.index('m'))# give the first one place only
print(letters.count('m')) # how many times an item occurs in a list
print(letters.remove('d')) # it remove but need another print to see what happen
print(letters)
print(letters.reverse())#also need to another print statement
print(letters)

# Analize to relize
"""
You’re analyzing a data set and need to remove the outliers (the smallest and largest values. The data is stored in a list). Complete the code to remove the smallest and largest elements from the list and output the sum of the remaining numbers. I’m very lost. Having trouble from the lesson on how to pull the min and max and get rid of them let alone add it all up after. Code: 
"""
data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78] 
#your code goes here 
data.remove(max(data)) #look at this
data.remove(min(data))
print(sum(data))

#my example
my_degree = [ 100,50,70,10,80,70,55,6,7]
my_degree.remove(min(my_degree))
my_degree.remove(max(my_degree))

print(sum(my_degree ))

#string function
print("welcome, {a} {b} {a}".format(a='hello',b='btoo'))
#{place holder} , format(our variable and its value)
#from list 
#make {empty} , and format{list[indix],list[indix]}
a = [2,5,7]

print("welcome, {},{}".format(a[0],a[2]))

####
print(','.join(['spam','btoo','go']))
#to join multiple strings inside list to make one string, saprated by (,)

print(''.join(['spam','btoo','go']))
#you should write string even empty'' before.join , to work

print('** '.join(['dark','go']))

print(' welcome every body'.split(','))


print(' welcome , every, body'.split(','))

print(' welcome , every, body'.split('*'))

print('welcome btoo'.replace('btoo','mohamed'))

print('hello my bro'.upper())
print('hello my bro'.lower())

### the result one of bool(true or false)
print('this is btoo'.startswith('this'))
print('this is btoo'.endswith('btoo'))

#Shouting text

def shout(text):
    
    text = input('Enter your text\t')
    print(text + ' !!!')

shout('')

#Feet to inches
"""
You need to make a function that converts a foot value to inches. 1 foot has 12 inches. Define a convert() function, that takes the foot value as argument and outputs the inches value. —————— Lost here again as it doesn’t explain well how to set and use the convert variable in the lesson.
"""

feet = int(input('Enter your feet\t'))

def convert(ft):
    inches = ft * 12 # our rule
    print(inches) # we use variables called inches

convert(feet) # take your value from upper input


#convert this rule
#c = 1.8 *(f - 32)
f = int(input(''))
#we use the inner variable

def c(f):
    c = 1.8 * ( f -32)
    print(c) # we need to know the full result
    
c(f)

##

def max(x, y):
    if x >=y:
        return x
    else:
        return y
print(max(4,7))
z = max(8,5)
print(z)

def shortest_string(x,y):
    if len(x) <= len(y):
        return x
    else:
        return y

shortest_string('btoo','mohammed')
print(shortest_string)
        
def add_numbers(x,y):
    total = x + y
    return total
    print('this won\'t be printed') #not printed, due it come after return
    
print(add_numbers(4,5))

# How many letters
"""
Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string. Sample Input hello, how are you? o Sample Output 3 Explanation: The letter o appears 3 times in the given text.
"""
#write text then write which letter want to know it
#your final code would be text.count(by using this letter repeated)

text =str(input('Enter text here..\t'))
letter =str(input('Enter letter which you want to know it\'s duplication..\t'))
num=text.count(letter)
print('this letter repeated ' + str(num) + 'times')

#Search engin



"""
You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
"""
#by using return inside function and print that function outside it

text = input()
word = input()

def search(text,word):
    if word in text:
        return('found it')
    else:
        return('not found')

print(search(text, word))

#by using print inside function and call it outside
text = input()
word = input()
def search_print(text,word):
 if word in text:
    print("Word found")
 else:
    print("Word not found")
search_print(text,word) # don't forget variables here.

#my example

#by using return inside function and print that function outside it


#by using print inside function and call it outside
company = input('Enter the company, then the city available on it\n')
city = input('Enter city you want to go to it\t')

def travel(company,city):
    if city in company:
        return city + ' it available'
    else:
        return 'we not found it, sorry'

print(travel(company,city)) # don't forget both variables
