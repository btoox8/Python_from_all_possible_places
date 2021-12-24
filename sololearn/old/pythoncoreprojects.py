#***Pro projects of python core***

#3-2 : brain freeze

'''
Today is a holiday at the children's camp, so all the children will be served ice cream. There are 3 groups of children: 23 children in the first group, 27 in the second, and 18 in the third. Every child should get 2 scoops of ice cream. Write a program to calculate and output the total number of ice cream scoops we need.
 ----
 '''
kids = 23 + 27 + 18 
print(kids / 2) 
print((23+ 27 + 18)/ 2) 

   ##another answer
   

if (23+27+18)%2 == 0: 
    print("The Scoop of ice cream is enough for the 3 group") 
else:
    print("You need to get", ' ', "scoop of ice cream more")




#6-2 : student text book

'''


We need to distribute math and history textbooks to students. There are 2 class sections: the first section has 18 pupils, and the second one has 19. The total number of books available for distribution is 76. Write a program to calculate and output how many books will be left after each student receives both books.


'''
num1 = 18
num2 = 19
num3 = (num1 + num2) * 2 
num4 = 76 - num3 
print(num4)

#9-2 :

text = input()
d = dict.fromkeys(text, 0) 
print(d)
for c in text: 
    d[c] += 1
    print(d)


if any(i>1 for i in d.values()):
   print("Deja Vu")
  
else:
     print("Unique")

In your solution a=d[c]  is storing value of the last character which can have a value greater than 1 or not ,if it doesn't have value greater than 1 then it will output unique even if other characters before it are repeated


#10-2 : More line, more better

'''

I'm trying the code coach More line, More better which asks this: Working with strings is an essential programming skill. Task: The given code outputs A B C D (each letter is separated by a space). Modify the code to output each letter on a separate line, resulting in the following output: 
A 
B 
C 
D 

Which I anwser this to: 

'''

print('A \nB \nC \nD') 





