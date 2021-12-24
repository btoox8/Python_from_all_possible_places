####### 19 + 20 ######
# 1 #
a = 1+2j

# Print Imaginary Part Here
# Print Real Part Here
print(a.imag)
print(a.real)

# 2 # 
num = 10
                                                                              ## flag ##
# Needed Ouput
# 10.0000000000                                                            ## not work with zfill
#print('%.10f' % num)                                                      ## old school deal with float
print('{0:.10f}'.format(num))                                             ## second
#print('{:.10f}'.format(num))                                               ##third

# 3 #
num = 159.650

# Needed Output
# 159
# <class 'int'>

x = int(num)
print(x)
print(type(x))

# 4 #

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 // 11)
print(int (97 / 20))

####### 21 - 23 #######
# 1 #
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama" => Method One
# "Osama" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

# 2 #
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

print(friends[::2])
print(friends[1:4:2])

# 3 #
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "Ahmed", "Sayed", "Ali",
# "Ali", "Mahmoud"
print(friends[1:-1:1])
print(friends[3:])

# 4 #
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

friends[3] = "Elzero"
friends[-1] = "Elzero"
print(friends)

# 5 #
friends = ["Osama", "Ahmed", "Sayed"]

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Sale]

friends.insert(0,'Nasser')
friends.append('Sale')
print(friends)

# 6 #
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

friends.remove('Nasser')
friends.remove('Osama')
friends.pop()
print(friends)

# 7 #                               ## extend allow us put list items in new one better than append 
friends = ["Ahmed", "Sayed"]        ## witch deal with any list as item stand by itself
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
all_friends = []
all_friends.extend(friends)
all_friends.extend(employees)
all_friends.extend(school)
print(all_friends)

# 8 #
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)


# 9 #                                                                        ## flag ###
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]               ## len(list)

# Needed Output
# 6
print(len(friends))

# 10 #
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web

x = technologies[4][0]
y = technologies[4][-1]
print(x)
print(y)

####### 24 - 25 #######
# 1 #
# Needed Output

# "Osama"
# <class 'tuple'>

x = "Osama",
print(type(x))

# 2 #                                                                ## flag ##
friends = ("Osama", "Ahmed", "Sayed")                           ## use list to edit tuple
                                                                ## len(tuple) , not opposite
# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
x = list(friends)
x[0] = 'Elzero'
print(x)
friends = tuple(x)
print(friends)
print(type(friends))
print(len(friends))

# 3 #
nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(len(nums_and_letters_one))

# 4 #
my_tuple = (1, 2, 3, 4)

# Needed Output

# 1 = a
# 2 = b
# 4 = c

a , b , _ , c = my_tuple
print(a,'\n',b,'\n',c)

