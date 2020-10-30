#This problem was asked by Google.
#Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#In this example, assume nodes with the same value are the exact same node objects.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

list1, list2 = [], []
def find_first_values(A, B):
    global list1, list2
    if A and B:
        list1.append(A.value)
        list2.append(B.value)
        find_first_values(A.next, B.next)

def if_same_nodes_equals_same_object():
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            return list1[i]
    return 0


A = Node(3)
A.next = Node(7)
A.next.next = Node(8)
A.next.next.next = Node(10)

B = Node(99)
B.next = Node(1)
B.next.next = Node(8)
B.next.next.next = Node(10)

find_first_values(A, B)
if(if_same_nodes_equals_same_object()) == 0:
    print("The nodes are not intersecting")
else:
    print(if_same_nodes_equals_same_object())

