import math

count = int(input())

for i in range(count):
    num = int(input())

    factorial = math.factorial(num)
    factorial = str(factorial)
    print(factorial[len(factorial) - 1])
