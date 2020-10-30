#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_fifth_powers():
    list = []
    for i in range(1000, 1000000): #if we reduce top limit, it will give the same result!, there are no numbers under 1000 that give the answer!
        sum1 = 0
        n = i
        while i:
            digit = i % 10
            sum1 += pow(digit, 5)

            i //= 10
        if n == sum1:
            list.append(n)
    return sum(list)

print(sum_of_fifth_powers())
