#This question was asked by ContextLogic.
#Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.

def division(number1, number2):
    if number1 > number2:
        quotient = 0
        for i in range(1, number1+1):
            if i % number2 == 0:
                quotient += 1

    else:
        quotient = 0
        for i in range(1, number2 + 1):
            if i % number1 == 0:
                quotient += 1

    return quotient

print(division(7, 25))#random number can be assigned