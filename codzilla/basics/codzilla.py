# What adding by codzilla, to my basics
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print(" _____")
print('   ||  ')
print('________')
print('\______/')

# Search about how make shape with python prints

# strings function ( to get information, modify it)
#.lower , .upper , .isupper , .islower
#you can use multiple function after each others
# as, .lower().islower()
print('--------- strings------------')
text = 'codzilla'
print(text.upper())
print(text.lower().islower())  # True or False

print(len(text))   # len for what inside variable
print(len('btoo')) # len from strings

print(text[0])     # what we found inside this place
print(text[-1])

print(text.index('c'))  # where we found this string, to search for certain character

text2 = 'btoooo'
print(text2.replace("oooo","mode")) # need two values, becarful it caseSensitive
                                   # first = old , second = new


#numbers
print('--------- numbers------------')

my_num = -5
print(abs(my_num))  # absolute value of number

print(pow(2,3))   # 2^3 = 8 
                  # should give it 2 values

                  ## [ max , min ] may for more than just two elements
print(max(4,10, 15))  #15
print(min(4,10, 0))  #0

print(round(3.2)) # 3
print(round(3.7)) # 4

from math import * 
print(floor(3.7))  # floor : back it to lower number even if 3.9 go back to 3
print(ceil(3.1))   # ceil: opposit to floor
print(sqrt(9))     #sqrt : get its square root

#inputs 
'''
    interacts with user
    capturing input
    process input & react
'''
print('--------- inputs------------')

# don't forget == input(string) , so need [int] to deal with numbers
color = input('enter a color: ')
plural_noun= input('enter a plural noun: ')
adjective = input('enter an adjective: ')

print('tress are '+color)
print(plural_noun+" are mean")
print('please keep it '+adjective)

  ## use (,) if you don't want use spaces
print('tress are',color)
print(plural_noun,"are mean")
print('please keep it',adjective)
  ## using .format
print('tress are {}'.format(color))
print("{} are mean".format(plural_noun))
print('please keep it {}'.format(adjective))

print('--------- lists------------')
#list as group of boxes every one saved type of data , all of them inside only one main place

friends = [1,'codzilla',True,False,[1,'islam']]
print(friends)
print(friends[2])
print(friends[1:3])      ## False not print
print(friends[1:])
print(friends[-1])
friends[0] = 'btoo'      ## change it
print(friends)
friends[0:2] = 'btoo'    ## replace first 2 by this string but it [ slice ]
print(friends)
print(friends.index(1))  ## ask about where I found (1)


print('--------- tuples------------')
coordinates = (23,45) 
print(coordinates)
print(coordinates[1])
'''
coordinates[0] = 66  # TypeError: 'tuple' object does not support item assignment
print(coordinates)
'''
list_of_tuples = [(2,3),(4,5),(6,7)]
print(list_of_tuples)
print(list_of_tuples[0][1])
'''
list_of_tuples[0][0] = 5
[0] = first item of list,[0] = first of the first item === 2
you can't change it , its tuples
'''
x = list(list_of_tuples)
print(x)

## change tuples to list
z = (1,3,5,6)
x = list(z)
print(x)


print('--------- function------------')

def say_hi(name,age):  # parameters may any datatype
    print('hi',name,'your age is ',str(age))

print('first')    ## before it
say_hi('btoo',8)
print('second')   ## after it

#cubing
def cube2(num):
    num*num*num


print(cube2(3))  # without return === none

def cube(num):
    return num*num*num
    print('this line not excutable ever')  ## !!!!!! any thing after return not disply!!

print(cube(3)) # now get result

result = cube(4) # use function inside variable
print(result)

# return is last line excute in function

print('--------- if ------------')

## wake up
wake_up = "yes"
hungry = "yes"
if wake_up == "yes":
    if hungry == "yes":
        print("cook breakfast")

## leave house
leave_my_house = True
weather = "cloudy"

if leave_my_house == True:
    if weather == 'cloudy':
        print("I take my umbrella")
    else:
        print("I take my sunglasses")

## at restaurant
at_restaurant = True
want = "beef"

if at_restaurant:  # it mean it == True
    if want == "beef":
        print(" I order a burger")
    elif want == "pasta":
        print(" I order spagetti")
    else:
        print(" I order a salad")

##
is_hungry = False
wants_to_eat = True

if is_hungry and wants_to_eat:
    print("go eat")
elif is_hungry and not wants_to_eat: # elif == we can not reach it, [if above it was excuite]
    print("you need it")
elif not is_hungry and wants_to_eat: 
    print("not eat if not hungry")
else:
    print("don't")

## False = 0 = ''
## True  = 1

print('--------- operators ------------')

# make max():

