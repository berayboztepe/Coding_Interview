#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

from num2words import num2words

list = []
sum = 0
for i in range(1, 1001):                #to convert nums to words and add them to the list with the help of num2words func.
    list.append(num2words(i))


for i in range(1000):
    counter = 0
    for j in list[i]:
        if j == " " or j == "-":        # but fe: 155 = one hundred and fifty-five so we have to get rid of " " and "-"
            counter += 1                #if str = " " or "-" counter = counter+1
    sum += len(list[i-1]) - counter     #and sub them from len of the list
print(sum)
