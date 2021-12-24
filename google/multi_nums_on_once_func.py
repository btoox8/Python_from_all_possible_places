def factorial(n): 
    result = 1
    sum = 1
    # المتغير الحكم في القصه
    for i in range(1,n+1):
        # تبدا من واحد لانو من الصفر حتقيف في الضرب
        #المدي لابد يشمل اخر قيمه تكتب
        #print(i)
        result *= i
    return result
        #print(result)
        # result = result * (n-1)

        # sum += result
        # print('r',result)
        # print('s',sum)
        # لابد من ان نتناقص تدريجيا 
        # مع الضرب في المتغير الحاكم
        
    #return sum

print(factorial(4))
print(factorial(5))
