range1 = int(input())
range2 = int(input())
sum = int(input())

origRange1 = range1

min = None
max = None

while range1 <= range2:
    nums = [int(dig) for dig in str(range1)]

    sumDigs = 0
    for i in nums:
        sumDigs += i

    if sumDigs == sum:
        min = range1
        break

    range1 += 1

while range2 >= origRange1:
    nums = [int(dig) for dig in str(range2)]

    sumDigs = 0
    for i in nums:
        sumDigs += i

    if sumDigs == sum:
        max = range2
        break

    range2 -= 1

print(min)
print(max)