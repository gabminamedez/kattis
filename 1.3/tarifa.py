limit = int(input())
count = int(input())

total = limit
for i in range(count):
    num = int(input())

    if num > limit:
        total -= num - limit

    elif num < limit:
        total += limit - num

print(total)
