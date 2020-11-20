"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

n = 10


def Permuted_Multiples(n):
    list, list2 = [], []
    for i in range(1, 7):
        a = n*i
        while a:
            digit = a % 10
            list.append(digit)
            a //= 10
        if i == 1:
            list2 = list.copy()
        else:
            if sorted(list) == sorted(list2):
                list2 = list.copy()
            else:
                return 0
        list.clear()
    return 1

while True:
    if Permuted_Multiples(n) == 1:
        break
    n += 1

print(n)

