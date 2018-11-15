"""The collatz conjecture takes a number n. If n is even, it is divided by 2.
if n is odd, it is multiplied by 3 and 1 is added (3*n+1). The purpose of the
sequence is to observe how n reaches zero. if n is 1, it will calculate to 4 an then
go back to 1. In the loop below, we exit when the calculation reaches 1 to avoid
an endless loop"""

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))
