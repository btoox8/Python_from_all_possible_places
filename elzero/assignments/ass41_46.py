## 41 - 46 ##
# 1 #
# Inputs

# def op(num1,num2,op):
#     num1 = input('num1').strip()
#     num2 = input('num2').strip()
#     num1 = int(num1)
#     num2 = int(num2)
#     operation = input('"+" Or "-" Or "*" Or "/" Or "%"').strip()
#     if operation == '+':
#         return num1 + num2
#     elif operation == '-':
#         return num1 - num2
#     elif operation == '*':
#         return num1 * num2
#     elif operation == '/':
#         return num1 / num2
#     elif operation == '%':
#         return num1 % num2

# print(op(20,40,'+'))
# print(op(20,40,'*'))

# # Needed Output

# # [num1 20] [operation +] [num2]
# # Example One 20 + 40 = 60
# Example Two 20 * 40 = 800


# 2 #

# age = 17

# # Needed Output

# # If Age Larger Than 6
# # if Age Smaller Than 16

# print("App Is Not Suitable For You") if age >= 16 else print("App Is Not Suitable For You")


# 3 #
# Input Example 38

# # Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

# age = int(input('You\'re age is : '))

# def age_calc(age):
#     age_weeks = age * 52
#     age_month = age * 12
#     age_days = age * 365
#     age_hours = age_days * 24
#     age_min = age_hours * 60
#     age_sec = age_min * 60
#     return age_month,age_weeks,age_days,age_hours,age_min,age_sec

# if age > 100 or age < 10 :
#     print("We can't do it")
# else:
#     print(age_calc(age))

# 4 #
# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country\n")
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

if country in countries:
    new_price = price - discount
    print("Your Country Eligible For Discount And The Price After Discount Is $70")
else:
    print("Your Country Not Eligible For Discount And The Price Is $100")