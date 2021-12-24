## 33 - 37 ##
# 1 #
print(bool(1))
print(bool(True))
print(bool('string'))
print(bool([1]))
print('#'* 30)
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(False))
print(bool(0))
print(bool(None))
print('#'* 30)


# 2 #
html = 80
css = 60
javascript = 70

# Needed Output
#True

print(bool(html > 50 and css > 50 and javascript > 50))

# 3 #
num_one = 10
num_two = 20
num = 20

# Needed Output
#True
#False
x = bool( (num > num_one and num <= num_two) or (num > num_two and num <= num_one) )
y = bool( (num > num_one and num > num_two) )
print(x,'\n',y)

# 4 #
num_one = 10
num_two = 20

# Needed Output
# 30
# 27000
# 1000
# 200.0
# <class 'str'>

result = num_one + num_two
print(result)
x = result ** 3
print(x)
y = x % 26000
print(y)
z = y / 5
print(z)
print(type(str(z)))

## 38 - 40 ##

# 1 #
# Input
#"     osAmA   "
# Needed Output
#"Hello Osama, Happy To See You Here."

text = input('   osama     \n').strip().title()
print(text)

# 2 #

# Inputs

# Input One 16
# Input Two 24

# Needed Output
# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" # If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" # If Age Is 16+

age = int(input('Your age : \n'))

if age >= 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
else:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")


# 3 #

# Inputs

#"Osama" # First Name
#"Mohamed" # Second Name

# Needed Output
# "Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."

first_name = input("Osama").strip().title()
second_name = input("Mohamed").strip().title()

print(f"Hello {first_name} {second_name[0]}.")

# 4 #

# Inputs

# "Osama@Nn.Sa" # Email

# # Needed Output

# "Your Name Is Osama"
# "Email Service Provider Is nn"
# "Top Level Domain Is sa"

#email = input('email').strip().lower()
email = "Osama@Nn.Sa"
#stop = email.find('@')
#print(stop)
#message = f"Your name is {email[:stop]}"
message = f"Your name is {email [:email.find('@')].title()}"
print(message)
domain = f"Email Service Provider Is {email [email.find('@') + 1 :(email.find('@')) + 3 ]}"
print(domain)
top_level_domain = f"Top Level Domain Is {email [email.find('.') + 1 :(email.find('.')) + 3 ]}"
print(top_level_domain)