#revers_string
## first method
text = input('Enter your text to reverse it\n')
print(text[::-1])

## second method
## make my reverse function

# definition of the reverse function 
def reverse_string(string): 
  #create an empty string
  str = "" 
  #looping from the end of the string's array
  for i in string: 
    #adding the current characte to the empty string
    str = i + str
  return str

myString = input("Enter a string : ")
print(reverse_string(myString))


# full program

 
#pedritooo
#simple string reverse program for command line

string_inputstring = str(input("Please enter a string to reverse>> "))

def reverse_string(input):
	reversedstring = input[::-1]
	return reversedstring

newstring = reverse_string(string_inputstring)
print(newstring)	


answer = str(input("Wanna reverse more strings?").lower())
while answer == 'yes':
	string_inputstring = str(input("Please enter a string to reverse or type quit() to exit>> "))
	if string_inputstring == 'quit()':
		print('Have a nice day!!!')
		break
	else:
		newstring = reverse_string(string_inputstring)
		print(newstring)
if answer == 'no':
	print('Have a nice day!!!')







   

