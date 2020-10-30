#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

f = open("names.txt", "r")
list, list1, list2 = [], [], []
names = f.readlines()

d ={'A': 1, 'B': 2, 'C': 3, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}


for line in names:
    words = line.split(",")
    for word in words:
        list.append(word)

list.sort()



def find_worth_of_name():
    for i in range(len(list)):
        sum = 0
        for j in list[i]:
            if not j == '"':
                sum += d[j]
        list1.append(sum)
    return list1

def find_the_name():
    for i in range(len(list)):
        list2.append(i+1)

    return list2

def obtain_score():
    sum = 0
    list1 = find_worth_of_name()
    list2 = find_the_name()
    obt = 1
    for i in range(len(list1)):
        obt = list1[i] * list2[i]
        sum += obt
    return sum


print(obtain_score())
