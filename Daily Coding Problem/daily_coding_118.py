#This problem was asked by Google.
#Given a sorted list of integers, square the elements and give the output in sorted order.
#For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


list = [-9, -2, 0, 2, 3]
def newlist(list):
    for i in range(len(list)):
        list[i] = (list[i]**2)
    #return sorted(list)
            #or
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[j] < list[i]:
                temp= list[j]
                list[j] = list[i]
                list[i] = temp
    return list

print(newlist(list))