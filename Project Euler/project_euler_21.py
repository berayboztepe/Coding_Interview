#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.
def d(n):
    list = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)

    return sum(list)

def sum_of_amicable(a, b):
    sum1 = 0
    if a != b:
        if a in list:
            return 0
        else:
            if d(a) == b and d(b) == a:
                list.append(a)
                list.append(b)
                sum1 += (a+b)
    return sum1
list = []
sum1 = 0
for i in range(1, 10000):
        sum1 += sum_of_amicable(i, d(i))

print(sum1)