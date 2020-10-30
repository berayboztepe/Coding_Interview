#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    #For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?

import math

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largest_pandigital_prime(n):
    list = []
    counter = 0
    a = n
    while n:
        digit = n % 10
        counter += 1
        if digit in list:
            return False
        else:
            list.append(digit)

        n //= 10
    for j in range(1, counter+1):
        if j not in list:
            return False
    if isPrime(a) == True:
        return True
    else:
        return False


def numbers():
    n = 1
    while n != 10000000:
        if largest_pandigital_prime(n) == True:
            a = n
        n += 1
    print(a)
numbers()

