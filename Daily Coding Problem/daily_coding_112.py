#This problem was asked by Twitter.
#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Assume that each node in the tree also has a pointer to its parent.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w
            #   as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

list1, list2, list4 = [], [], []


def keys_of_nodes(root):
    if root:
        list4.append(root.key)
        keys_of_nodes(root.left)
        keys_of_nodes(root.right)
    return list4

def ancestors1(root, key1):
    if not key1 in list4:
        print("The key has not found!")
        return
    if root:
        if key1 < root.key:
            list1.append(root.key)
            ancestors1(root.left, key1)
        elif key1 > root.key:
            list1.append(root.key)
            ancestors1(root.right, key1)
        else:
            if key1 == root.key:
                list1.append(root.key)

    return list1

def ancestors2(root, key2):
    if not key2 in list4:
        print("The key has not found!")
        return
    if root:
        if key2 < root.key:
            list2.append(root.key)
            ancestors2(root.left, key2)
        elif key2 > root.key:
            list2.append(root.key)
            ancestors2(root.right, key2)
        else:
            if key2 == root.key:
                list2.append(root.key)
            else:
                print("The key has not found!")

    return list2

def common_ancestors():
    list3 = []
    if len(list1) == 0 or len(list2) == 0:
        print("These two keys do not have common ancestors!")
        return
    else:
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    list3.append(list2[j])

        list3.reverse()
        return list3[0]

#       20
#     /   \
#    8     22
#   / \
#  4  12
#    /  \
#   10  14

r = Node(20)
r.left = (Node(8))
r.left.left = (Node(4))
r.left.right = (Node(12))
r.left.right.left = (Node(10))
r.left.right.right = (Node(14))
r.right = (Node(22))

keys_of_nodes(r)
ancestors1(r, r.left.right.left.key)
ancestors2(r, r.right.key)
print("LCA of %d and %d is = " %(r.left.right.left.key, r.right.key), common_ancestors())
