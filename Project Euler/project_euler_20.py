#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!


def sum_of_fact():
    fact = 1
    sum = 0
    for i in range(1, 101):
        fact *= i

    while fact:
        digit = fact % 10
        sum += digit

        fact //= 10
    return sum

print(sum_of_fact())