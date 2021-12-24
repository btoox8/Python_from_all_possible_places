#Time is precious
# number of seconds on 30 days.

print(30*(24*(60*60)))
print(30*24*60*60)


#Watch out for bacteria
# number of bacteria dublicate every hour (start with 500)

print((500*2)**1) # wrong 
print(500*2**2) 
print(500*2**3)
print(500*2**24) # initial nb * speed of dublication ** nb of hours
print((500*2)**2)  # wrong

#Time is ticking away
#hours in 888 min
print(888/60)
print(888//60)


#Flight time
'''
You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, covering a distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.

Calculate and output the total flight time in hours.

Hint
The result should be a float.
'''
print(7425/550)


#Smart talk
print("\"Stay hungry, stay foolish\" by Steve Jobs")

#Reach for stars

print("""
*
**
***
****
""")

print('* \n** \n*** \n****') # only inside one string

#Just say hello
print('hi' * 42)
print(42 * "hi")


#Leaderboard
"""
You need to make a program for a leaderboard. 
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
"""
print("""
1.
2.
3.
4.
5.
6.
7.
8.
9.
""")


print("1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.")
# if you make space between \n and any input it appear in your program


#Contact card

"""
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]


cont = dict(contacts)
# convert tuple to dict by (dict)
print(cont)
# to make sure it convert

name = input() # enrer name by user

if name in cont: #we called key by name
    print(name,'is',cont[name]) # what appear
       #key , string, key_value
else:
    print('Not found')
"""
#example from me

my_degree = [
('islamic',90),
('pysics',80),
('math',70),
('biology',60)

]

degree = dict(my_degree)
# so here our dict which we use it inside if
print(degree)

material = input('Enter your subject name:')
# our key we use it inside if

if material in degree:
    print(material , 'mark is ', degree[material])
else:
    print('not found')

#another example
 
programming = [
('python',80),
('js',30),
("html",80),
('css',44),
('dart',60)
]

  
#Get notify
#add 3 stars at beggining and end of notification

text = input('Enter your text\n')
print('***' +  text + '****')

#identity cards
#take name and age from user and use them on output

name = input("Enter your name :\n")
age = int(input("Enter your age: \n"))

print("My name is " + name + ' and I\'m ' +str(age))

#Tip calculater


'''
When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.
______________________________________
Your program needs to take the bill amount as input and output the tip as a float.

'''
print("Welcome , Your tip will be 20%")
bill = int(input("Enter your bill:\n"))
tip = bill*20/100
print(tip)

#my example

bill = int(input("Total sales:\n"))
our_discount = bill*15/100
print("Your final bill, "+str(our_discount))
