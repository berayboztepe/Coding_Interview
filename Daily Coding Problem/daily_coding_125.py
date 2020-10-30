#This problem was asked by Google.
#Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
#For example, given the following tree and K of 20
  #  10
   #/   \
 #5      15
#       /  \
 #    11    15
#Return the nodes 5 and 15.
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

K = int(input("Write a number:"))
list = []
def nodes(r):

    if r:
        list.append(r.key)
        nodes(r.left)
        nodes(r.right)
def sumofnodes(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == K:
                return list[i], list[j]
    return 0



r = Node(10)
r.left = (Node(5))
r.right = (Node(15))
r.right.left = (Node(11))
r.right.right = (Node(15))

nodes(r)

if sumofnodes(list) == 0:
    print("No sums = K")
else:
    print(sumofnodes(list))
