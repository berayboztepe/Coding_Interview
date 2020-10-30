#The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
        # For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall
                # call the word a triangle word.

#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
        # how many are triangle words?

f = open("words.txt", "r")
list, trianglen = [], []
names = f.readlines()

d ={'A': 1, 'B': 2, 'C': 3, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}


for line in names:
    words = line.split(",")
    for word in words:
        list.append(word)

for i in range(1, 26*3+1):
    trianglen.append(int(i*(i+1)/2))



def value_of_words():
    counter = 0
    for i in range(len(list)):
        sum = 0
        for j in list[i]:
            if not j  == '"':
                sum += d[j]
        if sum in trianglen:
            counter += 1
    return counter
print(value_of_words())