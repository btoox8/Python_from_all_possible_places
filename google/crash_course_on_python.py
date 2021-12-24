# ##
# mylist = [1,2,3,4]
# for x in mylist:
#     print(x*2, "its the new value")
#     #لكل عنصر في المتغير قم بتنفيذ العمليه الاتيه

# ##
# for i in range(10):
#     print('hi, every one')
#     #ناتجها ١٠ عناصر بدل كتابه العناصر قم باستبدال كل عنصر بهذه الجمله
# # من هنا نستتنتج انه يمكننا استخدامها في تكرار الجمل كل سطر ، في حين تكرار الاسترينج بالضرب نجده يتكرر علي نفس السطر ، اذا لم نتدخل للتعديل

# ## 
# print('I\'m btoo')

# ##
# color = "black"
# thing = "sadness"
# print(color,'is color of',thing)

# ##
# print((((1+2)*3)/4)**5)

# ## if we had type error we can use this 
# ## function to know our types
# print(type('hello'))

# ## may we can say variable like a container
#   # هذه اللغه تنفذ القيم تنازليا، اذا الاسفل تستبدل الاعلي
  
# lenght = 10
# width = 2
# area = lenght * width
# print(area)

# ## calc area of triangle
# ## (base*height)/2

# base = 6
# height = 3
# area = (base*height)/2
# print("the area of the triangle is: " + str(area))

# ## average size of 5 different files
# total = 2048 + 4357 + 97658 + 125 + 8
#   # المتغير يمكن ان يكون عمليات زياضية بحته
# files = 5
# average = total / files
# print("The average size is: " + str(average))

# ##
# def greeting(name,department):
#     print("Welcome, "+name)
#     print("You are part of",department,"department")
#     # استخدام الفاصله في تكوين الجمله يعطيك المساحه افضل من +
    

# greeting("btoo","PUBG")

# ## number of seconds from hours,minutes,seconds
# def print_seconds(hours,minutes,seconds):
#     print((hours*3600)+(minutes*60)+seconds)
#     #معرفة الاصغر من الاكبر باستخدام الضرب
#     #نسال نفسنا ماهي معادله حساب عدد الثواني ، من الساعات، من الدقائق، اما الثواني فمجرد ذكرها
#     # الناتج لدبنا هو جمع كل هذه المعطيات بعد ان تحولت لوحده موحده هي الثواني

# print_seconds(1,2,3)

# ## area of triangel
# def area_triangel(base,height):
#     return base*height/2
#    #لم نضع الجمله بين قوسين لان التنفيذ يبدا من اليسار لليمين، وهذا لايفرق هنا لتساوي اولوليه الضرب والقسمه
   
# area_a = area_triangel(5,4)
# area_b = area_triangel(7,3)
# sum = area_a + area_b
# print("The sum of both areas is: " + str(sum))

# ## get_seconds
# def get_seconds(hours,minutes,seconds):
#     return 3600*hours + 60*minutes + seconds

# amount_a = get_seconds(2,30,0)
# amount_b = get_seconds(0,45,15)
# result = amount_a + amount_b
# print(result)

# ## convert_seconds
# ## we calc from upper to lower
# ## we check reminder from upper every next step
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     # عدد الثواني علي ٣٦٠٠
#     minutes = (seconds - hours * 3600) // 60
#     #لاتنسي الاقواس بدونها سينتج معادله بنتائج خاطئه
#     #الدقائق هي عدد الثواني علي ٦٠
#     # لكن كم هو عدد هذه الثواني
#     #عدد الثواني في الوحده الاعلي اي الساعات
#     # منقوص منه عدد الثواني 
#     # الكل مقسوم علي ٦٠
    
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     # الثواني المتبقيه، قم بنقصان الوحدتين الاعلي من الثواني
#     # نلاحظ دون قسمه لاننا في الوحده الادني
    
#     return hours, minutes , remaining_seconds
#    # جمله الارجاع تعود بثلاث متغيرات
   
# hours , minutes , seconds = convert_seconds(5000)
#   # لابد من كتابه ٣ متغيرات مع مساواتها بالوظيفه وقيمتها، لكي نستخرح ٣ قيم كنتيجه
  
# print(convert_seconds) ## not appear , just its place inside memory
# print(hours , minutes , seconds) ## the three variabels name 
#                                 ## from function abpve

# a,b,c = convert_seconds(5000)  ## we just use any 3 vars
# print(a,b,c)

# ## lucky_number
# def lucky_number(name):
#     number = len(name) * 9
#     # انشاء متغير وربطه بعمليه علي متغيرنا الرئيسي
#     print("Hello "+ name + ". Your lucky number is " + str(number))

