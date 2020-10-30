#This problem was asked by Google.
#Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
#For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

list = []

def keys(n):
    if n:
        list.append(n.key)
        keys(n.next)

    list2 = list.copy()
    return list2

def isPalindrome(list):

    if list == list[::-1]: return True
    else: return False

n = Node(1)#answer is True
n.next = Node(4)
n.next.next = Node(3)
n.next.next.next = Node(4)
n.next.next.next.next = Node(1)
"""n = Node(1)#answer is False
n.next = Node(4)"""


print(isPalindrome(keys(n)))

