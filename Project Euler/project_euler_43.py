#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
        # but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.


from itertools import permutations



primes = [2, 3, 5, 7, 11, 13, 17]


def digits(n):
    n = str(n)
    list = []

    for i in range(1, len(n)-2):
        list.append(int(str(n)[i] + str(n)[i+1] + str(n)[i+2]))

    for i in range(len(list)):
        if list[i] % primes[i] != 0:
            return False
    return True

def palindromic_num(n):
    list = []
    a = n
    while n:
        digit = n % 10
        if digit in list:
            return False
        else:
            list.append(digit)

        n //= 10
    for i in range(len(str(a))):
        if not i in list:
            return False

    if digits(a) == True:
        return a

    return False

sum = 0

i = permutations('0123456789')
for n in i:
    if palindromic_num(int(''.join(n))) != False:
        sum += palindromic_num(int(''.join(n)))


print(sum)