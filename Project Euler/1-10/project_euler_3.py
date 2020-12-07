#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

a=600851475143
i=2
c=2
d=3

for i in range(2,a):
    if(a%i==0):
        for c in range(2,i):
            if(i%c==0):
                d=1
                break
            else:
                d=0
        if(d==0):
            print(i)


