string = input()

cups = [1, 0, 0]

for letter in string:
    cupA = cups[0]
    cupB = cups[1]
    cupC = cups[2]

    if letter == "A":
        cups[0] = cupB
        cups[1] = cupA
    elif letter == "B":
        cups[1] = cupC
        cups[2] = cupB
    elif letter == "C":
        cups[0] = cupC
        cups[2] = cupA

print(cups.index(1) + 1)