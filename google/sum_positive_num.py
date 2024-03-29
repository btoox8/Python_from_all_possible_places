# use sum_positive as variable

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        pass
        return 0

    else:
        # The recursive case is adding this number to 
        # the sum of the numbers smaller than this one.
        sum = n + sum_positive_numbers(n)

        return sum

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15