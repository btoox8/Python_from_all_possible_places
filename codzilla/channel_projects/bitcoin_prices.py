def power(base_num,pow_num):
    result = 1   # 1 x num = num
    for index in range(pow_num):   # number of times we x this base_num
        result = result * base_num
    return result

print(power(2,3))