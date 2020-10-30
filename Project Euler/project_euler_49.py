#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
    # (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
    # but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations
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
list3 = []
def unusual_way_numbers(n):
    list1, list2 = [], []
    while n:
        digit = n % 10
        list1.append(digit)
        n //= 10

    for i in range(len(list(permutations(list1)))):
        a = str()
        for j in range(len(list(permutations(list1))[i])):
            a += str(list(permutations(list1))[i][j])
        list2.append(int(a))
    list2 = sorted(list2)
    list1.clear()
    if not len(str(list2[0])) == 3:
        for i in range(6):
            for j in range(6, 12):
                for k in range(12, len(list2)):
                    if (list2[j] - list2[i]) == (list2[k] - list2[j]):
                        if isPrime(list2[i]) and isPrime(list2[j]) and isPrime(list2[k]) == True:
                            if not list2[i] in list3:
                                if not list2[j] in list3:
                                    if not list2[k] in list3:
                                        list3.append(list2[i])
                                        list3.append(list2[j])
                                        list3.append(list2[k])
                                        print(list2[i], list2[j], list2[k])
                                        return list3
    return 0

def numbers():
    for n in range(2000, 10000):
        if unusual_way_numbers(n) != 0:
            break
    return unusual_way_numbers(n)

print(numbers())
