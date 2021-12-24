#os compose of kernal and user space.
#python is cross platform
#python --version
#python3 --version
#python moduld publish in pypi, python package index
#pip used to update,install and remove external modules
#ضع صاح علي تسطيب المسار لاستخدامه في الطرفيه
#pip install request
#لاحظ التنزيل من الطرفيه وليس البرنامج
'''
import requests
response =requests.get('http://www.google.com')
import arrow
date = arrow.get('2020-01-18', 'YYYY-MM-DD')
date.shift(weeks=+6).formay('MM DD YYYY')
'''
#حسب توزيعات لينكس يختلف امر اداره الملفات
#apt,yum,def
#sudo apt install python3-pil
'''
import PIL.Image
image = PIL.Image.open('house.jpg')
print(image.size)
print(image.format)
'''

#sudo apt install python3-pip
#pip3 install pandas
'''
import pandas
visitors = [1235,6424,9345,8464,2345]
errors = [23,45,33,45,76]
df = pandas.DataFrame( p{'visitors': visitors,'errors'=errors}, index=['mon','tuse','wed','thu','fri'])
print(df)
df['errors'].mean()
#data frame = df
#ctrld linux == ctrlz windows
#cat google2.py
#python3 google2.py
'''
'''
shebang
افتح الملف عن طريق 
nano
nano google2.py
اكتب بداخلها
#!/usr/bin/env python3
الان 
chmod
chmod +x google2.py
هذا يعني انه اذا كتبنا قبله 
./
سيفتح تلقائيا
./google2.py  ===  python3 google2.py

'''

#استدعاء وظيفه من ملفاتك لاستخدامها في اخر
'''
cat areas.py
import math
def triangle(base,height):
	return base*height/2
def rectangle(base,height):
	return base*height
def circle(base,height):
	return math.pi*(radius**2)
	
	
في ملف جديد
import areas
areas.triangle(3,5)
areas.circle(5,7)

يمكننا البحث عن ملف معين بلغه بايثون داخل المكتبات
ls -l /usr/lib/python3/dist-packages/requests
'''
#IDEs
'''
ides== integrated development environment
vim google2.py
atom google2.py
'''


