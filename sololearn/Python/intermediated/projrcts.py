#TODO: Letter Counter
'''
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.

Sample Input
hello

Sample Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
You need to output the dictionary object.
Note, that the letters are in the order of appearance in the string.
'''
text = 'hello'
dict = {}
#your code goes here
for letter in text:
    # we enter to string
    # our letter now is key for dict
    # how count repearing
    if letter not in dict:
        dict[letter]=1
        
    else:
        dict[letter]+=1 
print(dict)


########
text = 'hello'
print({letter_as_key:text.count(letter_as_key) for letter_as_key in set(text)})

# NOTE:
'''
pure function : all args inside it
impure function : use args from out the function
higher function : use function on other as args or in return sentences
'''


# TODO: Spelling Backwards
'''
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
Complete the recursive spell() function to produce the expected result.
'''

def spell(txt):
    #your code goes here
    return txt[::-1]
    

txt = input()
print(spell(txt))
