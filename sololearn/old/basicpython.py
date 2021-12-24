#basic python
#***basic concepts***

print("hello")
print(5+5) # يمكن الكتابه هكذا ، لكن الافصل الطريقه الثانيه
print(5 + 5)
print((6*12)+5/(3*6))
# الاولويه للاقواس ثم الضرب والقسمه واخيرا الجمع او الطرح
print((60*60)*24*30)
# عدد الثواني في اليوم
#exponentiation
print(2**3**2)
print(2**9) #.  تساوي اللتي بالاعلي
print(9** (1/2))
print(27 ** (1/3)) # الجزر التكعيبي
print(20 // 6) #quotient
print(1.25 % 0.5) # remainder
#flight time
print(7425/550)


#***strings***
print("string")
print('brain\'s mother: He\'s not an angel.')
print('one \ntow \nthree')
print("""
this is 
a multiline
text
""")
print('spam' + 'eggs') #concatenation
print("2" + "2")
print('spam' * 3)
print(4 * '2')
#leaderboard
print('''
1.
2.
3.
4.
5.
6.
7.
8.
9.
''')
#***varables***
user = 'james' #  متغير لحفظ البيانات
# لكتابته شروط يبداء بحرف ويحتوي حرف رقم و _
x = 7
print(x)
print(x + 3)
print(x)
x = 123.456
print(x)
x = "this is a string" #يمكن تغيير نوع البيانات في المتغير مع عدم تفضيل فعل ذلك لتجنب الاخطاء
print(x + "!")
'''
x = input() # كل مايكتب هنا هو سترينج
print(x)
name = input("enter your name: ")#رساله توجيهيه
print('hello, ' + name)
age = int(input) # we can use float() also
print(age)
lesson = 40
print("it is lesson number " + str(lesson)
name = input()
age = input()
print(name + ' is' + age)
'''
#in-place operators
x = 2
print(x)
x += 3
print(x)
x = 'spam'
print(x)
x += 'eggs'
print(x) # equal srt concat
#tip calculator
bill = int(input())
print(bill*20/100) # لاحظ كيف تكتب النسبه المئويه
#***control flow***
my_boolean = True # should start with caps.
print(my_boolean) # لقد اعطينا قيم الصواب من عندنا
print(2 == 3) #   == هنا نحن نسال
print('hello' == 'hello')
x = 7
print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)
# if condition : ststements
x = 42
if x > 5:
    print('x is greater than 5')
num = 12
if num > 5:
    print('bigger than 5')
    if num <= 47:
        print('between 5 and 47')

x = 4
if x == 5:
    print('yes')
else:
    print('no')
#استخدام هذه الطريقه للتحقق من القيم قيمه قيمه وهي جمله if داخل else
num = 3
if num == 1:
    print('one')
else:
    if num == 2:
        print('two')
    else:
        if num == 3:
            print('three')
        else:
            print('something else')
# تحويل الجمله العلويه بطريقه. elif
num = 3
if num == 1:
    print('one')
elif num == 2:
    print('two')
elif num == 3:
    print('three')
else:
    print('something else')
#boolean logic
print( 1 == 1 and 2 == 2)
print( 1 == 1 and 2 == 3)
print( 1 != 1 and 2 == 2)
print( 2 < 1 and 3 > 6)
print( 1 == 1 or 2 == 2)
print( 1 == 1 or 2 == 3)
print( 1 != 1 or 2 == 2)
print( 2 < 1 or 3 > 6)
age = 15
money = 500
if age > 18 or money > 100:
    print("welcome")
print(not 1 == 1)#لحلها نري نتيجه المقارنه ثم نعكسها
print(not 1 > 7)
#while loops
i = 1
while i <= 5: # طالما يتحقق الشرط تجري الدوره
    print(i)
    i = i + 1
print('finished') # عندما تنكسر الدوره هذا مايطبع
i = 3
while i >= 0:
    print(i)
    i = i - 1
x = 1
# even pr odd
while x < 10:
    if x%2 == 0:
        print(str(x) + ' is even')
    else:
        print(str(x) + " is odd")
    x += 1
#break and continue 
i = 0
while True: 
    print(i)
    i = i + 1
    if i  >= 5:
        print('breaking')
        break
print('finished') # نلاحظ انها ستطبع في النهايه

i = 1
while i <= 5:
    print(i)
    i+=1
    if i ==3:
        print('skipping 3')
        continue # للمواصله بعد تحقيق الشرط لباقي اللوب
#BMI
height = float(input('Enter your height in cm : '))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
# قسمنا علي ١٠٠ لتحويلها الي متر
if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are normal")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")
    
    
#
x = height = 1.7
y = weight = 130
BMI = y / (x)**2


if BMI <= 18.4:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
elif BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")
