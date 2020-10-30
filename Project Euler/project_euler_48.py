#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

sum, list, a = 0, [], str()
for i in range(1, 1001): sum += pow(i, i)
for i in range(10):
    digit = sum % 10
    list.append(digit)
    sum //= 10
list.reverse()
for i in list: a += str(i)
print(a)