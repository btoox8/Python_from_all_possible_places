
#!--------------
#***data type***
#?--------------

print('--------------------- STRINGS---------------------------')

#!------------
#***strings***
#?------------

'''
  - strings are amongst the most popular types in python. we can create them simply by
    enclosing characters in quotes. python treats single quotes the same as double quotes.
  - creating striings is as simple as assigning a value to a variable.
'''
x = 'ahmed'
y  = "herro"
print(x[1])
print(y[0:4])
print(y[2:])
# نلاحظ العد يبدا من صفر لذا القيمه الثانيه لانصلها انما نتحرك بمقدارها
print(x + y)
print(x * 2)
print(x + x)
#لايمكن ضرب اثنين في بعض ، ولكن يمكن ضربه في عدد لتكراره


## string formating and raw string:::

#*** string formating operator***
print("My name is %s and weight is %d kg" % ('mahmoud', 71))
   #              %s = string      %d = number
'''
print(".  %var1. %var2. %var3" % (value1,value2,value3))

'''
print("My name is {} and weight is {} kg".format('mahmoud', 71))


'''
print("... {} .... {} kg".format(value1, value2))
'''
#*** raw string ***
#الانتباه للباك سلاش اذا اردنا كتابتها وعدم تخطيها

'''
  - #? raw strings don't treat the backslash as a special character at all.
    every character you put into a raw string stays the way you wrote it.
'''

print("c:\python34\scripts")
print("c:\\python34\\scripts")    # just only print \ one time
print(r"c:\\python34\\scripts")   # r = raw , so print all \\

#built-in string methods::

x = "sherazz Is big pipe. hhhh"
y = ' '
print(x.capitalize()) # just first letter on all sentences
print(x.upper())
print(x.lower())
print(y.isspace()) #وجود  is : true or false
print(x.islower()) # should be all lower
print(x.isupper()) # should be all upper
print(x.istitle())
print(x.center(40 , '*')) # return a space-padded string with the 
                          #original string centered to a total of width colmuns.
                          #x.center(total width of new string ,fill character : should be 1 [sign , number,letter])

'''
#? count:
  counts how many times str occurs in string or in a substring of string 
  if string index begging and ending index end are given.
  counts(str,beg=0,end=len(string)) , defult value [from start to the last]
'''

print(x.count('z'))
print(x.count('z', 8))     # 8 == begging
print(x.count('z', 5, 10)) # 8 = beg , 10 = end
#احسب عدد مرات تكرر الحرف في الكل المعطي ، وقد نضيف له مدي ينتهي فيه

'''
endwith:
  determines if string or a substring(if starting index beg and ending index end are given)
  ends with suffixx, returns true if so and false otherwise.
  endwith(suffix,beg=0,end=len(string))  , defult value [from start to the last]
'''
print(x.endswith('zz')) #true or False 
print(x.endswith('az')) # قيمتها الافتراضيه تبدا من الصفر الي طول ال string


'''
find:
  determines if string or a substring(if starting index beg and ending index end are given)
  returns index if found, and -1 if not
  find(str,beg=0,end=len(string))  , defult value [from start to the last]
'''
print(x.find('e')) # give us it's first position
print(x.find('ixx')) # -1 ??? == not found it


print(x.index('e'))

'''
print(x.index('i'))  
#اذا لم يجدها يخرج رساله خطا نصيه بعدم وجوده
substring not found
'''

print(x.istitle()) # true if every word start with capital letter

# replace(old,new,(max))
print(x.replace('e','ii'))       # نستبدل القديم بالجديد
                                 # it change every (e) by (ii)
print(x.replace('e' , 'ii',(5))) #! here we use ,(max) == to stop on certain number of time

'''
split:
  splits string according to delimiter str(space if not provided) and
  returns list of substrings; split into at most num substrings if given
  split(str='your split item',num=string.count(str)) 
'''

# make a list from this string sentence, and split between them by ( , - / ...)
print(x.split(' ')) # تعطينا لسته ، اذا وجدت فراغات يتم استبدالها بما بين القوسين

s = "herro * neeero -teroooo , hhh  ooo"
print(s.split(' '))
print(s.split('-'))
print(s.split(','))
print(s.split('*'))

c = "herro * neeero *teroooo *hhh * ooo"
print(c.split(('*'),3))    # here we choose number of our elements inside a list by index start from zero


print('--------------------- LIST---------------------------')

#!---------
#***list***
#?---------

'''
list:
  - the most basic data structure in python is the sequence. each element of a sequence is
    assigned a number - its position or index. the first index is zero, the second index is one
    and so forth
  - creating a list is as simple as putting different comma-separated values between square brackets.

'''

list1 = ['physics', 'chemistry', 1997, 2000, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", 'b' , "c", "d"]
print(list1[0])
print("list1[3]: ", list1[3])

#updating list (change value for one or more)
list2[3] = "teen"
print(list2[3])  # so 4 become 'teen'

# del (if we know element = value)
del list3[1]
print(list3)

#***built-in list method
#?----------------------

#len(list) : gives the total lenght of the list
#len and index
print(len(list1)) # كم عدد عناصرها
print(list1.index(2000)) #دلني علي مكان القيمه

#insert
list1.insert(3, 'math') # لابد من الخانه ثم القيمه
print(list1)

#append
list2.append('data') # تضاف للنهايه مباشره
print(list2)

#count لعد العنصر وتكراراته
print(list1.count(2000))   # repeat two times

#pop احذف اخر قيمه
# print last value then delet it
print(list1.pop())

#reverse
print(list3.reverse()) #بدل استخدام لووب

#remove نحدد فيها القيمه المراد حذفهت
list1.remove(2000) 
print(list1)      # remove from first place found in it only.


#***math with lists***

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
print(list1+list2)        #! one list with all items 
print(list1* 3)          #? كررها كذا مره وكلها داخل لسته واحده

#***
x = '''
       Welcome
       This is my first lesson
       So lets go
       '''
print(x)

print('--------------------- TUPLES---------------------------')

#!-----------
#***tuples***
#?-----------

#immutable غير قابله للتعديل ولكن يمكن استخدامه لانشاء اخري
#ممكن نتحايل لحل المشكله بالتحويل للست قايمه ثم تعديلها ثم ارجاعها لتيوبل

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,3 ,5)


