
#!---------------
#***conditions***
#?---------------

#المقدره علي اتخاذ قرار منطقي تبعا للقيم المتغيره
#flow diagram :(if condition is true = if code), (if condition is false = else code)

#why condition??
'''
a decision is when a program has more than one choice of actions 
depending on a variable's value. think of a trafic light.
when it is green, we continue our drive.
when yellow , reduce our speed.
when it is red , we stop.
these are logical decisions that depend on the value of the traffic light.
so, python has a decision statement to help us when our application needs
to make such decision for the user.
'''
x = 4
if x == 5:
    print('x = 5')
    #! no thing appear , due to our condition not true

#? traffic_light

color = str(input("Enter traffic light color:\n"))

if color == 'green' or color == 'Green':
    print('continue your driving')
elif color == 'yellow' or color == 'Yellow':
    print('please, decrease your speed')
elif color == 'red' or color == 'Red':
    print('stop!!!!')
else:
    print('You don\'t use the right light')

# else run :: when if code and elif code are wrong

#? if with boolean operators

name = "mahmoud"
age = 21
if name == "mahmoud" and age == 21:
    print("your name is mahmoud and your age 21")
if name == "mahmoud" or name == 'ahmed':
   print("your name is either mahmoud or ahmed")

#login ex:

username = 'btoo'
password = 12345

if username == 'btoo' and password == 1234 :
    print("login access, welcome btoo")
else:
    print("login field, try again")
    
#if else
x = 500
if x > 600 :
    print("x is bigger than 600")
else:
    print("x is smaller than 600")

#if , elif , else :-
# (if statement is true = do smth),
# (elif another statement is true = do smth), 
# (else = do another thing)

x = 100
if x == 200:
    print("1 - got a true expression value")
    print("x")
elif x == 150:
    print("2 - got a true expression value")
    print(x)
elif x == 100:
    print("3 - got a true expression value")
    print(x)
else:
    print("4 - got a false expression value")
    print(x)
print("Good bye")
#ex
x = 333
if x < 200:         #! if x = 99 , print == "expression value is less than 200"
    print("expression value is less than 200")
    if x == 150:
        print("which is 150")
    elif x == 100:
        print("which is 100")
    elif x == 50:
        print("which is 50")
    elif x < 50:
        print("expression value is less than 50")
elif x > 200:
    print("expression value is more than 200")
else:
    print("could not find true expression")
print('good bye')

#? single if statement
# فقط ارفع جوتب الشرط بعد :
X = 5 
if x == 5 : print("x = 5")

# SINGLE IF ELSE
#نبدا بالجواب ثم شرط if ثم else وجملتها ، نلاحظ عذم وجود نقاط او فواصل رقميه
name = 'btoo'

###  True Condition False
print('welcome btoo') if name =='btoo' else print('who are you')

#ex
y = 10
t = 15
if y == 10 : print('y = 10')
print('t = 10') if t == 10 else print('t != 10')

#!-------------
#***examples***
#?-------------

#1
#this loop not stop except you get the number
answer = 23
question = "what number am i thinking of\t?"
print('let\'s play the guessing game!')

while True: # condition of loop is true to cont
    guess = int(input(question)) #! beautiful using of variables, to shortcut your code
#?استخدم متغير جديد ، يساوي القيمه الرقميه لمتغير في الاعلي يدخله المستخدم ، لنقوم بعد ذلك باجراء الجمل الشرطيه علي المتغير الجديد
    if guess < answer:
        print("littile higher")
    elif guess > answer:
        print('little lower')
    else: # guess == answer
        print("excelent!!!")
        break  # we need use break to stop the loop if user guess it

#2
#! all , any ::: and becarful use == instad of = , so : 
#? ([variable == value,....]):
'''
both there sentence should inside ( [ ] )
also put variables and thier values ,,,,,,,,
saprate between variabels by ,,,,,,,,,,,,,,,
'''
x , y , z , r = 5 , 6 , 3 , 2
if all( [ x == 5 , y == 6 , z == 3, r == 2] ):
    print("all done")# حال تحقق جميعها
if any( [ x == 2 , y == 6 , z == 3, r == 1] ):
    print("error happen") #  حال تحقق شرط واحد

#3 : is it in dictionary

birds = {"parakeet": 1, 'parrot': 2}
if "parrot" in birds:
    print("found")

    ##
pubg_maps = {"livik":1,"sanhock":2,"mirmar":3,"karakin":4}
if "karakin" in pubg_maps:
    print("yes")

    ##
    ## we choose our input is it one element from certain list.
#! ############################
#? using if input in (items):

pubg_maps = input("Enter your favorit pubg map")
if pubg_maps in ("livik", 'sanhock'):
    print(pubg_maps) 



#4
a = 1
b = 2

if a == 1 and b == 2 :
    print("True")

if a == 0 or b == 2 :
    print("True")

if not (a == 1 and b == 3):
    print("True")

if a != 0 and b != 3 :
    print("True")

#5
number = 1
#see if number is not equal to 2
# يعني not لعكس الجمله المكونه
if not number == 2: 
    print('True')
    
# see if string not in collection
#يعني not in للبحث عن شي هل هو موجود والرجوع بالقيمه
birds = {"parakeet": 1, 'parrot': 2}

if "automobile" not in birds:
    print('not found')
    
#6
x = 4
if x in (0 , 2, 4): # هل قيمه x موجوده داخل القوسين
    print("match")
else:
    print("not match")

#7
value1 = 15
value2 = 10
#see if these two values are equal
equal = value1 == value2   
#! equal = (True or False)

#test True and False constants  
## if result was false no one of lower sentence will be work
if equal == True: print(1)
if equal != False: print(2) # it's also true

#8
#? [] الدوران حول قايمه داخل قائمه والاستفاده من 

values = [[1, 1], [2, 1], [1, 1], [3, 1]]

for pair in values:
    #every element compose from [0,1] , index number
    # we start by the first part of each list 
    #.. It is most specific
    #.. This reduce total checks
    if pair[0] == 1 and pair [1] == 1:
        print("True")
    elif pair[0] == 2 and pair [1] == 1:
        print("done")
    else:
        print('not important')
# for (name from me [pair] , to use it later) in var
# في المثال اعلاه نتحقق من كل قايمه مكونه من عنصرين عنصر عنصر علي حدا...

