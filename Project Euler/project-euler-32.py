# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


list, list1, list2, list4 = [], [], [], []
sum = 0
def my_frequency_with_dic(list):
    frequency_dict = {}
    for item in list:
        if(item in frequency_dict):
            return 0
        else:
            frequency_dict[item] = 1
    return frequency_dict

for j in range(10, 10000):
    ab = j
    q = 0
    while ab:
        digit = ab % 10
        if not digit in list:
            list.append(digit)
        else:
            list.clear()
            q = 1
            break
        ab //= 10
    if q == 1:
        continue
    for i in range(2, int((j**(1/2))) + 1):
        b = i

        if j % i == 0:
            a = int(j/i)
            while i:
                digit = i % 10
                list1.append(digit)
                i //= 10
            while a:
                digit = a % 10
                list2.append(digit)
                a //= 10
            list4 += list1
            list4 += list2
            list4 += list
            dict = my_frequency_with_dic(list4)
            if not dict == 0:
                for k in range(1, 10):
                    if 0 in dict.keys():
                        list4.clear()
                        list1.clear()
                        list2.clear()
                        break
                    if k in dict.keys():
                        if k == 9:
                            print(j, b, j/b)
                            q = 1
                            sum += j
                        else:
                            continue
                    else:
                        list4.clear()
                        list1.clear()
                        list2.clear()
                        break
            else:
                list4.clear()
                list1.clear()
                list2.clear()
        if q == 1:
            break
    list.clear()

print(sum)
