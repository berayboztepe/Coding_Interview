#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


a = str()
for n in range(1, 1000000):
    a += str(n)

sum = int(a[0]) * int(a[9]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999])

print(sum)