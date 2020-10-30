#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
    # and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def truncatable_primes_left(n):
    if isPrime(n) == True:
        if len(str(n)) != 1:
            for i in range(len(str(n)) - 1):
                mulp = pow(10, len(str(n)) - 1)
                a = (n // (mulp))
                n -= a * mulp
                if isPrime(n) != True:
                    return False
            return True

def truncatable_primes_right(n):
    if isPrime(n) == True:
        if len(str(n)) != 1:
            for i in range(len(str(n)) - 1):
                n //= 10
                if isPrime(n) != True:
                    return False
            return True

def numbers():
    list = []
    n = 11
    while len(list) < 11:
        if truncatable_primes_left(n) == True and truncatable_primes_right(n) == True:
            list.append(n)
        n += 1
    return sum(list)

print(numbers())






