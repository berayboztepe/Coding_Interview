#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)
def isPalindromic_numbers(n):

    n = str(n)
    for i in range(len(n) // 2 ):
        if n[i] != n[len(n) - (i+1)]:
            return False

    return True

def isPalindromic_binaries(n):
    n = bin(n)[2:]
    n = str(n)
    for i in range(len(n) // 2 ):
        if n[i] != n[len(n) - (i+1)]:
            return False
    return True

def numbers():
    list1 = []
    for n in range(1, 1000000):
        if isPalindromic_binaries(n) == True and isPalindromic_numbers(n) == True:
            list1.append(n)
    return sum(list1), list1
print(numbers())