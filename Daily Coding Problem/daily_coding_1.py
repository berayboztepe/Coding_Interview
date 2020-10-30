#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

k = int(input("Write a number: "))

def isTrue(list1, k):
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] + list1[j] == k:
                return True

    return False

print(isTrue([10, 3, 5, 7], k))