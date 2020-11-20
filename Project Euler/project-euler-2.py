from math import sqrt
n = 600851475143

def check_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True




for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        if check_prime(i):
            print(i)

