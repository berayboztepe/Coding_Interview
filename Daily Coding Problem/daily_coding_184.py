# This problem was asked by Amazon.
# Given n numbers, find the greatest common denominator between them.
# For example, given the numbers [42, 56, 14], return 14.

n, denomitor = [14, 56, 42], 0

for i in range(1, min(n)+1):
    control = True
    for j in n:
        if j % i != 0:
            control = False
            break
    if control == True:
        denomitor = i

print(denomitor)