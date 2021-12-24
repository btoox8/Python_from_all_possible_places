# 1 #
# name = 'Mohamed Ahmed'
# age = 31
# counrty = 'Sudan'

# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt

# text = f"\"Hello '{name}', How You Doing \\ \"\"\""" Your Age Is \"{age}\"\""" + And Your Country Is: {country}"
# print(text)
# text = "\"Hello '{:s}', How You Doing \\ \"\"\""" Your Age Is \"{:d}\"\""" + And Your Country Is: {:s}".format(name,age,counrty)
# print(text)


# 2 #
# "Hello 'Osama', How You Doing \
# """ Your Age Is "38"" +
# And Your Country Is: Egypt

# text2 = "\"Hello '{:s}', How You Doing \\ \n\"\"\""" Your Age Is \"{:d}\"\""" + \nAnd Your Country Is: {:s}".format(name,age,counrty)
# print(text2)


# 3 #
# name = 'Elzero'

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

# output = name[1]
# output2 = name[2]
# output3 = name[-1]
# print(f'Second Letter Is "{output}"\nThird Letter Is "{output2}"\nLast Letter Is "{output3}"')

# 4 #
# name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"

# output = name[1:4]
# output2 = name[::2]
# output3 = name[-2::-2]          ## nice one
# print(f'lze = "{output}"\nEzr = "{output2}"\nrzE = "{output3}"')

# 5 #
# name = "#@#@Elzero#@#@"

# # Needed Output
# # Elzero

# output = name.strip('#@')       ## should be in " "
# print(output)

# 6 #
# num = "9"
# num2 = "15"
# num3 = "130"
# num4 = "950"
# num5 = "1500"

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

# a = num.zfill(4)
# b = num2.zfill(4)
# c = num3.zfill(4)
# d = num4.zfill(4)
# e = num5.zfill(4)

# print(a,"\n",b,"\n",c,"\n",d,"\n",e)

# 7 #
# name_one = "Osama"
# name_two = "Osama_Elzero"

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

# x = name_one.center(20 , '@')           ## (int  , str)
# z = name_two.center(20 , "@")

# print(x,'\n',z)


# 8 #
# name_one = "OSamA"
# name_two = "osaMA"

# # Needed Output
# # osAMa
# # OSAma

# x = name_one.swapcase()
# z = name_two.swapcase()
# print(x,'\n',z)

# 9 #

# msg = "I Love Python And Although Love Elzero Web School"

# # Needed Output
# # 2

# x = msg.count('Love')
# print(x)

# # 10 #
# name = "Elzero"
# # Needed Output
# # 2

# z = name.index('z')       ## index or find the string to find its position
# #z = name.find('z')
# print(z)

# # 11 # 

# msg = "I <3 Python And Although <3 Elzero Web School"

# # Needed Output
# # I Love Python And Although <3 Elzero Web School

# x = msg.replace('<3',"Love", 1)
# print(x)

# # 12 #

# msg = "I <3 Python And Although <3 Elzero Web School"

# # Needed Output
# # I Love Python And Although Love Elzero Web School

# x = msg.replace('<3',"Love")
# print(x)


# # 13 #

# name = "Osama"
# age = 38
# country = "Egypt"

# # Needed Output Using f""
# # My Name Is Osama, And My Age Is 38, And My Country Is Egypt

# x = f'My Name Is {name}, And My Age Is {age}, And My Country Is {country}'
# print(x)