# lucky_number("Kay")
# lucky_number("Mohammed")
# lucky_number("btoo")

# ##
# def month_days(month,days):
#     return f'{month} has {days} days.'
# print(month_days('June',30))   
# print(month_days("july",31))


# ## circle_area (our code was refractor
# #استخدم كلمات تدل علي ماتفعله الوظيفه عند تسمية المتغيرات

# def circle_area(radius):
#     pi = 3.14
#     area = pi * (radius ** 2)
#     print(area)

# circle_area(5)

# ## rectangle_area
# def rectangle_area(base,hight):
#     area = base * hight
#     print("The area is " + str(area))

# rectangle_area(5,6)

# ## fun with color
#   #هنا نتحدث عن علامات مقارنه لذا الناتج اما صواب اوخطا
# print("Yellow" > "Cyan" and "Brown" > "Magenta")
# print("Yellow" > "Cyan" or "Brown" > "Magenta")
# print("Yellow" > "Cyan" and "Brown" < "Magenta")

# print(1 == "1") 
# # هنا السوال هل هما نفس نوع البيانات

# ##Branching  == make descition


# ## username not less than 3 chrt
# def hint_username(username):
#     if len(username) <3:
#         print("Invalid username. Must be at least 3 characters long")

# hint_username("btoo") ## not excute becuse our condition not happing 
# # ليس لدينا جمله توضح ماسيحدث اذا كان الطول اكبر من ٣
# #لذا لن يظهر شيء
# hint_username("bb")

# # ##
# def is_positive(number):
#     if number > 0:
#         return True
#     return False  ## How using return instade of else !!!
        
# #       #تعريف الموجب

# print(is_positive(5))
# print(is_positive(0))
# print(is_positive(-5))


# ## even number
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False  ## not excuite except if was wrong
    
#     #قاعده الزوجي،اذا لم تتحقق في نفس المستري جمله الارجاع تعود بانها جمله خاطئه

# print(is_even(8))
# print(is_even(7))



# ## week 3 ##
# #_______________________________________________________#
# print('########### welcome to week  ############')

# x = 0
# while x < 5:
#     print("Not there yet, x=" + str(x)) # the body of loop
#     x = x + 1
# print("x=" + str(x)) # if loop finish , so condition was false

# ## loop inside function
# def attempts(n):
#     x = 1
#     while x <= n:
#                 #لابد من ربطها مع المتغير العلوي للوظيفه
#                 # سناخذ الرقم الذي سيكتب بالمستخدم كاساس للحلقه التكراريه
#         print("Attempt " + str(x))
#         x += 1
#     print("Done")

# attempts(5)

# ##
   
# '''
# username = get_username()
# while not valid_username(username):
#     print("Invalid_username")
#     username = get_username()

# '''

# ##
# #حلقه لمتغيرين
# # نهايتها ، ينتج عنها القيمه النهائيه للمتغيرين المعطيان
# x = 1
# summ = 0
# while x < 10:
#     # احد المتغيرين به شرط التوقف للحلقه
#     summ += x 
#     # العلاقه الرياضيه للاول
#     x += 1
#     # المتغير المتحكم في الحلقه
#     print(summ,x)
    
    
    
#    ## you should make another variable for t
#    ##to start from 0 not to start from last value from above loop
# product = 1
# x = 1
# while x < 10:
#     product = product * x
#     x += 1
# print(summ,product)
# # اخذنا قيمه
# #summ
# # من اعلي قيمه وصلتها الوظيفه السابقه

# ## infinity loop
# # عندما تكتب حلقه لشرط دايما حدوثه صحيح
# '''
# while x % 2 == 0:
#     x = x /2
# '''
#     ## solve it
#     # لتخطيها يمكننا تعديل الحلقه
#     #a#
# if x != 0:
#     while x % 2 == 0:
#         x = x /2
#     #b#
# while x !=0 and x % 2 == 0:
#     x = x /2
# '''
# while True:
#     do_something_cool()
#     if user_requested_to_stop():
#         break
# '''

# ##
# for x in range(10):
#     print(x)

# ##
# friends = ["broo",'ahmed','hassan']
# for friend in friends:
#     #الاسناد المتغير جديد مننا نحن
#     # لكل عنصر في القائمه
#     #لينفذ عليه امر معين علي طول صحه الحلقه
#     print("Hello",friend)
# ##
# values = [23,52,59,37,48]
# sum = 0
# lenght = 0
# for value in values:
#     sum += value  # take all values and adding each together
#     lenght += 1   # take number of values

