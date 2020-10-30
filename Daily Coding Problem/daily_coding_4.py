#This problem was asked by Stripe.
#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array.
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_min_pos_int(array):
    i = 0
    while True:
        i += 1
        if not i in array:
            return i


print(find_min_pos_int([3, 4, -1, 1]))