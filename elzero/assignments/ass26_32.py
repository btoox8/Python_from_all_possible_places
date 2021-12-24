## 26 - 32 ##
# 1 #

my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4
unigue_list = list(set(my_list))
#unigue_list = [1,2,3,4,5]
print(unigue_list)
print(type(unigue_list))
unigue_list.pop()
print(unigue_list)


# 2 #

nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

print(nums | letters)
print(nums & letters)
print(nums ^ letters)

# 3 #
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}

print(my_set)
my_set.clear()
print(my_set)
my_set.add('A')
my_set.add('B')
print(my_set)
print(my_set.discard('C'))      # NOTE: delete without error from set

# 4 #
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output 
# True

if (set_one - set_two) != None:
    print('True')

# 5 #
# Create Dictionary Here
dict = {}
# Needed Output
# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"
# "AI Progress Is 20%"

dict['Html'] = 'Progress Is 90%'
dict['CSS'] = 'Progress Is 80%'
dict['Python'] = 'Progress Is 30%'
dict['AI'] = 'Progress Is 20%'
print(dict)

