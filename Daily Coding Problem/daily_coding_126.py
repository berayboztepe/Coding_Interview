#This problem was asked by Facebook.
#Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. 
#How many swap or move operations do you need?

k = int(input("Write a number:"))

def swapper(list):
    list = list[::-1]
    for i in range(k):
        list = list[-1:] + list[:-1]

    return list[::-1]


print(swapper([1, 2, 3, 4, 5, 6]))
#only k operations all I need