# print("Total sum: " + str(sum) + " - Average: " + str(sum/lenght))
#    # ماهي الا طريقه حساب المعدل
#    # حيث اضافه صفر للعناصر لن توثر
#    # ولحساب عدد العناصر وضعنا متغير يزداد تدريجيا بمقدار واحد
#     #الي انتهاء الحلقه

# ##
# '''
# we use for loop : iterate over a sequence of elements
# while loop: action over and over until a condition has changed
# '''
# ##
# product2 = 1
# for n in range(1,5): ## we start from 1 , because if start by 0 all result will be 0
#     product2 *=n 

# print(product2) 

# ##  not true
# def factorial(n): 
#     result = 1
#     # المتغير الحكم في القصه
#     for i in range(1,n+1):
#         # تبدا من واحد لانو من الصفر حتقيف في الضرب
#         #المدي لابد يشمل اخر قيمه تكتب
#         result = result * (n-1)
#         # لابد من ان نتناقص تدريجيا 
#         # مع الضرب في المتغير الحاكم
        
#     return result

# print(factorial(4))
# print(factorial(5))

# ##
# def to_celsius(x):
#     return (x - 32) * 5/9
#     # هذه وظيفه منفصله
#     # استخدم وظيفه في لوب

# for x in range(0,101,10):
#     # كتبنا شروط اللوب 
#     # ربطنا متغيرنا الخاص لاستخدامه كمتغير في الرظيفه العلويه
#     #لابد من وجود المتغير في الوظيفه والحلقه
#     print(x, to_celsius(x))

# #------------------------- week 4 -------------------------------
# def double_word(word):
# 	return word *2 + str(len(word*2))
	
# print(double_word('hello'))
# ##

# def first_and_last(message):
# 	if message[0] == message [-1]:
# 	       return True
# 	       if message=='':
# 	       	return True


# print(first_and_last('else'))
# print(first_and_last(' '))

# ##
# ## انتبه لو كانت بين قوسين ماحتقدر تضيفهم لي بعض ااحقا
# message = 'a kong string with a sily typo'
# print(message)
# new_message = message[:2]+'l'+message[3:]
# print(new_message)
# print(new_message.index('s'))
# ## سيرجع الاول فقط
# print(new_message.index('long'))
# ##سيرجع مكان بدايه النص

# #يممننا استخدام التحقق لجزء من النص
# pets = 'cats and dogs'

# print('cats' in pets)
# print('dragon' in pets)
# print('dragon' not in pets)

# ## بدل الدومين لايميلات معينه
# def replace_domain(email,old_domain,new_domain):
# 	if '@' + old_domain in email:
# 		index = email.index('@'+old_domain)
# 		new_email = email[:index] + '@'+ new_domain
# 		return new_email
# 	return email
		
		
# print(replace_domain('gg','btoo','jhk'))

# ## to avoid value error
# # is string in, get it by index
# a = 'lions tigers and bears'
# print('bears' in a)
# print(a.index('bears'))
# print(a.index('and'))
# b = a[:13] + 'hourses ' + a[13:]
# print(b)

# ##  .strip() 
# ##تزيل المساحات البيضاء والاسطر الجديده
# #lstrip()  add space to left
# #rstrip() add space to right
# print('   yes   btoo   '.strip())
# print('yes'.rstrip())
# print('yes'.lstrip())

# #some string methods
# #upper(),lower(),strip(),isnumeric(),isalpha(),count(),endswith(),replace(old,new),delimiter.join(list of string)


# #join
# #مايكتب بين الكلمات
# #.join
# #([our string])
# a = ' '.join(['this','is','btoo'])
# b = '...'.join(['this','is','btoo'])
# print(a)
# print(b)

# #split()
# #لتحويل كل كلمه في النص لجزو من قايمه
# a = 'this is another example'.split()
# print(a)

# #formatting string
# name = 'manny'
# number = len(name) * 3
#     ## first
# print('hello {}, your lucky number is {}'.format(name,number))
#     ## second way
# print('your lucky number is {number}, {name}'.format(name = name,number= len(name)*3))

# ## 
# price = 7.5
# with_tax = price * 1.09  # 1.09 == 9%
# print(price,with_tax)
#        ## استخدام التقريب
#        ## :.2f
# print('Base price: ${:.2f}. with Tax: ${:.2f}'.format(price,with_tax))

# ##نلاحظ يمكننا زياده خانات التقريب 
# print('Base price: ${:.4f}. with Tax: ${:.4f}'.format(price,with_tax))

# # :>3 let space to right equal 3
# def to_celsius(x):
# 	return (x-32)*5/9
	
# for x in range(0,101,10):
# 	print('{:>3} F | {:6.2f} C'.format(x,to_celsius(x)))