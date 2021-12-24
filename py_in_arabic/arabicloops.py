
#!----------
#***loops***
#?----------

##**while***
'''while expresion == (condition):
      Statement (s). 
      
@ repeats a statement or group of statements while a given condition is true.
 it tests the condition before executing the loop body
      '''
#تقوم بتكرار الجمل طالما تحقق الشرط
x = 0
while x < 10:
    print(x)
    x += 1  # if this line not written == infinty loop
#نلاحظ بدا من الصفر لانه يسبق قانون الاضافه في الترتيب
print("the end") # تظهر بعد انتهاء الدوره

#***infinty***
# لاتنتهي ومن استخداماتها في الالعاب والواجهات الرسوميه
# used in gaming, GUI, newtwork ...
'''
y = 0
while y < 10:
    print(y)
'''
# نلاحظ ستطبع اول قيمه الي ما لا نهايه

#else with while:
#to excute another code when while loop is become false
#when write it ,always will be excute

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print("x > 10")
# نري اننا استفدنا منها في كسر الدوره


#single line , حول الاعلي
#while exp : statement ; operators
z = 0
while z < 10: print(z) ; z += 1

#nested while
'''
while exp1:
   while exp2:
       stat(s2)
   Stat(s1)
'''

b = 0
while b <= 5:
    x = 0 # متغير محلي
    print (b + 1 , "interation")
    # وضعه هذه الجمله لتدلنا علي بدايه الدوره
    while x <= 3: # هذه الدوره تنفذ حتي قبل جمله زياده الاولي
        print('b = ' , b , 'x = ', x)
        print(x+1 , 'itration')
        # وضعه لتدلنا علي نهايه الدوره
        x += 1
    b += 1

## b from  0 to 10 , x from 0 to 15
b = 0
while b <= 10:
    x = 0
    print(b)
    while x <= 15:
        print(x)
        x += 1
    b += 1

#!---------------
#*** for loop ***
#?---------------

#دوره تحدث بمرورها علي تجمع من العناصر المحدده
#the for loop iterates over the elements of a collection
'''
for iterating_var in sequence:
    Statements(s)
    حيث تبحث عن وجود العنصر واحد تلو الاخر فان وجدته تذهل للذي يليه حتي تنتهي السلسله
'''
# take string == letter by letter
for letter in 'python':
    print(letter)

#nested for
'''
for iterating_var in sequence:
    for iterating_var in sequence:
        Stat(s2)
    Stat(s1)
'''
# we can use while and for inside wach other

# for every letter in python we take all ahmed letters
for x in 'python':
    print(x)
    print(".......")
    for y in 'ahmed':
        print(y)
#ex
for i in range(2, 20):
    for x in range(2, i):
        if i % x == 0:
            print(i, "equal", x, '*', i/x)
            break
    else:
            print(i, "is a prime number")

#for vs while
# FOR تستخدم لعدد دورات معلوم، تدور حول تجمع عناصر ، وتدور علي مدي قيم معلومه النهايه
#for like search inside certain containner. our appels bag.
#WHILE تدور الا ان يختل الشرط، اكثر عموميه وتعقيد ومرونه، وبامكانها اخذ كل تعبير BOOLEAN كتعبير شرطي منفرد
#while need starting value and true condition
'''
foe loop:
    you should use the for loop when the number of iterations is known.
    the loop iterates over the elements of a collection.
    the loop iterates over a range of values which is known in advance.

while loop:
    the while statement simply loops until a condition is false.
    the while loop is the more general one because its loop condition is
    more flexible and can be more complicated thwn that of a for.
    the while loop can take every boolean expression as condition.
'''
# we can 2 values as starting values for 2 while sentences

a = 0
b = 0
while a < 4:
    a = a + 1  # how first while increas
    b = 0
    while b < 4:
        b =  b + 1  # how second increase
        print(a,b)  # what we see after every loop end
        
# same above , so for this type for much easier
for a in range(1,5):
    for b in range(1,5):
        print(a,b)
        
#range
#range(start,end,step)
# defult : start by zero , increase by 1 every time
                                |# print result
#range(20)                       |# range(0,20)
print(range(20))                |# range(0,20)
                  ## so to see the number we should put range inside list()
print(list(range(20)))          |# [0,1,....19]
print(list(range(5, 20)))       |# [5,6,19]
print(list(range(5 , 20 , 2)))  |# [5,7,9,...,19]


#***control statements*** 
# break , continue , pass (used with loop and other function)

#break ,  تنهي الدوره الحاليه وتنفذ الجمله التاليه
'''
- the break statement in python terminates the current loop ,
  and resume execution at the next statement
- the most common use for break is when some external condition,
  is triggered requiring a hasty exit from a loop
'''

for letter in 'python':
    if letter == 'h':
        break        ## so h nottttt print due to break stop loop there
    print("Current letter : ", letter)
                    ## make new line to saprate loop from next part of program
print("finish")

#ex
var = 10
while var > 0:
    print("Current variable value : ", var)
    var = var - 1
    if var == 5:
        break

print("Good bye")

#continue, تعني تجاوز الجمله الحاليه واكمال الدوره
#continue == skip it (skip this iteration only)
for letter in 'python':
    if letter == 'h':
        continue 
    print('current letter : ', letter)
    
#
var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue 
    print("Current variable value : ", var)
print("Good bye")

#pass, لتخطي كود لم نقم بتجهيزه وهنا نضيفها لكيلا يتعطل البرنامج لدينا
#pass useful when we need hold space/place for our future code.

for letter in 'python':
    if letter == 'h':
        pass
        print("this is pass block")
    print("Current letter : ", letter)
print("finish")

#ex
def student():
    pass # استخدمت لتجنب خطا برمجي
def teachers():
    print("welcome")