print("tup1[0]: ", tup1[0])
print("tup1[]: ", tup1[1:])

tup3= tup1 + tup2
print(tup3)

#! امر del للازاله يزيلها كامله وتصبح غير موجوده ولا يمكننا ازاله عنصر من داخلها
'''
del tup3
  print(tup3)
    is not define error
    '''

#indexing, slicing and matrixes
l = (1, 2, 3, 4, 5)
print(l[2])
print(l[-2])
print(l[1:])

#***built-in tuple function***
print(len(l))
print(max(l))
print(min(l))

#listt, tuple
d = list(l)
print(d)

f = tuple(d)
print(f)


print('--------------------- DICTIONARY---------------------------')

#!---------------
#***dictionary***
#?---------------

'''
  - a dictionary is mutable and is another container type that can store any 
    number of python objects, including other container types.
  - dictionaries consist of pairs(called items) of keys and their corresponding values.
  - python dictionaries are also known as associative arrays or hash tables
  - each key is seprated from its value by a colon(:), the items are seprated by commas,
    and the whole thing is enclosed in curly braces. an empty dictionary without any
    items is written with just two curly braces. 

'''
# called also : associative arrays or hash tables
# pairs of   key : value  == called (item)
# في خانت القيم يمكنك استخدام اي شي واي كميه ولكن المفتاح واحد ولا يكرر والا سيكتب قيمه اخر مفتاح
# لانستخدم index لاننا نستعيض عنه بي key
# المفتاح لايمكن ان يكون قايمه , ولكنه يمكن ان يكون str, number, tuple


dict = {'A':1, 'B':2, 'C':'3',4:'D'}
print(dict)

#اذا ااردنا معرفه قيمه معينه ناتي بهاا هكذا key
# we don't use index but its key
print(dict['C'])
print(dict[4])

#modify
dict['B'] = 230 #تبديل قيمه
dict['schools'] = "btoo" #!اضافه كامله  
                         # add it
dict[6] = 2012 #اضافه كامله
                        # add it
print(dict)

#delete

dict = {'A':1, 'B':2, 'C':'3',4:'D'}

del dict['A']
print(dict)
#remove entry with certain key   = key & value


dict = {'A':1, 'B':2, 'C':'3',4:'D'}
print(len(dict))
dict.clear()        #S! clear()
print(len(dict)) # لم يتبقي عنصر
#remove all entries in dict  = empty dict


dict = {'A':1, 'B':2, 'C':'3',4:'D'}
del dict
print(dict)
#delete entire dict


#properties of dict keys
'''
  - dict values have no restrictions. they can be any arbitary python object,
    either standard objects or user-defined objects. however, same is not true for the keys.
  - more than one entry per key not allowed. which means no duplicate key is allowed.
    when duplicated keys encountered during assignment, the last assignment wins.
  - key must be immutable. which means you can use 
    1- strings, 
    2- numbers or 
    3- tuples as
    dictionary keys but something like['key] is not allowed
    noooooooo  list as key

'''
dict = {'name':1,'name':2}  #! تكرار امفتح يذكر قيمة الاخير
print(dict['name'])         # take the last == appear the value

x = dict
print(x)  # appear key & value



#built-in dict
#clear
dict = {'A':1, 'B':2, 'C':'3',4:'D'}
dict.clear()
print(dict)
print(len(dict))


#copy لعمل نسخه كامله منه
dict = {'A':1, 'B':2, 'C':'3',4:'D'}
f = dict.copy()
print(f) # ياخذ نسخه مع اختلاف الترتيب ولا بهمنا لاستخدامنا  key 

#fromkeys
#? ناخذ المفاتيح من المتغير الاول والقيم لكل مفتاح من المتغير الثاني
# dict.fromkeys(x, y)
x = ('key1' , 'key2' , 'key3')
y = 0
dict_from_tuple_var = dict.fromkeys(x ,y)
print(dict_from_tuple_var)

# f = {'1':"ahmed", "age":2}
# x = ("age", "name", 2, "ahmed")
# print(f.fromkeys(x))


#get
#الارجاع للمعلومات فيها يعتمد علي keys فقط

f = {'1':"ahmed", "age":2}
print(f.get('ahmed')) #! value return none
print(f.get('1'))     #  return as value
print(f.get('3'))     #? not in dict return none

#items , don't forget s at end
#استخراج قايمه من القاموس بداخلها tuple
f = {'1':"ahmed", "age":2}
print(f.items())    # it back [(key & values),(k and V)]

#keys
print(f.keys())
#values
print(f.values())


#setdefault
print(f.setdefault('1', 2020))
#لو اعطيناه قيمه خلاص لو لا يكتب القيمه الافتراضيه اللي عندنا ولل none

#update ==  add , just put all together 
f = {'1':"ahmed", "age":2}
x = {'2':"ahmed", "bag":4}
x.update(f) #لابد من كتابته خارج امر الطباعه 
print(x)








