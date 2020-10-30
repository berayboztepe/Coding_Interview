#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math
def fact_equal_number():
    sum1 = 0
    for i in range(3, 1854721):  #the upper bound should be 1854721 at most(according to factorion theory!)
        list1, sum, n = [], 0, i

        while i:
            digit = i % 10
            list1.append(digit)
            i //= 10
        for j in range(len(list1)):
            sum += math.factorial(list1[j])
        if sum == n:
            sum1 += n
    return sum1

print(fact_equal_number())

