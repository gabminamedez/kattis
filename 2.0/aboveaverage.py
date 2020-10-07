cases = int(input())

for i in range(cases):
    students = input()
    students = [int(student) for student in students.split()]

    total = 0
    for j in range(1, students[0] + 1):
        total += students[j]

    average = total / students[0]

    aboveAvg = 0
    for j in range(1, students[0] + 1):
        if students[j] > average:
            aboveAvg += 1

    pctg = aboveAvg / students[0] * 100
    pctg = format(pctg, '.3f')

    print(str(pctg) + "%")