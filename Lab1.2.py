import sys
import math

Numbers = []
Complex = []
Real = []
Rational = []
Whole = []
Natural = []
Even = []
Odd = []
Prime = []

def check_prime(number):
    if (int(number) < 2): return
    if int(number) == 2:
        Prime.append(number)
    else:
        i = 2
        limit = int(math.sqrt(int(number)))
        while i <= limit:
            if int(number) % i == 0:
                return
            i += 1
        Prime.append(number)


print("Введите числа через запятую\n")
numbers = list(input().split(','))
print(numbers)

for number in numbers:
    if "i" in number:
        Complex.append(number)
    else:
        Rational.append(number)
        if "." in number:
            Real.append(number)
        else:
            Whole.append(number)
            if int(number) > 0:
                Natural.append(number)
            if int(number) % 2 == 0:
                Even.append(number)
            else:
                Odd.append(number)
            check_prime(number)

print("Complex\n", Complex)
print("Real\n", Real)
print("Rational\n", Rational)
print("Whole\n", Whole)
print("Natural\n", Natural)
print("Even\n", Even)
print("Odd\n", Odd)
print("Prime\n", Prime)



