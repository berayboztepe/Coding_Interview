#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
a=3
b=4
sonuc=0

for a in range(3,500):
    for b in range(4,500):
        c=((a**2)+(b**2))**(1/2)
        sonuc=a+b+c
        if (a < b and a < c and b < c):
             if (sonuc == 1000):
                 print(a*b*c)
                 break

