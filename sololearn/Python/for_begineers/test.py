"""
Write a function that takes a string and a letter as its arguments 
and returns the count of the letter in the string. Sample Input hello, 
how are you? o Sample Output 3 Explanation: The letter o appears 3 times in the given text.
"""
#write text then write which letter want to know it
#your final code would be text.count(by using this letter repeated)

def nums_letters():
    text = input()
    user = input()
    x = text.count(user)
    print(x)
nums_letters()