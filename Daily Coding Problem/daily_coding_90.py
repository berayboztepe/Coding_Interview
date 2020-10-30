#This question was asked by Google.
#Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
from random import randrange

n = 15
l = [10, 8, 4, 7, 5, 8]

def random_generate():
    a = randrange(0, n-1)
    if not a in l:
        print(a)

for i in range(1, 31):#a code that generates 30 values that is not in list! and prints only if is not in list.
    random_generate()
