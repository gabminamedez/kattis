cases = int(input())

for i in range(cases):
    count = int(input())

    places = []
    total = 0
    for j in range(count):
        loc = input()
        if loc not in places:
            total += 1

        places.append(loc)

    print(total)
