from math import sqrt


# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?
tut = {}
for b in range(1, 500):
    for a in range(b, 500):
        c = sqrt((a**2) + (b**2))
        if a+b+c <= 1000 and int(c) == c:
            if a+b+c in tut:
                tut[a+b+c] += 1
            else:
                tut[a+b+c] = 1




print(int(max(tut, key=tut.get)), ',', max(tut.values()))
