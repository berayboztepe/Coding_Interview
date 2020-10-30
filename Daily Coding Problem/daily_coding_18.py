#This problem was asked by Google.
#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
#For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#•	10 = max(10, 5, 2)
#•	7 = max(5, 2, 7)
#•	8 = max(2, 7, 8)
#•	8 = max(7, 8, 7)
#Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

k = int(input("Write a number : "))

def find_max(array, k):
    counter = k-1
    for i in range(len(array)):
        list = []
        counter += 1
        if counter <= len(array):
            for j in range(i, counter):
                list.append(array[j])
            print(max(list))

find_max([10, 5, 2, 7, 8, 7], k)