def max_num(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

print(max_num(10,20,30)) 

# compare two strings:
## [1] return
def str_match(str1,str2):
    if str1 == str2:
        return "match"
    else:
        return "not match"

print(str_match('btoo','kko'))

## [2] print
def str_match(str1,str2):
    if str1 == str2:
        print("match")
    else:
        print("not match")

str_match('btoo','kko')

## calculator

num1 = float(input("please enter the first number: "))
operator = input("please enter the operator: ")
num2 = float(input("please enter the second number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == '/':
    print(num1/num2)
elif operator == "*":
    print(num1*num2)
elif operator == "//":
    print(num1//num2)
elif operator == "%":
    print(num1%num2)
else:
    print("sorry, you enter wrong operator")

## ------------------------------------
## change it to function ## -----------
## ------------------------------------
def calc():  ## if your parameter empty [ you can call your function with empty parameter]
	num1 = float(input("please enter the first number: "))
	operator = input("please enter the operator: ")
	num2 = float(input("please enter the second number: "))

	if operator == "+":
		print(num1+num2)
	elif operator == "-":
		print(num1-num2)
	elif operator == '/':
		print(num1/num2)
	elif operator == "*":
		print(num1*num2)
	elif operator == "//":
		print(num1//num2)
	elif operator == "%":
		print(num1%num2)
	else:
		print("sorry, you enter wrong operator")

calc()



print('--------- Dictionaries ------------')
# as what happen when search by dictionary book,  (key,value)

convert_month = {
    "Jan" : 'January',
    'Feb' : 'Febraury',
    'Mar' : 'March'
}
     ## don't forget == [ ] , we use it always for indexing
print(convert_month['Mar'])
    ## another way
print(convert_month.get('Mar')) 
print(convert_month.get('code', "value not found")) # here why we use get, 
                                                    # we can add message if our value not found

city = {
    'jed' : 'jeddah',
    'krt' : 'Khartoum',
    'cai' : 'cairo'
}

print(city.get('jed'))
print(city.get('ruh','not adding yet')) # instade of none == [keyEroor], we use our message

print('--------- while loops ------------')
# else,continue,break
i = 0

while i <=10:
    i = i +1
    if i == 5:
        continue    ## skip this
    if i == 9:
        break       ## go outside the loop
    print(i)        ## ## anythngs after break == not excute
else:               ## else == not excute if we use break
    print('the condition was false')

print('--------- for loops ------------')
##build guessing game
buddies = ['pikachu','grandizer','suzero','winner']
string = 'codezilla'
# for with list
for index in range(len(buddies)):
    print(index)                   ## print number 0,1,...

buddies = ['pikachu','grandizer','suzero','winner']
string = 'codezilla'
# for with list
for index in range(4):
    print(index)  
# ---------------------- #

buddies = ['pikachu','grandizer','suzero','winner']
string = 'codezilla'
# for with list
for index in buddies:
    print(index)  

# to print list of values
for index in range(len(buddies)):
    print(buddies[index])

# for with string
for x in range(len(string)):
    print(x)
# to print every letter
for x in range(len(string)):
    print(string[x])

# for with if
## search item by item
for buddy in range(len(buddies)):
    if buddies[buddy] == 'winner':  # 0,1,2, take it item by item
        print(buddy, 'is the winner')
    else:
        print(buddy,"is not the winner")

# for with break and else  ,,, just when found it , print it
for buddy in buddies:    # here we search every elements inside list
    if buddy == 'winner':  
        print(buddy, 'is the winner')
        break    # finish the loop
else:
    print("is not the winner")

# for with continue
for x in range(3,10):
    if x ==5:
        continue
    print(x , "is the choosen number")
else:
    print(" the loop is finished")

print('--------- expontent def ------------')

def power(base_num,pow_num):
    result = 1                     # 1 x base_num = base_num
    for index in range(pow_num):   # number of times we multiply this base_num , just new [last_result * base_num]
        result = result * base_num # 1 * base_num * base_num * base_num
    return result

print(power(2,3))

'''
         r     base_num   , pow_num
		1*2        2           1
		2*2        4           2
		4*2        8           3
		8*2        16          4
'''

print('--------- nested loops + 2d list ------------')
#نحتاج للوصل لها تحديد قيمتين
#مفيده في احداثيات الالعاب والبرامج

no_list = [
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]

print(no_list)
print(no_list[1][0])  # 4

#nested loop
## to deal with list items

for row in no_list:
	for col in row:
		print(col)
		#قد نستفيد منها في العمليات الحسابيه داخل لعناصر اللسته
	#	print(col*2)
	#	print(col*(col+1))

				
print('--------- try , except-----------')
value = int(input('Enter a number: '))
print(value)
print('success')   # if we write letter == ValueError: invalid literal for int() with base 10: 'btoo'

#نحتاجها لكي لا يتوقف البرنامج عند الخطا

'''
by tring I just do it only for one error by time

try:
	value = int(input('Enter a number: '))
	print(value)
	result = 10/0
except ZeroDivisionError:
	print('you cannot divide by zero')
	#هنا لن يتوقف البرنامج عند حدوث الخطا ولكن ستظهر هذه الرساله
except ValueError as err:
	print(err)
	# هذا اذا اردناه يخرج الرساله البرمجيه

except:
	print('invalid input')
	#الاستثناء الافتراضي لازم في النهاية
print('success')
'''


print('--------- files-----------')
# not work read about dealing with it for both windows and linux

'''
r read
w write
r+ read and write
a append to add to last of it
'''
## ----------------------------------
## we use print() to read -----------
## ----------------------------------

workers_file = open('workers' ,'r')
# if on windows workers.text
print(workers_file.readable())
# it back true or false
print(workers_file.read())
#read all it
print(workers_file.readline())
#read every time one line
print(workers_file.readlines())
#read all of them on list style
print(workers_file.readlines()[2])
#read line number 3
'''
for worker in workers_file.readlines():
	print(worker+'is cool')

'''
workers_file.close()

#:::::
x = open('index.html','w')
x.write('<p>btoo</p>')
x.close()

y = open('text','w')
list_of_lines =['\n welcome','\n btto','hhh']
y.writelines(list_of_lines)
y.colse()

'''
read = r
write = from start = w
write = from last = a
read and write = delete start = w+
read and write = add = start = r+
read and write = add = end = a+

'''