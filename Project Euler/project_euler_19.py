#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
years = []
days1 = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
counter = 0

for i in range(1901, 2001):
    years.append(i)

l = 1
for i in range(len(years)):
    y = years[i%101]
    if y % 4 == 0 and y != 1900:
        days[1] = 29
    else:
        days[1] = 28
    for j in range(len(months)):
        m = months[j%12]
        for k in range(days[j]):
            d1 = days1[l%len(days1)]
            l += 1
            if d1 == days1[6] and k+1 == 1:
                counter += 1
            #print("year = ", y, "month = ", m, "day = ", k+1, "that day is = ", d1)

print(counter)