#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

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

list2 = []
def is_circular_primes(n):
    n = str(n)
    list1 = []
    for i in range(len(n)):
        n = n[-1:] + n[:-1]

        list1.append(int(n))
    list1.reverse()
    if isPrime(list1[0]) == True:
        for j in range(len(list1)):
            if isPrime(list1[j]) == False:
                return False
        return True


def numbers():
    for n in range(2, 1000000):
        if is_circular_primes(n) == True:
            list2.append(n)

    return len(list2)

print(numbers())