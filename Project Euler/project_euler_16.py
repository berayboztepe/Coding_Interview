#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

import math

def find_sum_of_digits_of_pow():
    n = pow(2, 1000)
    sum = 0
    while n:
        digit = n % 10
        sum += digit

        n //= 10
    return sum

print(find_sum_of_digits_of_pow())