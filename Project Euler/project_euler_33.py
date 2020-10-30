#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe
            #   that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value,
            # and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
list1 = []
for i in range(10, 100):
    for j in range(10, 100):
        a, b = i, j
        lista, listb = [], []
        while a:
            digit = a % 10
            lista.append(digit)

            a //= 10
        while b:
            digit = b % 10
            listb.append(digit)

            b //= 10
        a1, b1 = 1, 1
        if 0 not in lista:
            if 0 not in listb:
                if lista[0] in listb:
                    a1 = lista[1]
                elif lista[1] in listb:
                    a1 = lista[0]

                if listb[0] in lista:
                    b1 = listb[1]
                elif listb[1] in lista:
                    b1 = listb[0]

        if i/j == a1 / b1 and i != j:
            if not [i, j] in list1:
                if not [j, i] in list1:
                    list1.append([i, j])

result = [1, 1]
for f in list1:
    result[0] *= f[0]
    result[1] *= f[1]


print(result[1]/result[0])
