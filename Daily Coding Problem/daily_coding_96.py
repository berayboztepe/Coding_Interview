#This problem was asked by Microsoft.
#Given a number in the form of a list of digits, return all possible permutations.
#For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].



from itertools import permutations

list1 = [1, 2, 3]

def find_permutations():
    return list(permutations(list1))

print(find_permutations())

