from math import sqrt
from sympy import FiniteSet

primes = []
def check_prime(number):
    if number != 1:
        for i in range(2, int(sqrt(number) + 1)):
            if number % i == 0:
                return False
    else:
        return False
    return True
i = 3

while True:
    if check_prime(i):
        primes.append(i)
    else:
        for j in primes:
            a = sqrt((i-j)/2)
            b = int(sqrt((i-j)/2))
            if sqrt((i - j)/2) == int(sqrt((i - j)/2)):
                break
        else:
            break
    i += 2

print(i)


