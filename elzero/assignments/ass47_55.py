## 47 - 51 ##
# 1 #

num = int(input('num'))
l = []

if num == 0:
    print("Number 0 Is Not Larger Than 0")
else:
    for n in range(1,num):
        l.append(n)
        if n == 6:
            continue
        #print(l)
        x = l[::-1]
        l = x
        print(x[n - 1])
    
# # Input
# num = 0

# # Needed Output
# "Number 0 Is Not Larger Than 0"
# # Input
# num = 10

# # Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."