i = 0

while i <=10:
    i = i +1
    if i == 5:
        continue    ## skip this
    if i == 9:
        break       ## go outside the loop
    print(i)
else:               ## not excute if we use break
    print('the condition was false')