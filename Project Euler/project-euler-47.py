from math import sqrt

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def check_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


primes = []

for i in range(2, 1000):
    if check_prime(i):
        primes.append(i)

n = 1000
consecutive = []

while True:
    bolenler  = []
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            if (i in primes):
                bolenler.append(i)
            if n/i in primes:
                bolenler.append(int(n/i))
    if len(bolenler) == 4:
        if len(consecutive) == 0:
            consecutive.append(n)

        else:
            if n == consecutive[0] + 1:
                consecutive.append(n)
            elif n == consecutive[1] + 1:
                consecutive.append(n)
            elif n == consecutive[2] + 1:
                consecutive.append(n)
                break

            else:
                consecutive.clear()
    else:
        if len(consecutive) != 0:
            consecutive.clear()
    n += 1

print(consecutive)
