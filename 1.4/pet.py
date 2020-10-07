one = input()
one = [int(num) for num in one.split()]
two = input()
two = [int(num) for num in two.split()]
three = input()
three = [int(num) for num in three.split()]
four = input()
four = [int(num) for num in four.split()]
five = input()
five = [int(num) for num in five.split()]

scores = [one[0] + one[1] + one[2] + one[3],
          two[0] + two[1] + two[2] + two[3],
          three[0] + three[1] + three[2] + three[3],
          four[0] + four[1] + four[2] + four[3],
          five[0] + five[1] + five[2] + five[3]]

highest = max(scores)
for i in range(len(scores)):
    if scores[i] == highest:
        winner = i + 1
        break

print(str(winner) + " " + str(highest))
