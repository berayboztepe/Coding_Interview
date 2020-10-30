"""This problem was asked by Google.
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false."""

#a = "abc"
#b = "acb"
a = "abcde"
b = "cdeab"

def can_be_shifted():
    l = []
    l1 = []
    l2 = []
    for i in a:
        l.append(i)
    for i in b:
        l2.append(i)
    for i in range(len(l)):
        l = l[-1:] + l[:-1]
        l1.append(l)
    for i in range(len(l1)):
        if l1[i] == l2:
            return True
    return False

print(can_be_shifted())