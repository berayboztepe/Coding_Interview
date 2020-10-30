# This problem was asked by Airbnb.
# Given a linked list and a positive integer k, rotate the list to the right by k places.
# For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
# Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)
list = []


k = int(input("Print a number:"))

def order(a):
    if a:
        list.append(a.value)
        order(a.next)
    return list

iter = a


for i in range(k):
    while iter.next != None:
        z = iter
        iter = iter.next
    z.next = None
    iter.next = a
    a = iter


#print('->'.join(str(x) for x in order(a)))
                    #or
print('->'.join(map(str, order(a))))


