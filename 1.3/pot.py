count = int(input())

total = 0
for i in range(count):
    num = input()
    exponent = num[len(num) - 1]
    base = num[:len(num) - 1]
    total += int(base)**int(exponent)

print(total)
